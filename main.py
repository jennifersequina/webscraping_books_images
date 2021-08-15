
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com")

search = driver.find_element_by_id('twotabsearchtextbox')
search.send_keys('Harry Potter and the Cursed Child, Parts 1 & 2, Special Rehearsal Edition Script')
search.send_keys(Keys.RETURN)

try:
    result = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "search"))
    )

    books = result.find_elements_by_class_name("sg-col-inner")
    for book in books:
        # print(book.text)
        links = book.find_elements_by_xpath("//a[@class='a-link-normal a-text-normal']")
        # print(links)
        for link in links:
            print(link.get_attribute("href"))

finally:
    None
    # driver.quit()

time.sleep(10)