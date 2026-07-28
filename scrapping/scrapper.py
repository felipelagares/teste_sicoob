import selenium
from logs.logger import default_logger


def page_scraper(driver: selenium.webdriver.Chrome):
    books = []
    for index in range(1, 21):
        book_xpath = f'//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[{index}]'

        image = "/article/div[1]/a/img"
        book_cover = driver.find_element(
            "xpath", book_xpath + image).get_attribute("src")

        name_path = "/article/h3/a"
        book_name = driver.find_element("xpath", book_xpath + name_path).text

        price_path = "/article/div[2]/p[1]"
        book_price = driver.find_element("xpath", book_xpath + price_path).text

        rating_path = "/article/p"
        book_rating = driver.find_element("xpath", book_xpath + rating_path).get_attribute("class")
        book_rating = book_rating.replace("star-rating ", "")

        availability_path = "/article/div[2]/p[2]"
        book_availability = driver.find_element(
            "xpath", book_xpath + availability_path).text

        default_logger.info(f"\nindex: {index}\n Book Name: {book_name}\n Book Price: {book_price}\n Book Rating: {book_rating}\n Book Availability: {book_availability}\n")

        books.append({
            "name": book_name,
            "cover": book_cover,
            "price": book_price,
            "rating": book_rating,
            "availability": book_availability
        })

    return books