## 1. Pandas

### Pivot table
: 조건에 따라 필요한 데이터만 뽑아 값을 정렬하는 방법

<br>

#### **Pandas에서 제공하는 피봇 테이블 기능 :  pivot_table() 메소드**

pivot_table(data, values, index, columns, aggfun, fill_value, margins, margins_name)  

    - data : 분석할 데이터 프레임. 메서드 형식일때는 필요하지 않음 ex)df1.pivot_table()  
    - values : 분석할 데이터 프레임에서 분석할 열  
    - index :  행 인덱스로 들어갈 키열 또는 키열의 리스트  
    - columns : 열 인덱스로 들어갈 키열 또는 키열의 리스트    
    - aggfunc : 분석 메소드. mean이 기본 함수   
    - fill_value : NaN 대체값 지정    
    - margins : 모든 데이터를 분석한 결과를 행열로 추가할 지 여부  
    - margins_name : margins가 추가될 때 그 열(행)의 이름`  

- 방법 : 두개의 키를 사용해서 데이터를 선택  
    - 행 인덱스, 열 인덱스

```py
import seaborn as sns

# 타이타닉 데이터 중 일부 열만 추출해서 사용
df = sns.load_dataset('titanic')[['age','sex','class','fare','survived']]
df.head()
```

|age|sex|class|fare|survive|
|---|---|---|---|---|
|22|male|Third|7.25|0|
|38|female|First|71.2833|1|
|26|female|Third|7.925|1|
|35|female|First|53.1|1|
|35|male|Third|8.05|0|

```py
# 선실 등급에 따른 성별에 대해 생존여부별로 나이와 티켓값의 평균과 최대값을 산출
df_t = pd.pivot_table(df,  # 피벗할 데이터프레임
                      values=['age', 'fare'],  # 계산할 데이터
                      index=['class', 'sex'],  # 행 인덱스
                      columns='survived',  # 열 인덱스
                      aggfunc=['mean', 'max'],  # 적용 함수 종류, 여러 개 출력 가능
                     )
df_t
```

![](https://github.com/Swldud/mulcam_TIL/blob/master/python/pivot%20table%20example.png?raw=true)

<br>

### group()

: 그룹의 특성을 보여주는 / 그룹 분석을 위한 함수

#### groupby() 메소드

    - size(), count() : 그룹 데이터의 개수 반환  
        - count() : Null 값이 아닌 행만 반환  
        - size() : Null 값인 행도 모두 포함해서 반환  
    - mean(), median(), min(), max() : 그룹 데이터의 평균, 중앙값, 최소, 최대 값 반환  
    - sum(), prod(), std(),var(), quantile() : 그룹 데이터의 합계, 곱, 표준편차, 분산, 사분위수 반환  
    - first(), last() : 그룹 데이터 중 가장 첫 번째, 마지막 데이터 반환  

    - agg(), aggregate()  
        - 만약 원하는 그룹연산이 없는 경우 함수를 만들고 이 함수를 agg에 전달  
        - 또는 여러가지 그룹연산을 동시에 하고 싶은 경우 함수 이름 문자열의 리스트 전달  

    - describe()  
        - 하나의 그룹 대표값이 아니라 여러 개의 값을 데이터프레임으로 반환  

    - apply()  
        - describe() 처럼 하나의 대표값이 아닌 데이터프레임을 출력하지만 원하는 그룹 연산이 없는 경우에 사용

    - transform()  
        - 그룹에 대한 대표값을 만드는 것이 아니라 그룹별 계산을 통해 데이터 자체를 변형



```py
df2 = pd.DataFrame({
    'key1': ['A', 'A', 'B', 'B', 'A'],
    'key2': ['one', 'two', 'one', 'two', 'one'],
    'data1': [1, 2, 3, 4, 5],
    'data2': [10, 20, 30, 40, 50]
})
```
||key1|key2|data1|data2|
|---|---|---|---|---|
|0|A|one|1|10|
|1|A|two|2|20|
|2|B|one|3|30|
|3|B|two|4|40|
|4|A|one|5|50|

```py
# key1으로 그룹화
key1_groups = df2.groupby(df2.key1)

# 그룹화된 객체의 요약 확인
key1_groups.groups  # [] {'A': [0, 1, 4], 'B': [2, 3]}  

# 키 확인
key1_groups.groups.keys()  # dict_keys(['A', 'B'])  

# 특정 그룹 선택 : get_group() 사용
key1_groups.get_group('A')
key1_groups.get_group('B')

# 그룹화된 객체 df에서 그룹 전체 값 추출 (키, 값)
pd.DataFrame(key1_groups).loc[0].values  # A 그룹
pd.DataFrame(key1_groups).loc[1].values  # B 그룹

# 연산할 열 선택 후 함수 적용
key1_groups['data1'].sum()

# 여러개의 열 선택 후 함수 적용
key1_groups[['data1', 'data2']].sum()
```
<br>

#### apply()
    - apply(반복적용할 함수, axis = 0/1)
    - lambda는 반복적용할 함수를 따로 정의하지 않고 한 줄 코딩!

```py
t_df = sns.load_dataset('titanic')[['age','sex','class','fare','survived']]

# 선실별로 그룹화한 후
# 각 그룹에 대한 기초통계 정보 확인
t_groups = t_df.groupby('class')
t_groups.apply(lambda x : x.describe())
```

<br>

```py
import seaborn as sns
iris = sns.load_dataset("iris")

# versicolor 품종의 sepal_width : 꽃받침 너비의 최대값
i_groups.get_group('versicolor')['sepal_width'].max()
```

#### 그룹에 대해 열별 함수 적용

```py
group_name.agg(func_name)
group_name.aggregate(func_name)
group_name.apply(func_name)
```

#### 재귀함수 적용
```py
def top5_length(df):
    # petal_length 값으로 내림차순 정렬 후 5개 행 반환
    return df.sort_values('petal_length', ascending=False)[:5]
```

