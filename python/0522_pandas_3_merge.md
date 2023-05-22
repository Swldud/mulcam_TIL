## 1. Pandas

### 데이터 프레임의 병합

#### 1. merge()

- 두 데이터 프레임의 공통 열 / 행을 기준으로 병합
- 공통되는 열 = 이름이 같음 = key

#### 2. join()
- 인덱스 기준으로 병합
- 열을 기준으로 병합하려면 열을 인덱스로 바꿔줘야 함.
- df1.join(df2, on=None, how='left', lsuffix='', rsuffix='', sort=False)

------------------
<br>

```py
pandas.merge(df_left, df_right, how = 'inner')

df1.join(df2, how='inner')
```

- inner join (교집합으로 합치기)
    - 같은 값이 존재하는 행만 병합
```py
df1.merge(df2, how='inner')
pd.merge(df1, df2, how='inner')

df1.join(df2, how='outer')
```
![inner](https://github.com/Swldud/mulcam_TIL/blob/3d4c27342e80b6aed7cd1dceaba4ee1e81d9c67b/python/inner.png?raw=true)

- outer join (합집합으로 합치기)
    - 전부 병합하고, 빈 값은 NaN으로 채워짐.

```py
df1.merge(df2, how='outer')
pd.merge(df1, df2, how='outer')
```

![](https://github.com/Swldud/mulcam_TIL/blob/master/python/outer_join.png?raw=true)


- left / right join (왼/오른쪽 데이터 프레임을 기준으로 병합)

```py
df1.merge(df2, how='left')
pd.merge(df1, df2, how='left')
```
![](https://github.com/Swldud/mulcam_TIL/blob/master/python/left_join.png?raw=true)

```py
df1.merge(df2, how='right')
pd.merge(df1, df2, how='right')
```
![](https://github.com/Swldud/mulcam_TIL/blob/master/python/right_join.png?raw=true)


#### 같은 키 값이 여러 개 있는 경우

|품종|꽃잎길이|
|---|---|
|setosa|1.4|
|setosa|1.3|
|virginica|1.5|
|virginica|1.3|

<br>

|품종|꽃잎 너비|
|---|---|
|setosa|0.4|
|virginica|0.3|
|virginica|0.5|
|ersicolor|0.3|

=>
```py
pd.merge(df1, df2, how = 'inner')
```

|품종|꽃잎길이|꽃잎너비|
|---|---|---|
|setosa|1.4|0.4|
|setosa|1.3|0.4|
|virginica|1.5|0.3|
|virginica|1.5|0.5|
|virginica|1.3|0.3|
|virginica|1.3|0.5|

 - 1번 df에 ersicolor에 대한 데이터가 없기 때문에 자료X
 - virginica에 대한 데이터가 각각 2개 씩 있음 = 2x2 = 4 개의 데이터 생성

<br>

#### 열병합

- 열 병합을 할 때에는 key로 사용할 기준열을 명시해 주어야 한다
- pd.merge(df1, df2, on, how)

```py
pd.merge(df1, df2, on='고객명', how='inner')
```

- key가 되는 기준 열의 이름의 다를 경우, 두 df의 기준열의 명시하여, 두 열이 같은 열임을 나타낼 것.

```py
df1=pd.DataFrame({
    '이름' :['영희','철수','철수'],
    '성적' :[90,80,80]
})

df2 = pd.DataFrame({
    '성명' :['영희','영희','철수'],
    '성적2':[100,80,90]
})


pd.merge(df1, df2, left_on='이름', right_on='성명')
```

=>

|이름|성적|성명|성적2|
|---|---|---|---|
|영희|90|영희|100|
|영희|90|영희|80|
|철수|80|철수|90|
|철수|80|철수|90|


#### 인덱스 기준 열병합
- 사용할 인덱스 명을 명시
- 한 쪽 데이터 프레임의 인덱스만 사용시
```py
pd.merge(df1, df2, left_on=['도시', '연도'], right_index=True)

pd.merge(df1, df2, right_on=['도시', '연도'], left_index=True)
```
<br>

- 양쪽 데이터 프레임의 인덱스를 사용하여 병합

||서울|부산|
|---|---|---|
|a|1|2|
|c|3|4|
|e|5|6|

||대구|광주|
|---|---|---|
|b|7|8|
|c|9|10|
|d|11|12|
|e|13|14|


```py
pd.merge(df1, df2, left_index=True, right_index=True, how='inner')
```
=>
||서울|부산|대구|광주|
|---|---|---|---|---|
|c|3|4|9|10|
|e|5|6|13|14|

```py
pd.merge(df1, df2, left_index=True, right_index=True, how='outer')
```

=> 
||서울|부산|대구|광주|
|---|---|---|---|---|
|a|1|2|||
|b|||7|8|
|c|3|4|9|10|
|d|||11|12|
|e|5|6|13|14|

<br>

- join()으로 열병합


|고객명|날짜|데이터|
|---|---|---|
|춘향|2/1|2000|
|춘향|2/2|3000|
|몽룡|2/3|10000|

|고객명|데이터|
|---|---|
|춘향|여자|
|몽룡|남자|

```py
df1.set_index('고객명').join(df2.set_index('고객명'), on='고객명', lsuffix='_x', rsuffix='_y')
```

=>
|고객명|날짜|데이터_x|데이터_y|
|---|---|---|---|
|춘향|2/1|2000|여자
|춘향|2/2|3000|여자
|몽룡|2/3|10000|남자


#### 3. concat()
    - 기준열 사용X
    - 위/아래 데이터 행 연결  or  옆으로 열 연결
    - 두 시리즈/df 를 연결하기 때문에 인덱스 값이 중복 될 수 있음
    - ignore_index=False : False: 기존 index 유지, True: 기존 index 무시하고 0-base 인덱스 설정

- 단순 행/열 연결
```py
pd.concat([df1, df2], axis=0)
pd.concat([df1, df2], axis=1)
```

- 열이 다른 df의 연결
```py
# 행 연결은 열 이름이 같은 것은 합쳐짐
pd.concat([df1, df2], axis=0) # 행연결 : 기본 합집합 : 전체 연결
pd.concat([df1, df2], axis=0, join='inner') # 교집합 : 공통된 열만 연결
pd.concat([df1, df2], axis=0, join='outer') # 합집합 : 전체 연결

# 열 연결은 열 이름이 같아도 합쳐지지 않고 따로 만들어짐. 같은 이름의 열이 여러 개 존재할 수 있음. 
pd.concat([df1, df2], axis=1) # 행연결 : 기본 합집합 : 전체 연결
pd.concat([df1, df2], axis=1, join='inner') # 교집합 : 공통된 열만 연결
pd.concat([df1, df2], axis=1, join='outer') # 합집합 : 전체 연결
```



- 다중 인덱스 
<br>
   : 인덱스가 중복되는 데이터프레임을 병합할 때, 구분하기 위해서 계층적 인덱스를 사용한다

```py
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'E': ['C4', 'C5', 'C6', 'C7'],
                    'F': ['D4', 'D5', 'D6', 'D7']},
                   index=[0, 1, 2, 3])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'O': ['D8', 'D9', 'D10', 'D11']},
                   index=[1,2,3,4])

df = pd.concat([df1, df2, df3], keys=['x', 'y', 'z']) # 기본 outer 합집합             
```

- 다중 인덱스 원소 접근

```py
# z의 1,2행의 C, O열의 값 추출  : 비연속 열 선택
df.loc['z'].loc[1:2,['C', 'O']] # oc(행, 열) -> 비연속 (값이 여려 개 :[] 사용)

```
- 기존 인덱스를 제거하고 기본 숫자위치 인덱스로 대체 
    <br>
    : (ignore_index = True) 사용
```py
pd.concat([df1, df2, df3], join='inner', ignore_index=True)
```




