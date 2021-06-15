# KoreanOCR-for-Web
AI_OCR for enhancement of accessibility about web's image resources.
---

[Sources]
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
![Failed to load](/Model-Structure.png)
- WebController.py - `Selenium`을 이용하는 웹 접근용 파일
