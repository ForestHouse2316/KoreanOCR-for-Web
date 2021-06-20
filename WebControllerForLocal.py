from selenium import webdriver
from bs4 import BeautifulSoup as bs
import urllib.request as ul
import shutil
import os
from Recognizer import Recognizer  # 파이썬의 클래스 개념이란.....?


'''

|필독|
urlretrieve 가 로컬파일에 대하여 작동하지 않으므로 로컬파일 전용 테스트 파일 WebControllerForLocal.py 로 분리했습니다.
WebControllerForLocal.py 와는 사용법이 약간 다릅니다. 이 파일은 /WebExample/web.html 에 대해서만 작동합니다.
그러므로 크롬에서 해당 로컬 html의 절대경로를 입력하셔야 합니다. 이후 과정은 기본 메뉴얼과 동일합니다.

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
            except Exception as e:  # HTTPError 인데 모듈 임포트 다시 해야해서 특정 안함
                try:
                    print(e)
                    print("Trying another way to retrieve img . . .")
                    ul.urlretrieve(page_url + img[1], f'./Temp/{img[0]}.png')
                except: pass

        print("Recognizing character . . .")
        # predictions = Recognizer.recognizeImages('./WebExample/temp')
        predictions = Recognizer.recognizeImages('./WebExample/temp')
        print(predictions)








