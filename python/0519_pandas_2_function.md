## 1. Pandas

### function

- count() : 데이터 개수 반환  
- value_counts() : 데이터 빈도 수 반환  
- sort_index() : 인덱스를 기준으로 정렬  
- sort_values() : 데이터 값을 기준으로 정렬  
- dropna() : NaN 제거  
- fillna() : NaN을 다른 값으로 채움  
- apply() : 동일한 반복 연산에 함수 적용  
- cut() : 데이터 구간 분할  
- qcut() : 경계선 없이 데이터 수가 동일한 구간으로 분할  
- set_index() : 열로 인덱스 설정  
- reset_index() : 인덱스 제거하고 열로 추가  
- rename() : 열/행 인덱스 이름 변경

<br>

#### 1. count() : 데이터 개수 반환  

- 결측치를 포함하지 않고 개수를 반환함.

```py
df.count()
```

- 카테고리 값 세기
<br>

     value_counts() 인수 
        
        - dropna=True 디폴트 (NaN 무시)  
        - dropna=False : NaN 개수도 카운트  
        - ascending=True : 오름차순 정렬 (기본 False로 내림차순)  
        - normalize=True  : 각 값 및 전체에서의 범주형 데이터의 비율을 계산

```py
titanic['alive'].value_counts()  # alive 라는 열의 변수 개수 세기
titanic['alive'].value_counts(normalize=True)  # alive 라는 열의 변수 비율 보기

pd.DataFrame(titanic['alive'].value_counts())  # count를 포함한 데이터 프레임 만들기

titanic.count()  # 전체 열의 개수 세기

titanic['열이름'].value_counts(dropna =False)  # 결측치를 포함하고
titanic['열이름'].value_counts(dropna =True)  # 결측치를 제외하고

titanic['embarked'].value_counts(ascending=True) # 오름차순
titanic['embarked'].value_counts(ascending=True) # 내림차순

```

#### 2. sort() : 정렬함수

- sort_index(ascending=True/False) : 인덱스를 기준으로 정렬
    (ascending 생략하면 오름차순 정렬)
- sort_values(ascending=True/False) : 데이터 값을 기준으로 정렬

```py
df.sort_values(ascending=False)  # 데이터값 기준 내림차순 정렬
df.sort_index(ascending=True)  # 인덱스 기준 오름차순 정렬

df1.sort_values(by=[0, 2], ascending=False)  # 0열과 2열만 내림차순 정렬
```


#### 3. sum() : 행렬 합계

- 각 열의 합계 
```py
df2.sum(axis=0)
df2.sum()
```

- 각 행의 합계
```py
df2.sum(axis=1)
```

#### 4. min() / max() : 최대/최소값 

-  각 열의 최대최소값
```py
df2.min(axis=0)
df2.max(axis=0)

df2[0:4].max()  # 특정 행만 고르기
```

- 각 행의 최대최소값
```py
df2.min(axis=1)
df2.max(axis=1)
```

#### 5. fillna(숫자): 숫자로 결측치 대체

```py
df2.fillna(0)
```

#### 6. apply() : 함수 반복

- apply(반복적용할 함수, axis = 0/1)
- lambda는 반복적용할 함수를 따로 정의하지 않고 한 줄 코딩!

```py
# 각 열의 최대값 - 최소값을 구하기

#1
df3.max(axis=0) - df3.min(axis=0) 

#2
def diff(x):  # x는 시리즈
    return max(x) - min(x)
df3.apply(diff, axis=0)

#3
df3.apply(lambda x : x.max() - x.min(), axis=0)
```

#### 7. map(함수, 리스트/튜플/시리즈) : 리스트, 튜플, 시리즈 등을 지정된 함수로 처리해줌

```py
s = pd.Series([100, 20, 63])  # 시리즈 형태의 무언가

def check(score):
    if score >= 60 :
        result = '합격'
    else:
        result = '불합격'
    return result 

s.map(check)

# [] 0     합격
# [] 1    불합격
# [] 2     합격

```

#### 8. cut(data,bins,labels) : 데이터 범주화 

- data : 구간 나눌 실제 값   
- bins : 구간 경계값  
- labels: 카테고리값  

```py
ages=[0, 0.5, 4, 6, 4, 5, 2,10, 21, 23, 37,15, 38, 31, 61, 20, 41, 31,100]
bins = [0, 4, 18, 35, 50, 65, 100]
labels = ['영유아','미성년자','청년','중년','장년','노년']

ctgs = pd.cut(data, bins,labels=labels)  # cut을 사용하면 Categorical 형태임.
ctg_df = pd.DataFrame({'나이':ages,'연령대':ctgs})  # 데이터 프레임으로 보려면 이렇게

```
#### 9. codes : 범주화 자룔를 숫자로 인코딩

- 결측값은 -1로 치환함
- labels에 작성한 순서대로 0부터 할당

```py
ctgs.codes

# [] rray([-1,  0,  0,  1,  0,  1,  0,  1,  2,  2,  3,  1,  3,  2,  4,  2,  3,  2,  5]
```


#### 10. qcut(data, 구간수, labels=[d1,d2....]) : 일정한 수로 데이터 분할

- 동일한 값이 존재할 경우 구간의 수가 달라질 수 있음.

```py
qctg = pd.qcut(data, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'])  # Q1~Q4의 4구간으로 데이터 분할  
                                                          # 딱 떨어지지 않으면 이상하게 나눠짐 왤까...??
pd.value_counts(qctg)  # 각 구간의 데이터 개수 확인
```


#### 11. set_index() / reset_index()  : 인덱스와 열 간의 전치

- 원본에 바로 반영되지 않기 때문에, replace = True 를 사용해서 반영해야 함

- set_index()
 <br>
        - 기존의 행 인덱스를 제거하고 데이터 열 중에서 하나를 인덱스로 설정  
          (열 -> 인덱스)  
        <br>

- reset_index()  
        - 기존의 행 인덱스를 제거하고 인덱스를 열로 추가  
         (인덱스 -> 열)  


#### 12. rename() : 인덱스 이름 변경

- 행 인덱스 이름 변경  
    - rename(index={현재 index : 새 index}) 

    <br>

- 열 인덱스 이름 변경  
    - rename(columns={현재 index : 새 index}) 

```py
df4.rename(index={0:'1반',1:'2반', 2:'3반', 3:'4반',4:'5반'}, inplace=True)

df4.rename(index={'5반':'6반'}, inplace=True)  # 5반만 6반으로 변경
```

#### 13. for문 

- 기본적인 for문 작성법과 다를 것 X


<br>
<br>

## 추가적인 내용

### 난수 생성

```py
import random

random.random()  # 0~1 사이의 랜덤 실수를 리턴
random.uniform(1, 10)  # 1~10 사이의 랜덤 실수를 리턴
random.randint(1, 10)  # 1~10 사이의 랜덤 정수를 리턴
random.randrange(start, end, step)  # range로 만들어지는 정수 중에 하나를 랜덤하게 리턴
random.choice('abcdefghij')  # 랜덤하게 하나의 원소 선택해서 리턴
random.sample([1, 2, 3, 4, 5],  3)  # 랜덤하게 여러 개의 원소를 선택 (여기서는 3)
random.shuffle([1, 2, 3, 4, 5, 6, 7])  # 원소의 순서를 랜덤하게 바꿈

random.seed(숫자) # seed를 넣으면 고정되어서, 계속 같은 값이 추출됨.

```

### 열 인덱스 출력 순서 변경
```py
df4 = df4[['c', 'a', 'new']]
```