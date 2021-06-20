# KoreanOCR-for-Web
AI_OCR for enhancement of accessibility about web's image resources.


## Sources & References
(취소선은 미사용 소스)  

* ~~Binary형 이미지 데이터셋  (1GB 이하)
https://www.dropbox.com/s/69cwkkqt4m1xl55/phd08.alz?dl=0  
  =>변환기 : https://github.com/sungjunyoung/phd08-conversion~~  

  
* 한국어 구문분석 링크모음  
https://github.com/songys/AwesomeKorean_Data  
  
* AI Hub 대용량 한글 데이터셋 (손글씨, 글꼴, 단어 단위, 실생활) (수십 GB 단위 용량)  
https://aihub.or.kr/aidata/133/download  
  =>시간관계상 인쇄체 Syllable만 사용

* ~~CLOVA 의 OCR 모델  
  https://github.com/clovaai/deep-text-recognition-benchmark~~  

* Python Selenium 의 웹페이지 소스코드 수정  
https://stackoverflow.com/questions/39543237/python-selenium-modifying-the-source-code-of-a-webpage

- KerasLayer 설명  
https://ssongnote.tistory.com/13

- E.g. 사이트  
https://junstar92.tistory.com/154  
~~https://cvml.tistory.com/21~~  

- 신경학개론(기초 ~ 최적화)  
https://sacko.tistory.com/10
  
- 배치 정규화 심화설명  
https://gaussian37.github.io/dl-concept-batchnorm/

- Anaconda Virture Env 에서의 TensorFlow 및 cuDNN 설치법  
https://broscoding.tistory.com/331

-----
## Structures
- Train.py - 학습 시작 지점
- DatasetBuilder.py - AI Hub 가 제공하는 `.json`에서 한글 2350종류만 추출하여 정리한 `.csv`를 통해 학습을 위한 데이터셋 정보 생성
- TrainCallback.py - 학습중 학습 현황 표시와 모델저장을 위한 콜백 클래스
- Model.py & Model.ipynb(test file) - CNN 모델 파일. `.ipynb`는 아래에 있는 현재 구성된 모델의 구성도를 만들기 위해 사용된 파일입니다.
![Failed to load](/Document/Model-Structure.png)
- WebController.py - elenium을 이용하는 웹 접근용 파일

-----
## Processing sequence  
  
### Model Training
#### Composing Training Dataset
먼저 AI Hub 에서 가져온 syllable 데이터에서 현대한글 2350 자만을 사용하기 위해 `.json` 파일에서 2350자에 해당하는 메타데이터를 추출하여 `.csv` 에 정리합니다.  
`Train.py`를 실행하면, 이 `.csv`를 통해 `DatasetBuilder.py`에서 학습 데이터셋의 정보를 배열에 담아 리턴합니다.  
#### Training
가져온 데이터 정보로 학습을 시작합니다. 각 데이터는 상기한 모델 구조를 돌게 됩니다.  
매 학습마다 `TrainCallback.py`를 keras 모듈이 콜백하여 학습 진행 현황 데이터를 넘겨줍니다.  
학습률은 0.001, epoch는 10입니다.  
10 epoch 를 돌며 가장 정확도가 크고 손실이 낮은 모델을 자동으로 `\Korean OCR\saved_model` 에 저장해둡니다.  

---
### Webpage Modifying
#### Opening Window Assigned to WebDriver
사용자가 `WebDriver.exe`(Chrome version) 에 의해 열린 창을 통해 인터넷 검색을 한다고 가정합니다.  
`WebController.py`는 초기에는 해당 창을 띄우기만 할뿐, 특정 사이트에 자동으로 접속하거나 데이터를 긁어오지는 않습니다.  
Selenium에서 드라이버를 연결한 후 `input()`에서 무한루프를 돌며 사용자의 응답을 기다립니다.
#### Replacing HTML Element
`input()`무한루프에서는 현재 기준 두 가지 명령어를 받습니다. `[Enter]`와 `exit` 입니다.  
사용자가 엔터키를 누르게 되면 Selenium은 현재 페이지의 HTML을 가져와 이미지가 있는지 분석합니다.  
이미지가 있다면 해당 이미지를 다운받아 가공하여 이미지 안의 글자를 텍스트 형태로 반환합니다.  
페이지 소스에서 분석이 완료된 이미지 element를 지워 그 자리에 반환된 텍스트를 넣습니다.

- Downloading images
![Failed to load](/Document/img_src_query1.png)
![Failed to load](/Document/img_src_query2.png)
- Changed web's 
![Failed to load](/Document/changed_web.png)

-----

## Result
잘 학습시켰음에도 학습된 데이터의 양이 너무 적은지, PPT에서 폰트로 글자를 찍어내면 잘 인식하지만 일반 웹상의 글자를 인식하지는 못한다.  
글자 `이코노미스트`를 넣은 결과로 `디크그디그크` 처럼 모양을 다르게 하거나 소위 '야민정음' 처럼 한 두 획을 제하거나 더해야 나오는 모양의 글자로 인식이 되었다.  
과적합은 아닌 것으로 보이는 것이, 10에포크만을 돌렸고 대략 8에포크 정도의 결과를 썼기 때문에 단순 데이터의 양과 종류가 부족했던 것으로 생각된다.  
또한 Image Preprocessing -> Text Detection -> Text Recognizing 순으로 절차를 밟아야 하지만 Text Detection에 대한 이해가 너무 부족해 구현하지 못했다는 한계가 있다.  
추후 더욱 많은 데이터셋을 학습시키고 Text Detection 기능을 추가한 뒤 폰트 속성을 약간 조정한다면 웹 번역을 서포트 할 수 있는 좋은 기능이 될 것이라 생각한다.
