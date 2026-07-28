from datetime import datetime
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from scrapping.image_downloader import download_image
from google_api.drive import create_folder, upload_image
from logs.logger import default_logger
from scrapping.scrapper import page_scraper

CHROMEDRIVER_PATH = "chromedriver/chromedriver.exe"
BASE_URL = "https://books.toscrape.com/catalogue/page-1.html"


def main():
    os.makedirs("images", exist_ok=True)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    folder_name = f"BooksScraper_{datetime.now():%Y%m%d_%H%M%S}"
    folder_id = create_folder(folder_name)

    default_logger.info(f"Pasta criada no Google Drive: {folder_name}")

    try:
        driver.get(BASE_URL)
        for page in range(1, 3):
            books = page_scraper(driver)

            for book in books:
                download_image(book["cover"], book["name"])

            for image_file in os.listdir("images"):
                image_path = os.path.join("images", image_file)
                upload_image(image_path, '12j3Mked1OpYQihPs22pk6FwJSV1yog8F')
                default_logger.info(f"Imagem enviada para o Google Drive: {image_file}")

        driver.find_element("xpath", '//*[@id="default"]/div/div/div/div/section/div[2]/div/ul/li[3]').click()

    finally:
        driver.quit()
        default_logger.info("Execução finalizada.")


if __name__ == "__main__":
    main()