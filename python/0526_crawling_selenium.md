# Selenium : 동적 페이지 크롤링

## 정적 페이지와 동적 페이지
- 정적 페이지
    - 항상 같은 내용을 보여주는 웹페이지
    - 정적 웹페이지 방식은 글 자체가 전부 html 단위의 파일들로 이루어져 있음
    - 단순히 사이트 관리자가 미리 만들어놓은 웹페이지만 볼 수 있음
    - 새 글을 쓰거나 수정할 때, 글을 다운로드 받아 편집하고 업로드까지 수동으로 진행

- 동적 페이지
    - 사용자의 인터랙션에 따라 바뀌는 웹페이지
    - 데이터베이스(DB, Database)를 활용
    - 사용자가 글을 작성하거나 블로그 설정 등을 바꾸면 그 내용이 서버에 있는 DB에 저장이 되고 그 결과가 웹페이지에 반영이 되는 형태로 동작
    - 웹 브라우저 상에서 새 글 작성도 할 수 있고, 통계나 다양한 위젯 등 화려한 기능들을 많이 제공


## method

- 드라이버 객체 생성    
  : selenium은 웹 브라우저를 컨트롤하는 기능이기 때문에 webdriver 프로그램을 사용해야 한다
    - chrome_options = webdriver.ChromeOptions()
    - driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

- 조건문
    - driver.find_element(By.CLASS_NAME, "information")
    - driver.find_element(By.CSS_SELECTOR, "#fname")
    - driver.find_element(By.ID, "lname")
    - driver.find_element(By.LINK_TEXT, "Selenium Official Page")
    - driver.find_element(By.NAME, "newsletter")
    - driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page")
    - driver.find_element(By.TAG_NAME, "a")
    - driver.find_element(By.XPATH, "//input[@value='f']")  
      (x path: html 문서에서 element의 경로 | 개발자 도구 > element 선택 > 우클 > copy > copy xPath)


##  selenium을 통한 데이터 추출

1. webdriver 객체 생성  

```py
import pandas as pd
import numpy as np
from urllib.request import urlopen # 서버 요청/응답 패키지
import bs4 
from bs4 import BeautifulSoup

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By # 셀레니움 4.0부터 포함된 객체(모듈)

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)  # 비어있는 chrome 새창이 열림

```

2. 페이지 접속
```py
driver.get('url 주소 넣기')  # 위에서 열렸던 새 창에 url 화면이 뜸

```

3. driver method를 이용하여 데이터 추출

- 예시: <span class="u_likeit_text _count num">
```py
element = driver.find_element(By.CSS_SELECTOR, ".u_likeit_text._count.num") # 클래스 선택자는 맨 앞에 . 으로 시작 , id 선택자는 맨 앞에 # 등 기본적인 크롤링 명령어와 같음
                                                                            # 단, 띄어쓰기가 되어있는 곳은 . 을 사용하여 붙임
```

4. 자동화를 위한 함수 작성
```py
# 비어있는 datafarme 생성
naver_webtoon_df_final = pd.DataFrame({
    'title': [],
    'author': [],
    'rating': [],
    'view': [],
})

def get_page_webtoon(url):
    driver.get(url)  # 크롤링의 대상이 될 url을 받아옴.
    time.sleep(2)  # 크롤링 하는 동안 페이지가 갱신되는 것을 막기 위해 time 모듈 사용
    
    df = pd.DataFrame({
        'title': [],
        'author': [],
        'rating': [],
        'view': [],
    })
    
    boxes = driver.find_elements(By.CSS_SELECTOR, '.ChallengeListItem__info_area--hnJTz')
    
    for box in boxes:
        title = box.find_element(By.CSS_SELECTOR, '.ContentTitle__title--e3qXt').text
        author = box.find_element(By.CSS_SELECTOR, '.ContentAuthor__author--CTAAP').text
        rating = box.find_element(By.CSS_SELECTOR, '.Rating__star_area--dFzsb').text.split('\n')[1]
        view = box.find_element(By.CSS_SELECTOR, '.Rating__view_area--GQb_S').text.split('\n')[1]

        webtoon = pd.DataFrame({
            'title': title,
            'author': author,
            'rating': rating,
            'view': view,
        }, index=range(1))
        
        df = pd.concat([df, webtoon], ignore_index=True)

    return df

    # 추출하고자 하는 페이지 수를 정해서 넣기
    for page in range(1, 21):
    url = base_url + str(page)
    print(url)
    
    page_webtoon = get_page_webtoon(url)
    
    naver_webtoon_df_final = pd.concat([naver_webtoon_df_final, page_webtoon], ignore_index=True)  # concat() 사용 유의

```


## 추가적인 내용
- 지정된 파일의 특정 문자열을 포함하는 파일들을 리스트로 변환 
```py
from glob import glob
import os

files = sorted(glob('crawl_data/지역_위치별*.xls'), key=os.path.getctime, reverse= True)  # 파일 저장 시간 순으로 정렬
```

- 특정 열에 특정 값이 들어있는 행 제거
```py
# 가격 대신 '-' 들어 잇는 주유소 제거
station_df = station_df[station_df['가격'] != '-']
station_df[station_df.가격 == '-']
```