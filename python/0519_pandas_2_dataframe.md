## 1. Pandas

### DataFrame

 - 열 이름은 index = 으로 생성
 - 행 이름은 columns = 으로 생성 
 - df = pd.DataFrame(data, index = index, columns = columns)

#### list로 dataframe 만들기

```py
df= pd.DataFrame([['a', 'b', 'c'],
                ['a', 'a', 'g'],
                ['a', 'i', 'j']]),
                columns=['a', 'b', 'c'],  # 열이름
                index=[1, 2, 3])  # 행이름

df

```

#### 결측치 확인
- .isna()

<br>

#### 데이터프레임 속성 파악
- shape 속성 (row, column)  # 얘는 numpy에서 쓰임 = array, 배열 상태에 있을 때 사용 가능
- describe() 함수 - 숫자형 데이터의 통계 정보 출력  # r의 summary와 같은 기능
- info() 함수 - 데이터 타입, Non-Null Count 출력  # 결측값 여부 & 데이터 타입 확인

<br>

#### 데이터프레임의 전치 (행/열 바꾸기)
- R의 t() 함수와 같은 기능
- ***원본 데이터에 영향을 주지 않기 때문에, 할당해주어야 함.***
- df.T 
- df.transpose()

<br>

#### loc

- loc는 인덱스 이름을 기준으로 탐색하는 인덱서이다.
- 일반 인덱스가 열을 기준으로 한다면, loc는 **행**을 기준으로 작동한다.
- 문자 인덱스가 있는 상태에서 기본적인 숫자 인덱스를 사용하려 하면 오류 남!

```py
df5['국가'] = '대한민국'  # 얘는 열에 국가 추가하고 행에 주르륵 대한민국 추가됨.
df5.loc['국가'] = '대한민국'  # 얘는 행에 국가 추가하고 열에 주르륵 대한민국 추가됨.
```
<br>

#### iloc

- iloc는 정수형의 위치를 기준으로 탐색하는 인덱서이다.
- 기본형이 **열**을 기준으로 **숫자**로 작동하고, loc가 인덱스의 **행**을 기준으로 **이름**으로 작동한다면,
  <br>
  iloc는 **행**을 기준으로 **숫자**로 작동한다.

<br>

|구분|loc|iloc|
|---|---|---|
|행 불러오기|df.loc['행이름']|df.iloc[행번호]|
|열 불러오기|df.loc[:,'열이름']|df.iloc[:,열번호]|
|행/열 불러오기|df.loc['행이름','열이름']|df.iloc[행번호, 열번호]|
|특정구간 불러오기|df.loc['행이름':'행이름','열이름':'열이름']|df.iloc[행번호:행번호, 열번호:열번호]|

<br>

#### 데이터 추출

- 열 추출
    - loc나 iloc로 열을 추출할 때는 반드시 앞에 슬라이싱을 사용해야 함!
```py 
df['열이름']
df[['열이름']]  # 위에 것과 다르게 dataframe 형태로 출력됨.
                # 문자 인덱스가 있는 상태에서 기본적인 숫자 인덱스를 사용XX

df.loc[:,'열이름']
df.iloc[:,'열번호']

```

- 행 추출
    - 기본형으로 행을 추출할 때는 반드시 슬라이싱을 사용해야 함!
```py
df[:'행이름'] 
df['행이름1':'행이름2']  
df[:'행번호'] 
df['행번호1':'행번호2']

df.loc['행이름']  # loc에 열 이름만 작성하면 오류남
df.loc['행이름1':'행이름2']
df.loc[['행이름1','행이름2']]

df.iloc['행번호']  
df.iloc[['행번호']]  # dataframe 형태로 나오게 하려면 [] 한 번 더 쓰기


```

- 특정값 추출
```py
df['열이름']['행이름']
df.loc['행이름','열이름']


```

- 논리 / 연산으로 행 선택하기 (R의 filter)

```py
df[df.A >15]
df.loc[df.A>15]
```



<br>

#### 데이터 추가

- 열 추가
```py
df[] = ''
```
- 행 추가
```py
df.loc[] = ''
```

#### 데이터 삭제

- axis=0 (default)은 행을 의미, axis=1은 열을 의미

- 행 삭제
```py
df5.drop('광주',axis=0, inplace = True)  # inplace는 원본데이터에 적용할지 여부. False가 기본
df5.drop(['서울','대구'], axis=0, inplace =True)  # 여러 개 삭제 시, 리스트로 만들어서!
df5.drop(df5.index[1:3], inplace=True, axis = 0)  # 여러 개 삭제 시, 슬라이싱 사용도 가능
```

- 열 삭제
```py
df5.drop('2015', axis=1, inplace =True)
df5.drop(['2015','2010'], axis=1, inplace =True)
df5.drop(df5.index[1:3], inplace=True, axis = 1)

del df5['2015']
```

#### 데이터 갱신 (변경)

- 특정 값을 변경하기 위해서는 행과 열을 지정하여 지목한 다음에 대체할 값을 쓰면 됨!

```py
df5['2005']['대구'] = 2500000
```



<br>
<br>

## 추가적인 내용

### csv / excel 파일 열기

#### read_csv() / read_excel() 함수의 주요 파라미터
- sep : 각 데이터 값을 구별하기 위한 구분자(separator) 설정
- header : 헤더(제목) 위치. header를 작성하지 않으면 첫 행이 헤더가 되고, header = None으로 입력하면 숫자로 입력됨. 
- skiprows : 제외하는 행 지정
- thousands : 천 단위 구분 표시 제거
- **index_col : index로 사용할 열 설정**
- **usecols : 선택 열 지정**
- encoding : 인코딩 설정 
    (utf-8f로 저장된 파일은 encodin='utf-8'
     euc-kr로 저장된 파일은 encodin='euc-kr'로 해야 오류 없음)

```py
df_train2 = pd.read_csv('data/train.csv',
                        usecols= ['PassengerId','Survived','Name','Sex','Age'],  # 열 이름 짓기
                        index_col = 'PassengerId')  # index로 사용할 열
```

