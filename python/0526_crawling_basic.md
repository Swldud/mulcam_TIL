# Web crawling (웹 크롤링)

## parsing(파싱)
  : 받아온 데이터(html 문서)에서 필요한 데이터를 추출하는 것
    => BeautifulSoup 사용

## Beutifulsoup

- method
    - find(태그이름, [{속성이름: 속성값}])
<br>
    : 태그 중 첫번째 태그만 추출
<br>
<br>

    - findAll / find_all(태그이름, [{속성이름: 속성값}])
<br>
    : 지정한 태그 모두를 찾아서 추출, list 형태로 반환됨.
<br>
<br>
    - select() 
    : 여러 개의 태그 추출 (하나만 추출할 때는 select_one())
<br>
    find와 기본적인 기능은 같음.
        - method
            - .클래스명 : 클래스 선택자
                - 같은 값을 클래스는 여러개 있을 수 있음
            - #id 명 : id 선택자
                - 같은 id 값을 갖고 있는 태그는 유일
                - 문서내에서 유일한 태그 선택 시 사용
            - 띄어쓰기 선택 : 자식 선택
                - div li : div태그내의 모든 자식 li
            - \> 선택 : 자식 선택
                - div > li : div태그내의 자식 태그 li
<br>
<br>

            - 시작하는 : ^
            - 끝나는 : $
            - 일치하는 : =
            - 모든 : *
<br>
<br>
    - next_sibling
<br>
    : 같은 태그의 바로 다음 태그를 보여줌. (줄 바꿈한 경우 \n 도 형제로 인식하여 추출함)




### 0. import
```py
# print 명령문 없이 여러 값을 한 번에 출력시킬 때 쓰는 코드
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"

# 웹페이지를 열어보기 위해 사용되는 모듈
from urllib.request import urlopen

# Beutifulsoup
#!pip install bs4
import bs4

```

### 1. 소스코드 얻어오기 = parsing

```py
url = "원하는 사이트 url"
html = urlopen(url)
text = html.read()  # text를 확인했을 때, 한글이 깨진다면 text.decode('utf8') 추가 실행

# parsing한 객체를 가져오기 (beutifulsoup)
변수명 = bs4.BeautifulSoup(html, 'html.parser')  # 'html.parser' 은 beautifulsoup에게 html을 분것라하고 알려주는 것. (파이썬의 내장 클래스임.)
```

### 2. 추출하기

```py
변수명.find('추출하고 싶은 태그이름')  # 추출하고자 하는 태그의 첫번째 태그만 반환
변수명.findAll('추출하고 싶은 태그이름')  # 추출하고자 하는 태그에 해당되는 태그 전부 반환

# 태그의 텍스트 반환
변수명.find('추출하고 싶은 태그이름').text

# findAll()로 반한된 리스트 내에서 특정 원소의 텍스트 출력
변수명.findAll('태그이름')[숫자].text

# findAll의 모든 텍스트를 추출하기 위해서는 for문을 사용해야 함

변수명2 = 변수명.findAll('태그이름')
for i in 변수명2:
    print(i.text)

# lis = ul.findAll('li')
# for li in lis:
#     print(li.text)

# '\n'(특정적으로 반복되는 문자)을 기준으로 자르기
변수명.text.split('\n')
```

- 특정 속성을 갖고 있는 태그 추출 
```py
# html
html_str = """
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""

bs_obj = bs4.BeautifulSoup(html_str, 'html.parser')

# 태그 중에 특정 속성을 갖고 있는 첫번째 태그를 추출
bs_obj.find('ul', {'class':'greet'})

# [] <ul class="greet">
#    <li>hello</li>
#    <li>bye</li>
#    <li>welcome</li>
#    </ul>

# class 속성값이 greet인 ul 태그 내의 모든 li의 텍스트값 추출
# 메소드 체인 방식 가능 : find().find()
lis = bs_obj.find('ul', {'class': 'greet'}).findAll('li')

for li in lis:
    print(li.text)

# [] hello
#    bye
#    welcome

```

- 태그 안에서 특정 속성명의 태그 추출
```py
bs_obj.find('ul')['class']

# 얘 역시 findAll로 찾기XXX
```

