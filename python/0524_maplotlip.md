# 시각화 패키지

## Matplotlip
- 파이썬 표준 시각화 도구 
- matplotlib: import matplotlib as **mpl**
- pyplot: import matplotlib.pyplot as **plt**
  <br>
  (단, jupyter notebook에서 시각화를 표시하려면,  
   매직 명령어 %matplotlib inline 을 실행해야 함.)

- method
    - 라인 플롯 (line plot) (선 그래프) : plot()
    - 바 차트 (bar chart) (막대 그래프) : bar()
    - 스캐터 플롯 (scatter plot) (선점도) : scatter()
    - 히스토그램 (histogram) : hist()
    - 박스 플롯 (box plot) : boxplot()
    - 파이 차트 (pie chart) : pie()
    - 기타 다양한 유형의 플롯 지원

<br>

- 매직 명령어
```py
import matplotlib.pyplot as plt
%matplotlib inline
```

### 1. plot() : 선 그래프

- method
    - figure(figsize=(가로크기,세로크기)) : 그래프 크기 설정
    - title() : 제목 출력
    - xlim(범위값): x 축 범위
    - ylim(범위값) : y 축 범위
    - xticks() / yticks() : x / y 축의 눈금 표시 기준 
    <br>
    (지정하지 않으면 x,y값의 범위 내에서 그려짐)
    - legend() : 범례
    - xlabel() : x축라벨(값)
    - ylabel() : y축라벨(값)
    - grid() : 그래프 배경으로 grid 사용 결정 함수

- style
    - color : c (선색상)
    - linewidth : lw (선 굵기)
    - linestyle : ls 
      <br>
      (solid, dashed, dotted, dashdot)
    - marker : 마커 종류
    <br>
      (+, o, *. . , x, s, d, ^, v, >, <, p, h)
    - markersize : ms (마커크기)
    - markerfacecolor : mfc (마커 내부 색상)
    - markeredgecolor : mec (마커 테두리 색상)
    - markeredgewidth : mew (마커 테두리 굵기)

```py
plt.plot([10,20,30,40], [1,4,9,16],
        c= 'b', lw = 5, ls = '--', marker = 'o', ms=15, mec = 'g', mew = 5, mfc='r')
plt.xlim(0, 50)  # x 축 범위 지정
plt.ylim(-10, 30)  # y 축 범위 지정
plt.xticks(x, ("10대","20대","30대","40대","50대","60대")) # x축의 눈금 지정 x의 값이지만, 뒤에 작성한 튜플 or 리스트 안의 내용으로 보여짐
plt.title('그래프 제목', loc='left', pad = 30, fontsize= 30)  # loc를 통해 위치 설정 가능 (loc= 'right'|'left'| 'center') 
                                                             # pad를 통해 그래프와 제목 사이의 간격 설정
                                                             # fontsize를 통해 제목 폰트 크기 설정
plt.xlabel('x축 제목')
plt.ylabel('y축 제목')
```

<br>

- 화면분할
  : 하나의 화면에 여러 개의 그래프를 생성하는데, 이때 그리드 형태로 위치와 순서를 지정한다
    - subplot(인수1, 인수2, 인수3) 
    - subplot(인수1인수2인수3)  : 쉼표 생략이 가능함
    - tight_layout(pad=) : 플롯간 간격을 설정

```py
plt.subplot(221)
plt.subplot(222) 
plt.subplot(223) 
plt.subplot(224) 
plt.tight_layout()  # 자동 간격 설정
```

<br>

- legend(): 범례 표시 
    - plt.legend(loc=, ncol= )  
    - loc = (x,y) : 범례표시 위치 값
    - ncol= 열의 개수
    - 범례를 표시하기 위해서는 plot에 label 속성이 추가되어 있어야 함
        - plt.plot(x,y,label='a')

```py
x = [2005,2010,2015,2020]
y1 = [2,12,7,10]
y2 = [5,7,12,20]

plt.plot(x, y1, label="모니터")
plt.plot(x, y2, label="노트북")
plt.xlabel("연도")
plt.ylabel("판매수량")

plt.legend(loc="best", ncol=2)
plt.show()
```

### 2. 막대 그래프 
 - method

    - 세로 막대 그래프 그리기: bar()
        - bar(x,y,color=[],alpha=)

        <br>

    - 가로 막대 그래프 그리기
        - barh(y,x,color=[], alpha=)
        <br>
        <br>
    - color = [] : 색상값 설정
    - alpha = 투명도 설정
    - plt.text(가로 위치, 세로 위치, 문구, fontsize=, color= )
    - plt.plot([0,1],[2,3], color=, linestyle=, marker=) : 선 추가
      
<br>      

#### 데이터 프레임으로 막대 그래프 그리기
- plot() 이용
    - 수직 바 차트 : df.plot(kind='bar')
    - 수평 바 차트 : df.plot(kind='barh')
    - legend 자동 추가됨
- bar() 이용
    - bar(df.열1, df.열2, ..)

```py
df1 = pd.DataFrame({
    '나이':[15, 20, 17, 50, 2, 30, 23],
    '이름':['둘리', '도우너', '또치', '길동', '희동', '마이콜', '영희']},
    columns = ['나이', '이름'])

df1.plot(kind = 'bar', grid = True, figsize = (5,5))  # 수직 막대 그래프, 그리드 여부, 그래프 사이즈
```

