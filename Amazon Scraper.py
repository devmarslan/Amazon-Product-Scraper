import csv
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request,response
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

link = input("Enter Link: ")
driver = webdriver.Chrome(ChromeDriverManager().install())

# a1 = driver.find_element(By.XPATH, '//*[@id="a-autoid-7-announce"]/img').get_attribute("src")
# print(a1)


record_no = 0
page_no = 1
records = []
while True:
    counter = 1
    url = link+"&page="+str(page_no)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    results = soup.find_all('div', {'data-component-type': 's-search-result'})
    for i in results:
        print(counter)
        try:
            driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div['+str(counter)+']/div/div/div/div/div[2]/div[1]/h2/a').click()
            url = driver.current_url
            try:
                title = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text
            except:
                title = ""
            try:
                price = driver.find_element(By.CLASS_NAME, 'a-price').text
            except:
                price = ""
            try:
                delivery = driver.find_element(By.XPATH, '//*[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]/span').text
            except:
                delivery = ""
            try:
                stock = driver.find_element(By.XPATH, '//*[@id="availability"]/span').text
            except:
                stock = ""
            try:
                color = driver.find_element(By.XPATH, '//*[@id="variation_color_name"]/div/span').text
            except:
                color = ""
            try:
                sold_by = driver.find_element(By.XPATH, '//*[@id="tabular-buybox"]/div[1]/div[4]').text
            except:
                sold_by = ""
            try:
                brand = driver.find_element(By.CLASS_NAME, 'po-brand').text
            except:
                brand = ""
            try:
                model_name = driver.find_element(By.CLASS_NAME, "po-model_name").text
            except:
                model_name = ""
            try:
                age_range = driver.find_element(By.CLASS_NAME, "po-age_range_description").text
            except:
                age_range = ""
            try:
                power_source = driver.find_element(By.CLASS_NAME, "po-power_source_type").text
            except:
                power_source = ""
            try:
                about_item = driver.find_element(By.XPATH, '//*[@id="feature-bullets"]/ul').text
            except:
                about_item = ""
            try:
                product_dimension = driver.find_element(By.XPATH, '//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[1]/td').text
            except:
                product_dimension = ""
            try:
                item_weight = driver.find_element(By.XPATH, '//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[2]/td').text
            except:
                item_weight = ""
            try:
                safety_info = driver.find_element(By.XPATH, '//*[@id="important-information"]/div/p[2]').text
            except:
                safety_info = ""
            img1 = "1"
            img2 = "2"
            img3 = "3"
            img4 = "4"
            img5 = "5"
            for x in range(1, 20):
                if img1 == "1" or '360' in img1:
                    try:
                        img1 = driver.find_element(By.XPATH, '//*[@id="a-autoid-' + str(x) + '-announce"]/img').get_attribute("src")
                    except:
                        img1 = "1"
                    try:
                        img2 = driver.find_element(By.XPATH, '//*[@id="a-autoid-' + str(x + 1) + '-announce"]/img').get_attribute("src")
                    except:
                        img2 = "2"
                    try:
                        img3 = driver.find_element(By.XPATH, '//*[@id="a-autoid-' + str(x + 2) + '-announce"]/img').get_attribute("src")
                    except:
                        img3 = "3"
                    try:
                        img4 = driver.find_element(By.XPATH, '//*[@id="a-autoid-' + str(x + 3) + '-announce"]/img').get_attribute("src")
                    except:
                        img4 = "4"
                    try:
                        img5 = driver.find_element(By.XPATH, '//*[@id="a-autoid-' + str(x + 4) + '-announce"]/img').get_attribute("src")
                    except:
                        img5 = "5"
                else:
                    break

            if color == '':
                try:
                    color = driver.find_element(By.CLASS_NAME, 'po-color').text
                except:
                    color = ""

            edit_price = about_item.replace("【", "[")
            record = [url, title, str(price), delivery, stock, color, sold_by, brand[6:], model_name[11:], age_range[24:], power_source[13:], edit_price.replace("】", "]"), product_dimension, item_weight, safety_info, img1.replace("US40_", ""), img2.replace("US40_", ""), img3.replace("US40_", ""), img4.replace("US40_", ""), img5.replace("US40_", "")]
            records.append(record)
            record_no = record_no + 1
            print(record)
            print("*****"+str(record_no)+"*****")
            driver.back()

        except:
            print("Not Found")

        counter = counter + 1

    page_no = page_no + 1
    if page_no > 13:
        break

with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Url', 'Title', 'Price', 'Delivery', 'Stock', 'Colour', 'Sold By', 'Brand', 'Model Name', 'Age Range', 'Power Source', 'About Item', 'Product Dimension', 'Item Weight', 'Safety Info', 'Img1', 'Img2', 'Img3', 'Img4', 'Img5'])
    writer.writerows(records)