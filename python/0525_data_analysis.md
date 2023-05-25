# 데이터 분석 코드 모음 

## str.contains()
```py
data.str.contains('단어1|단어2', na = False) # 결측값이 있으면 에러가 발생하기 때문에, na = False로 설정해야 함.   
                                            # 반환은 T/F로 
```

## .values
: 값 전체 출력

## .size
: 개수 셈

## .unique()  / set()
: 중복 제거 (set은 집합 함수임.)

```py
data.열이름.unique().size

len(set(data.열이름.values))
```

- 특정 열에서 특정 단어(값)가 포함된 행 추출하기
```py
data.열이름[data.위열이름.str.contains('단어1|단어2',na=False)]
```

- 특정 열에서 특정 단어(값)가 포함된 내용(값)을 확인하기
```py
set(data.열이름[data.위열이름.str.contains('단어1|단어2',na=False)])

# 중복없이 열의 내용 확인
set(data.열이름)
```

## isin()
: series.isin([데이터 리스트])

- 조건을 충족하는 데이터 프레임 추출하기

```py
data_output = data[(data.열이름 == '단어1') & data.열이름.isin(['단어2', '단어3'])]
```


- 특정 열만 뽑아서 새로운 데이터 프레임 만들기
```py
new = old[['열이름1','열이름2']]
```

## str.slice()
: 일부 글자만 추출하는 함수로, index 번호에 맞추어서 자르면 됨
  <br>
  단, end에 해당되는 숫자는 하나 크게 쓰는 것 잊지 말기!

```py
new_data = old_data.열이름.str.slice(start=num1, stop=num2) # start ~ end+1

```

## str.replace()
: 특정 문자를 대체하기 위해 사용

- method
    - regex (정규표현식)
    <br>
      : 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식의 언어로, 문자열을 처리하는 모든 곳에서 사용된다

    <br>
    - [a-c] : abc와 같음
    - [0-5]: 012345와 같음
    - [a-zA-z]: 모든 알파벳
    - [^0-9] : 숫자를 제외
    - [^a-z]: 영어를 제외
    - [^가-힣]: 한국어를 제외

```py
data = data.str.replace('단어','대체할 단어 혹은 공백', regex=True) 

# 공백 제거
data = data.str.replace(' ', '')
```

## sort_values()
- method
    - ascending = T/F
    - inplace = T/F

```py
data.sort_values(ascending=False, inplace=True)
```

## treemap
- !pip install squarify
- label = : 박스 안에 작성될 값
- color = 을 통해서 색상 고정 가능

<br>

- 트리맵의 시각화
```py
squarify.plot(data, label= dong_chicken_count.index)  # label은 박스 안에 작성될 이름

```

## 상관관계 분석
    - 0.2 이하 : 상관관계 거의 없음  
    - 0.2 ~ 0.4 :낮은 상관관계  
    - 0.4 ~ 0.6 : 보통 관계  
    - 0.6 ~ 0.8 : 높은 상관관계  
    - 0.8 이상 : 매우 높은 상관관계  

```py
np.corrcoef(data.열이름1, data.열이름2)
```

## p-value | pearson
```py
import scipy.stats
scipy.stats.pearsonr(data.열이름1, data.열이름2)
#or
scipy.stats.pearsonr(data.['열이름1'], ['data.열이름2'])
```

## 회귀식

####  회귀식 구하기 위해 사용하는 함수
**자세한 내용을 다시 확인하거나 써야할 때에는 cctv와 인구 예제 파일 찾기**
- polyfit(x, y, 차수) : 입력과 출력 값으로부터 다항식의 계수를 찾아 주는 함수  
    - 오차가 가장 적은 n차 방정식의 계수 반환  
    - y = ax + b 식의 a와 b 반환  
        - a : 기울기  
        - b : 절편  
        
        <br>

- poly1d() : 다항식을 구하는 함수  
    - polyfit() 함수 결과를 ploy1d() 함수에게 전달하고 그 결과로 함수를 받음
    - 이 결과 함수에 x값을 넣으면 직선식을 그리는데 필요한 y값 반환
        - y = ax + b의 y 값 반환

        <br>
    
- linspace() : 직선의 x, y값으로 사용할 값 생성  
    - linspace(stat, end, num개)  
    - start~end 범위에서 균일한 간격으로 수치(점)을 num 개 생성  

<br>

- 회귀식 작성 & 그려보기
```py
data_polyfit = np.polyfit(data['열이름1'], data['열이름2'], 1)  # 맨 뒤의 숫자는 회귀식의 차수

# [] array([4.51851962e-03, 1.90623665e+03])
# 앞에 나오는 수가 기울기, 뒤에 나오는 수가 절편

func = np.poly1d(data_polyfit)  # 회귀 방정식 생성?

# 회귀선 표시
plt.plot(확인할 데이터, fnuc(확인할 데이터))  # 나머지 method는 선형그래프와 동일
```

## np.linsplace()
 : 균등한 간격의 스퀸스를 만들어 낸다

 - np.linsplace(start = 시작할 숫자, stop = 끝낼 숫자, num = 원하는 숫자 개수)


