from selenium import webdriver
from bs4 import BeautifulSoup as bs
import urllib
import os
import time
import threading

# Declare element extractor
soup = bs('html', 'html.parser')




# Init browser
driver = webdriver.Chrome('./Korean OCR/WebDriver.exe')
driver.maximize_window()

while True:
    command = input()
    if command == 'exit':
        break
    elif command == '':
        print("Getting page source . . .")
        source = driver.page_source
        print("Analyzing page source . . .")
        img_elements = soup.find_all("img") # image elements list
        print(img_elements)
        img_src = []
        for element in img_elements:
            img_src.append(element.attrs['src'])
        print("Downloading image resources . . .")
        urllib.urlretrieve(img_src, img_src)