- 열이 여러 개인 데이터프레임의 막대 그래프 그리기
```py
df2 = pd.DataFrame({
    '나이':[15,20,17,50,2,30,23],
    '키' : [165,150,151,175,80,175,185],
    '이름':['둘리','도우너','또치','길동','희동','마이클','영희']
},columns=['나이','키','이름']) ; df2

x=[0,1,2,3,4,5,6]  # xticks 위치 표시에 사용할 변수

df2.plot(kind='bar', grid=True, figsize=(5,5))  # 기본적으로 df2의 막대 그래프를 그릴 거임
plt.xticks(x, df1.이름, rotation='horizontal')  # x 축으로 쓸 열을 선택
                                                # rotation은 x 축 이름이 너무 길때, 각도를 비스듬히 하려고 있는 거임
plt.show()
```
<br>

- 데이터프레임으로 수평 바 차트 그리기
```py
# '나이' 기준으로 오름차순 정렬
x = [0, 1, 2, 3, 4, 5, 6]
df2.sort_values(by='나이', ascending=False).plot(kind='barh', grid=True, figsize=(5,5))
plt.yticks(x, df1.sort_values(by='나이', ascending=False).이름)
plt.show()
```

- 특정 열 선택헤서 바 차트 그리기1

- df1

||나이|몸무게|키|성별|주소|
|---|---|---|---|---|---|
|홍길동|22|60.1|170.5|남|서울|
...


```py
x = (0, 20, 40, 60, 80)

df1.sort_values(by='몸무게', ascending=True).몸무게.plot(kind = 'barh',grid=True, figsize = (5,5))
plt.xticks(x, [f'{i}kg' for i in x])  # X축 표시 바꾸기 

# 요소를 하나만 넣어도 작동한 이유는, 이름이 열이 아니라 인덱스로 지정되어있기 때문이다.
# 요소를 하나만 넣으면 인덱스가 자동적으로 x 혹은 y 값으로 들어가서 작동한다.
```

- 특정 열 선택해서 바 차트 그리기2

- df2

||기간|자치구|세대|계|남자|여자|...|65세이상고령자|
|---|---|---|---|---|---|---|---|---|
|0|2017.1/4|종로구|72654|162820|79675|83145|...|25425|


```py
df2_1 = pop[['자치구', '65세이상고령자']][1:].set_index('자치구')  # 아예 원하는 열 두 개를 뽑아서 새로운 DF를 만들기
                                                                 # set_index 설정을 안 한다면, 어떻게 해야되는지는 모르겠우ㅠ
df2_1.plot(kind='bar')

```

<br>
- 데이터 프레임으로 선 그래프 그리기

```py
df2.plot()

# 데이터프레임 특정 열만 선택하여 라인 플롯 그리기
plt.plot(df2.나이)

```

- scatter plot() : 산점도 그리기

```py
x = [0, 1, 2, 3, 4]
y = [9, 8, 7, 9, 8]

labels = ["L1", "L2", "L3", "L4", "L5"]

plt.figure(figsize =  (6,4))
plt.scatter(x,y)

# 산점도 점에 라벨 추가 : plt.annotate(출력할 텍스트, (x위치, y위치))
for i, label in enumerate(labels):
    plt.annotate(label, (x[i], y[i]))

plt.colorbar()  # 점에 색깔 넣기

``` 

- 버블차트 그리기

```py

N = 30
np.random.seed(0)
x = np.random.rand(N) # 0 < x < 1 사이의 실수 랜덤 생성
y = np.random.rand(N)
y2 = np.random.rand(N)  # 색상에 적용할 값
y3 = np.pi * (15 * np.random.rand(N)) ** 2  # 크기에 적용할 ㄱ값

plt.title = '버블 차트'
plt.scatter(x, y, c= y2, s=y3)

```

- 히스토그램 그리기

```py
np.random.seed(0)
x = np.random.randn(1000)

plt.title('히스토그램')
plt.hist(x)
plt.show()
```

- boxplot() : boxplot 그리기

```py

s1 = np.random.normal(loc=0, scale=1, size=1000)
s2 = np.random.normal(loc=5, scale=0.5, size=1000)
s3 = np.random.normal(loc=10, scale=2, size=1000)

plt.plot(s1, label = 's1')
plt.plot(s2, label = 's2')
plt.plot(s3, label = 's3')

plt.boxplot([s1, s2, s3])
plt.style.use('default') # default, ggplot, classic, dark_background, seaborn

```

- pie() : 원 그래프 그리기

```py
labels = ['토끼', '고양이', '개', '거북이']
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# explode = (0, 0, 0, 0)
explode = (0, 0, 0.05, 0) # 개 

plt.figure(figsize=(6,4))
# plt.title('파이 차트')
plt.pie(sizes, labels=labels, colors=colors, shadow=True,
       autopct='%.1f%%', startangle=90, explode=explode)  # autopct = '% 표시', strangle은 순서? 인듯, explode는 차트를 쪼개는가의 여부

plt.axis('off') # 축 스케일 : equal, off, auto

plt.show()
```



## 추가적인 내용
### 한글 문제
### matplotlib의 기본 폰트에서 한글이 지원되지 않기 때문에 폰트 변경 필요
```py
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':  # 맥OS 
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':  # 윈도우
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system...  sorry~~~')
```