## Web scraping of Links & Images from Amazon

### Description:

This is about web scraping of links and images from Amazon website using Selenium and Chromedriver. I created this sub-project for my Virtual Bookstore web app - the links and images will be displayed in the search results in the said web app.

This project contains the following:
- main.py
- yaml_reader.py
- chromedriver
- book_info.csv


### Methodology:
This section explains the procedures in completing this project.

1. Connecting to the database (Google BigQuery) to get the list of books I wanted to put on a search in Amazon.
- I created yaml_reader.py to create function for configuration. It's important to keep the project id and credentials confidential.
- The yaml_reader.py will access the config.yaml I created where the project id and credentials path are saved.


