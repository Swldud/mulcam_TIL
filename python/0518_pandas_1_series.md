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
