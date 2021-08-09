from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
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
    # print(element.text)
#
#     books = result.find_elements_by_class_name("sg-col-inner")
#     for book in books:
#         title = books.find_element_by_class_name("a-link-normal a-text-normal")
#         # link = books.find_element_by_class_name("href")
#         print(title)
# #data component type="s-search-result"
# # a class="a-link-normal a-text-normal"
# # href=

finally:
    driver.quit()

time.sleep(10)

