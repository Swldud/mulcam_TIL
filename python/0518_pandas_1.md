# 파이썬 분석 라이브러리

- NumPy (넘파이) : 배열, 행렬 관련 편리한 기능 제공
<br>
   (import numpy as np)
  <br>
  <br>
- Pandas (판다스) : Series, DataFrame 등의 자료구조를 활용한 데이터 분석 기능 제공
   <br>
    (import pandas as pd)
   <br>
   <br>
- Matplotlib (맷플롯립) : 데이터 분석 결과를 시각화하는데 유용한 기능 제공

<br>

## 1. Pandas
- 서로 다른 여러 가지 유형의 데이터를 공통된 포맷으로 정리하기 위해 사용.

### series
- pandas의 기본 객체 중 하나로, 1차원 array, key:value 형태로 구성되어있음. 
  (dictionary와 구조가 비슷해서 dictionary를 series로 변환이 가능함)

#### 리스트로 series 생성하기

```py
s = pd.Series([1,2,3])
```
- 리스트 내에 서로 다른 타입의 데이터가 있으면 형변환이 발생
  ( 문자 + 숫자 = 문자  | 정수 + 실수 = 실수 | NA 값이 있으면 실수로 인식)


#### 인덱스 이름 붙이기
```py
s = pd.Series([1,2,3], index = ['홍갈동', '이몽룡', '성춘향'])
```

#### 시리즈에 이름 붙이기

```py
s.name = '성적'
s.index.name = '성명'  # 인덱스들의 이름 즉, 행의 열이름
```

#### 튜플로 series 생성하기

```py
s2 = pd.Series((1.0,2.0,3.0))
```
- 위에서 작성한 것과 다르게 [] 대신 ()를 씀 = 리스트가 아님 = 튜플 형태로 생성
- tuple: 변경불가능한(immutable) 순서가 있음

#### dictionary로 series 생성하기
```py
city = pd.Series(city = {'서울':9631482,'부산':3393191,'인천':2632035,'대전':1490158})
```

#### range와 arrange 함수 사용
```py
s = pd.Series(range(5)) ;s
v = pd.Series(np.arange(8)) ;v 
```

#### 결측치 작성
 - np.nan으로 작성해야 결측치로 읽힘.
 - pandas는 None


#### series 데이터 추사/수정/삭제

- 데이터 추가/수정
```py
s['행이름'] = 70
```

- 데이터 삭제
```py
del s['행이름']
```

#### series의 인덱스
```py
s[0], s[1]
s['행이름']
```
- 두 개 이상의 인덱싱 코드를 나열하면 튜플 형태로 출력

#### slicing (슬라이싱)
```py
series[start:end]
s[1:4]
s[['경기','전주','세종']]
```

#### 연산

```py
s3 % 2 == 0  # 논리형으로 출력
s3[s3 % 2 == 0 ]  # 계산값 출력
```
```py
(s3[s3 >= 7]).sum() 
sum(s3[s3 >= 7])
```
- Q. 처음에 배울 때는 괄호 안에 넣어서 썼는데, 왜 점을 써서 밖으로 빼는지 잘 모르겠다. 헷갈려@ㅁ@


#### in / items / for / if (dictionary에서 쓰는 연산자라면 OK)

```py
# in 연산자
1 in num_s2
'대전' not in s_city

# items()
list(s_city.items())

# for
for key in s_city.keys():
    print(key)    

for v in s_city.values:
    print(v)

# if
    if '과학' in s2:
    print('데이터에 과학 정보가 있습니다.')
else:
    print('데이터에 과학 정보가 없습니다.')


```

#### series 관련 함수

     - size 속성 : 원소 개수 반환  
     - shape 속성 : 튜플형태로 shape반환  
     - len() : 길이 (원소 개수 반환)
     - unique() : 유일한 값만 ndarray로 반환  
     - count() : NaN을 제외한 개수를 반환  
     - mean(): NaN을 제외한 평균  
     - value_counts() : NaN을 제외하고 각 값들의 빈도를 반환


