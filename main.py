from datetime import datetime
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from scrapping.image_downloader import download_image
from scrapping.scrapper import page_scraper

from google_api.drive import create_folder, upload_image
from google_api.sheets import create_sheet, insert_books

from logs.logger import default_logger


def main():

    os.makedirs("images", exist_ok=True)

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    folder_name = f"BooksScraper_{datetime.now():%Y%m%d_%H%M%S}"

    books_data = []

    try:

        # Cria pasta no Drive
        folder_id = create_folder(folder_name)

        default_logger.info(
            f"Pasta criada no Drive: {folder_name}"
        )


        for page in range(1, 4):

            url = (
                f"https://books.toscrape.com/"
                f"catalogue/page-{page}.html"
            )

            default_logger.info(
                f"Acessando página {page}"
            )

            driver.get(url)

            time.sleep(2)

            books = page_scraper(driver)


            for book in books:

                try:

                    # Baixa imagem
                    image_path = download_image(
                    book["cover"],
                    book["name"]
                    )


                    # Upload Drive
                    drive_link = upload_image(
                    image_path,
                    folder_id
                    )

                    default_logger.info(
                        f"Upload concluído: {drive_link}"
                    )


                    book["cover"] = drive_link


                    default_logger.info(
                        f"Imagem enviada: {book['name']}"
                    )


                except Exception as e:

                    default_logger.exception(
                        f"Erro imagem {book['name']}: {e}"
                    )


            books_data.extend(books)


        # Criar planilha
        sheet_id = create_sheet(
            "Books Scraper"
        )


        insert_books(
            sheet_id,
            books_data
        )


        default_logger.info(
            "Planilha criada com sucesso"
        )


    except Exception as e:

        default_logger.exception(
            f"Erro na execução: {e}"
        )


    finally:

        driver.quit()

        default_logger.info(
            "Execução finalizada."
        )


if __name__ == "__main__":
    main()