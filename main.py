from google.cloud import bigquery
from google.oauth2 import service_account
from yaml_reader import read_config
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

config = read_config('config/config.yaml')

project_id = config['project_id']
credentials = service_account.Credentials.from_service_account_file(config['credentials_path'])
client = bigquery.Client(credentials=credentials, project=project_id)

query = f"""
            SELECT title
            FROM `{project_id}.dev.books_data`
            """
rows = client.query(query=query).result()
title_list = list()
for r in rows:
    title_list.append(list(r.values()))

driver = webdriver.Chrome(ChromeDriverManager().install())

books_info = list()
for title in title_list:
    title_dict = dict()
    if isinstance(title, list):
        title_dict['title'] = title[0]
    else:
        title_dict['title'] = title

    driver.get("https://www.amazon.com")
    dropdown = driver.find_element_by_xpath("//option[@value='search-alias=stripbooks-intl-ship']")
    dropdown.click()
    search = driver.find_element_by_id('twotabsearchtextbox')
    search.send_keys(title)
    search.send_keys(Keys.RETURN)

    try:
        result = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.ID, "search"))
        )
        books = result.find_elements_by_class_name("sg-col-inner")

        for index, book in enumerate(books):
            if index == 0:
                links = book.find_elements_by_xpath("//a[@class='a-link-normal a-text-normal']")
                for link_index, link in enumerate(links):
                    if link_index == 0:
                        book_link = link.get_attribute("href")
                        print(book_link)
                        title_dict['book_link'] = book_link
                        break

                images = book.find_elements_by_xpath("//img[@class='s-image']")
                for img_index, image in enumerate(images):
                    if img_index == 0:
                        book_image = image.get_attribute("src")
                        print(book_image)
                        title_dict['book_image'] = book_image
                        break
                break
        books_info.append(title_dict)
    finally:
        None

book_info_df = pd.DataFrame(books_info)
book_info_df.to_csv('book_info.csv', index=False)

# # importing csv file to bigquery
# df = pd.read_csv('book_info.csv')
# df.to_gbq('dev.books_info', credentials=credentials, project_id=project_id)