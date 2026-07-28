from datetime import datetime
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scrapping.image_downloader import download_image
from google_api.drive import upload_image
from logs.logger import default_logger
from scrapping.scrapper import page_scraper
from google_api.sheets import create_sheet, insert_books

def main():
    os.makedirs("images", exist_ok=True)
    BASE_URL = "https://books.toscrape.com/catalogue/page-1.html"
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    folder_name = f"BooksScraper_{datetime.now():%Y%m%d_%H%M%S}"

    default_logger.info(f"Pasta criada no Google Drive: {folder_name}")

    try:
        books_data = []
        driver.get(BASE_URL)
        time.sleep(2)
        for page in range(1, 3):
            books = page_scraper(driver)
            books_data.extend(books)

            #for book in books:
            #    download_image(book["cover"], book["name"])
            
            #for image_file in os.listdir("images"):
            #    image_path = os.path.join("images", image_file)
            #    upload_image(image_path, '12j3Mked1OpYQihPs22pk6FwJSV1yog8F')
            #    default_logger.info(f"Imagem enviada para o Google Drive: {image_file}")
            try:
                next_page =driver.find_element("xpath", '//*[@id="default"]/div/div/div/div/section/div[2]/div/ul/li[3]')
                next_page.click()
                time.sleep(2)
            except:
                default_logger.warning("Elemento 'next page' não encontrado.")
                BASE_URL = f"https://books.toscrape.com/catalogue/page-{page+1}.html"

        
    finally:
        sheet_id = create_sheet(
                "Books Scraper"
                )
        
        insert_books(
                sheet_id,
                books_data
                )
        driver.quit()
        default_logger.info("Execução finalizada.")


if __name__ == "__main__":
    main()