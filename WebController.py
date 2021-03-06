from selenium import webdriver
from bs4 import BeautifulSoup as bs
import urllib.request as ul
import shutil
import os
from Recognizer import Recognizer  # 파이썬의 클래스 개념이란.....?


'''

|필독|
urlretrieve 가 로컬파일에 대하여 작동하지 않으므로 로컬파일 전용 테스트 파일 WebControllerForLocal.py 로 분리했습니다.
온라인에서(e.g. 네이버, 구글, etc.) 모든 사진을 다운받는 과정을 체크하시고 싶으시다면 README.md를 참고하여 이 파일을 실행하시기 바랍니다.
Recognizing 과정을 보시고 싶으시다면 WebControllerForLocal.py 파일을 실행하시기 바랍니다.

'''



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
        for img in enumerate(img_src):  # 특 : enumerate 겁나 편한데 사실 다른 언어 for(;;)은 그냥 기본.. 이지만 자바에 enhanced for syntax 있다는 점
            print(img)  #tuple(enum, img_link)
            try:
                ul.urlretrieve(img[1], f'./Temp/{img[0]}.png')  # 이미지는 temp에 따온 순서의 번호로 이름을 지정
            except :  # HTTPError 인데 모듈 임포트 다시 해야해서 특정 안함
                try:
                    print("Trying another way to retrieve img . . .")
                    ul.urlretrieve(page_url + img[1], f'./Temp/{img[0]}.png')
                except: pass

        print("Recognizing character . . .")
        predictions = Recognizer.recognizeImages('./Temp/')








