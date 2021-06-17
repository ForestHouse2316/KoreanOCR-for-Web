from selenium import webdriver
from bs4 import BeautifulSoup as bs
import urllib.request as ul
import shutil
import os
import time
import threading






# Init browser
driver = webdriver.Chrome('./Korean OCR/WebDriver.exe')
driver.maximize_window()

while True:
    command = input()
    if command == 'exit':
        break
    elif command == '':
        print("Getting page source . . .")
        soup = bs(driver.page_source, 'html.parser')

        print("Analyzing page source . . .")
        img_elements = soup.select("img")  # image elements list
        print(img_elements)
        page_url = driver.current_url
        img_src = []
        for element in img_elements:
            src = element.attrs['src']
            img_src.append(src)

        print("Initializing [Temp] folder . . .")
        if os.path.isdir('Temp'):
            shutil.rmtree('Temp')  # --force
        os.mkdir('Temp')

        print("Downloading image resources . . .")
        for img in enumerate(img_src):  # 요 enumerate 이게 엄~청 편하더군요..! 이런거 자바 util 에다가 만들어두면 꿀빨면서 쓰지 않을까 싶습니다..
            print(img)
            try:
                ul.urlretrieve(img[1], f'./Temp/{img[0]}.png')
            except: HTTPError
                try:
                    ul.urlretrieve(page_url + img[1], f'./Temp/{img[0]}.png')
                except: pass