- 태그 안의 태그에 포함되는 것 텍스트 전부 추출
```py
html_str = """
<html>
    <body>
        <ul class="ko">
            <li><a href="https://www.naver.com/">네이버</a></li>
            <li><a href="https://www.daum.net/">다음</a></li>
        </ul>
        <ul class="sns">
            <li><a href="https://www.goole.com/">구글</a></li>
            <li><a href="https://www.facebook.net/">페이스북</a></li>
        </ul>
    </body>
</html>
"""

a_list = bs_obj.findAll('a')
a_list

# [] [<a href="https://www.naver.com/">네이버</a>,
#     <a href="https://www.daum.net/">다음</a>,
#     <a href="https://www.goole.com/">구글</a>,
#     <a href="https://www.facebook.net/">페이스북</a>]

for a in a_list:
    print(a['href'])  # class a 안에 있는 href 태그의 내용물을 꺼내오라는 명령

# [] https://www.naver.com/
#    https://www.daum.net/
#    https://www.goole.com/
#    https://www.facebook.net/
```

- select() vs find()
```py

# id가 mainMenuBox인 <div>태그 추출
bs_1.find('div', {'id':'mainMenuBox'})
bs_1.select('#mainMenuBox')


# id가 mainMenuBox인 <diV>태그 내 모든 <li>태그 추출
bs_1.find('div', {'id':'mainMenuBox'}).findAll('li')
bs_1.select('#mainMenuBox li')


# 클래스가 box인 태그 내에 들어있는 모든 <a>태그를 추출
bs_1.select('.box a')

bs_2 = bs_1.findAll('div', {'class':'box'}) ; bs_2
for i in bs_2:
    print(i.findAll('a'))


# id가 fashion인 태그의 텍스트 추출 
bs_1.select_one('#fashion').text
bs_1.find('a', {'id':'fashion'}).text

# box 클래스(<div class="box">)의 첫번째 div 태그의 택스트 추출

bs_1.select('.box div')[0].text
bs_1.findAll('div', {'class':'box'})[0].find('div').text


```

- 특정 자식 태그 추출하기
```py
# <ul> 태그의 자식 태그들 중 style 속성의 값이 green으로 끝나는 태그의 컨텐츠
bs_obj.select('ul > *[style$=green]')[0].text  # style 중 green으로 끝나는 모든 자식태그를 가져오기
bs_obj.select('ul > li[style$=green]')[0].text
bs_obj.select('ul > li')[2].text
bs_obj.select('ul [style]')[2].text

obj.findAll('li')[2].text
```

- 모든 자식 태그의 text 추출하기
```py
# <ol> 태그의 모든(*) 자식 태그들의 컨텐츠 

# 1번 방법
for ol in bs_obj.select('ol *'):  # 띄어쓰기 선택 : 자식 선택
    print(ol.text)
    
# 2번 방법
for t in bs_obj.select('ol > *'):  # > : 자식 선택
    print(t.text)

# findAll
for i in obj.findAll('ol'):
    print(i.text)

```

- 자식 태그 찾을 때 ' *' 유무의 차이
```py
# find
obj.select('table')

# [] [<table border="1">
#    <tr class="name"><th>둘리</th><th>또치</th><th>도우너</th></tr>
#   <tr><td>케라토사우루스</td><td>타조</td><td>외계인</td></tr>
#   <tr><td>도봉구 쌍문동</td><td id="target">아프리카</td><td>깐따삐아 별</td></tr>
#   </table>]

# select
bs_obj.select('table *') 

# [] [<tr class="name"><th>둘리</th><th>또치</th><th>도우너</th></tr>,
#     <th>둘리</th>,
#     <th>또치</th>,
#     <th>도우너</th>,
#     <tr><td>케라토사우루스</td><td>타조</td><td>외계인</td></tr>,
#     <td>케라토사우루스</td>,
#     <td>타조</td>,
#     <td>외계인</td>,
#     <tr><td>도봉구 쌍문동</td><td id="target">아프리카</td><td>깐따삐아 별</td></tr>,
#     <td>도봉구 쌍문동</td>,
#     <td id="target">아프리카</td>,
#     <td>깐따삐아 별</td>]

```