#### series 날짜 생성 (pandas 패키지)

    - pd.date_range(start, end, periods, freq) 
    - 날짜 자동 생성  
    - 지정된 범위 내의 인덱스 생성  
    - start : (필수) 시작 날짜  
    - end : 종료 날짜  
    - periods : 기간 (end 또는 periods 둘 중의 하나 필수)  
    - freq : 간격 (D(Day)가 디폴트)

    freq 인수
        s: 초  
        T: 분  
        H: 시간  
        D: 일(day)  
        B: 비즈니스 데이 (평일)  
        BH : 비즈니스 시간 (업무시간 기준 09:00:00 ... 16:00:00)
        W: 주(일요일)  
        W-MON: 주(월요일)  
        M: 월말 (월 마지막일)  
        MS: 월 시작일  
        BM: 평일 중에서 월말  
        BMS: 평일 중에서 월 시작일  
        Q : 분기별 마지막 날  
        BQS : 비즈니스 데이 분기 시작일   
        A : 연도 마지막 날  
        AS : 연도 시작일

```py
pd.date_range(start='2023-05-01', end='2023-05-20', freq ='D')
pd.date_range(start='2023-05-01', periods=4, freq='w')
```

### dataframe
 - 열 이름은 index = 으로 생성
 - 행 이름은 columns = 으로 생성 

#### 데이터 프레임 생성
```py
data = [
    [22, 60.1, 170.5, '남', '서울'],
    [45, 51.3, 160.5, '여', '부산'],
    [23, 88.1, 175.5, '남', '대구'],
    [33, 60.1, 180.5, '남', '제주'],
    [40, 60.1, 173.5, '남', '강릉']    
]

columns = ['나이', '몸무게', '키', '성별', '주소']
index = ['홍길동', '성춘향', '이몽룡', '변학도', '강길동']

df3 = pd.DataFrame(data, index = index, columns = columns)
```

#### 결측치 개수 세기
```py
df2.isna()
```

#### 데이터 프레임에서 특정 행/열 추출

```py

df3.index
df3.columns  # 열 이름 확인
df3['나이']  # 열 하나만
df3[['나이','주소']]  # 여러개의 열

```

#### 시리즈로 데이터프레임 생성
```py
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'd'])
s3 = pd.Series([100, 200, 300], index=['a', 'b', 'e'])

pd.DataFrame([s1,s2,s3], index=[1,2,3])
```

#### Excel, csv 파일 불러오기

```py
!pip install openpyxl

df_pop3 = pd.read_excel('data/population_in_Seoul.xlsx', 
                        header=2,  # 열 이름이 있는 행번호
                        usecols=['자치구', '세대','세대당인구','65세이상고령자'])  # 열선택

df_pop3.info()  # 데이터프레임의 정보 확인
```

#### 데이터 프레임 전치
- 전치: 행과 열을 바꾸는 기능
- df.T 
- df.transpose()

#### 파생변수 만들기 (열 추가)

```py
df5 = df4.copy()  # 원본이 변하지 않도록 얕은 복사
df5['2010-2015 증가율'] = df5['2010-2015 증가율'] *100  # 파생변수 생성
del df5['2010-2015 증가율']  # 파생변수 삭제
```

- 파생변수, 즉 열을 추가 할 때 리스트를 통해 각 행의 값을 다르게 추가 할 수 있음
- 한 개의 값만 지정하면 모든 행에 동일한 값으로 추가됨.

#### 행 추가 (loc 인덱스 사용) / 삭제 (drop 사용) / 변경

```py
df5.loc['광주'] = ['호남권',2470000,2456000,2453000,2460000,1.00]
df5

df5.drop('광주',axis=0, inplace = True)  # axis = 0이면 행을 의미, 1이상은 열을 의미
                                         # inplace = True 는 결과를 반영하여 원본데이터가 변경됨을 의미

df5.drop(df5.index[1:3], inplace=True)  # 0-base 행 인덱스 1~2행 삭제
df5.drop(df5.columns[1:3], axis=1, inplace=True) # 0-base 열 인덱스 1~2 삭제

df5['2005']['대구'] = 2500000  # 2005 열의 대구 행의 값을 2500000로 변경함.
```



## 추가적인 내용

### jupyter에서 패키지 설치하기
```jupyter
!pip install numpy
```

### 결측치를 넣을 때
```py
s = pd.Series([0,1,3.0,np.nan])
```

### 모든 값을 출력하기
```py
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"
```
