from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
import time
import csv

options = Options()
options.add_argument("--incognite")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

proxylist = []
with open('proxylist.csv', 'r') as f:
    reader = csv.reader(f)
    for proxy in reader:
        proxylist.append(proxy[0])

f = open('CrawlingDataset.csv', 'w', newline='')


def web_crawler(URL, n):
    driver.get(URL)
    links = []
    try:
        elements = driver.find_elements_by_tag_name("a")
        for el in elements:
            if el.get_attribute("target") == '_blank':
                links.append(el.get_attribute('href'))
    except StaleElementReferenceException:
        elements = driver.find_elements_by_tag_name("a")
        for el in elements:
            if el.get_attribute("target") == '_blank':
                links.append(el.get_attribute('href'))
    print(len(links))
    # The links don't crawl respectively . The order of the links in list and webpage are different.
    # We give the link of the first product manually.
    temp = []
    for i in range(n):  # We know that there are 36 products in each page so we just need 36 links.
        # Other links are not links of products
        temp.append(links[i])
    links.clear()
    links = temp  # I Used temp because you might not want to crawl all products.
    writer = csv.writer(f)
    writer.writerow(['Product Number', 'Title', 'Image SRC 1', 'Image SRC 2', 'Description'])
    # The first line of our CSV data set.
    i = 1
    for link in links:  # We need to enter to the page of each product one by one to get the
        # information such as two first images and the tag 'This product has been described as'.
        data = [i]
        i += 1

        driver.get(link)
        time.sleep(3)
        elements = driver.find_elements_by_class_name("view-product-title")
        title = [el.text for el in elements]
        title = title[0]  # I wrote this line just because i wanted to convert list to str type.
        title = str(title)
        data.append(title)
        elements = driver.find_elements_by_tag_name("img")
        j = 0
        for el in elements:
            if el.get_attribute(
                    "alt") == title and j != 2:
                # In the assignment , just 2 of the images(If there is any!) are required,
                # so we need j to meet our requirement
                second_image = el.get_attribute("src")
                data.append(second_image)
                j += 1

        elements = driver.find_elements_by_class_name("product-keywords__word")
        description = [el.text for el in elements]
        description_string = ''
        for el in description:  # I'm just doing this to order the descriptions.
            description_string = description_string + ',' + el
        data.append(description_string)
        # TO SEE THE RESULT IN CONSOLE , PLEASE UNCOMMENT THE LINE DOWN BELOW.
        # print(data)
        writer = csv.writer(f)
        writer.writerow(data)
        data.clear()
    f.close()
    driver.close()


def chair_crawling(n):  # n must be lower than or equal to 36
    URLOfChairs = "https://www.houzz.com/products/chairs"
    web_crawler(URLOfChairs, n)


def table_crawling(n):  # n must be lower than or equal to 36
    URLOfTables = "https://www.houzz.com/products/dining-tables"
    web_crawler(URLOfTables, n)


def sofa_crawling(n):  # n must be lower than or equal to 36
    URLOfSofas = "https://www.houzz.com/products/sofas"
    web_crawler(URLOfSofas, n)


def bed_crawling(n):  # n must be lower than or equal to 36
    URLOfBeds = "https://www.houzz.com/products/beds"
    web_crawler(URLOfBeds, n)

# FOR TESTING MY CODE , PLEASE UNCOMMENT THE LINES DOWN HERE :)
########################################################################
# bed_crawling(10)
# chair_crawling(10)
# table_crawling(10)
# sofa_crawling(10)
########################################################################
