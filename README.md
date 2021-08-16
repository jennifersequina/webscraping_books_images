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
- I created yaml_reader.py to create function for configuration. It's important to keep the project id and credentials confidential. The yaml_reader.py will access the config.yaml I created where the project id and credentials path saved.

2. Setting up the driver to automatically do a search in Amazon website.
- I installed chromedriver using ChromeDriver manager. Note: This will be one-time web scraping, hence it is fine for me to install the chrome driver using the script but if the intention is to scrape on a daily basis or frequently, it should not be like this. The chromedriver should be installed and just use executable path to access it.
- Then I created driver to access amazon website, and used some Selenium locators to access and get the specific element from the HTML (i.e. search bar and the dropdown). NOTE: In accessing the web elements it's important to understand and check the HTML (right-click > inspect) to get the correct class, tag name or path.
- I put inside the exception handling function (try-finally) the script that will access the website and get the links and images of the first result.
- I collated the results in list, converted them to dataframes and saved as CSV file.

### Usage:

I will be using the result to continue the other project about virtual bookstore.
This also can be replicated in other websites such as airbnb, google, etc. whichever might be interesting for you to scrape! :)

