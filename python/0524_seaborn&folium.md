# 시각화 패키지

## Seaborn

- 그래프 유형
    - plot()
    - histplot() 
    - kdeplot()
    - boxplot()
    - swarmplot()
    - lmplot()
    - heatmap()

- method
    - set_style() : 그림의 전반적인 모양 스타일링
    <br>
      ( darkgrid, whitegrid, dark, white, ticks)
    - despine() : 격자가 살짝 떨어짐.  # 솔직히 잘 모르겠음. 필요한가?
      <br>
      (left, right, bottom, offset)

### load

```py
import matplotlib.pyplot as plt
%matplotlib inline
```


### 1. histplot()
```py
sns.histplot(x=tips['total_bill'])
```

### 2. kedplot() : 밀도 그래프

```py
# KDE Plot
sns.kdeplot(x=tips['total_bill'])
```

### 3. boxplot()

- x 방향 boxplot

```py
plt.figure(figsize=(6,4))
sns.boxplot(x=tips['total_bill']) # x 값만 지정
```

- y 방향 boxplot
```py
plt.figure(figsize=(6,4))
sns.boxplot(y=tips['total_bill']) # y 값만 지정


# 박스 여러 개
plt.figure(figsize=(6,4))

sns.boxplot(x=tips['day'], y=tips['total_bill']) # y 값만 지정
# 혹은
sns.boxplot(x='day', y='total_bill', data=tips,
palette='Set3',  # 박스 색상 지정 : palette  ( Set1 Set2 Set3 RdBu  RdYlGn )
hue='smoker')   # hue는 정한 데이터를 다시 hue 기준으로 나누어서 count 함.
```

### 4. swarmplot()
- scatterplot과 달리 겹치지 않고 옆으로퍼져서 표현되는 산점도 그래프

```py
sns.swarmplot(x='day', y='total_bill', data=tips, palette='husl')


# box plot과 swarmplot 같이 사용
plt.figure(figsize=(6, 4))
sns.boxplot(x='day', y='total_bill', data=tips)
sns.swarmplot(x='day', y='total_bill', data=tips, palette='husl')
plt.show()
```

### 5. implot()
- 회귀선 그래프 

- method

    - height  : 그래프 크기
        - size 사용시 오류 발생 : height로 변경해서 사용  
    - hue  : 카테고리 데이터를 분류하여 그룹화하되 하나의 그래프에 두개의 값을 모두 표현
        - hue='sex' : 하나의 그래프에 male, female 표시
    - col  : 카테고리 데이터를 분류하여 그룹화하되 그룹의 개수만큼 그래프를 생성해서 표현
        - col='sex' : 2개의 그래프로 분리. male 그래프, female 그래프
    - fit_reg=False : 회귀선 생략 가능
    - ci = None : 신뢰구간 없음 (95:95% 신뢰구간)
    - scatter_kws = {'s':50, 'alpha':1} : 점의 크기 및 투명도

- 일반적인 선형회귀 그래프 
```py
# 신뢰구간 영역 설정 : 50% 설정 시 (일반적으로 95%로 설정)
# sns.lmplot(x='total_bill', y='tip', data=tips, ci=50)
sns.lmplot(x='total_bill', y='tip', data=tips, ci=95)
plt.show()
```

- 변수차이에 따른 회귀선 비교
```py
sns.lmplot(x='total_bill', y='tip', hue='smoker', data=tips, 
            palette='Set1',  height=5, scatter_kws={'s':30, 'alpha':0.7})  # 두 선을 따로 출력할 때는 hue 대신 col 사용
plt.show()

# 팁비율을 성별로 구분해서, 요일별로 별도 그래프 생성. (요일이 4개이기 때문에, 두 개의 회귀선이 존재하는 4개의 그래프가 작성됨)

sns.lmplot(x='total_bill', y='tip', hue='sex', data=tips, 
            palette='Set2',  height=5, col='day', col_wrap=2,
           scatter_kws={'s':30, 'alpha':0.7})

```

### 6. heatmap()
- 열 분포도
- 수치 데이터를 색으로 표시

<br>

- method
    - annot = True :  숫자 표시 여부 
    - ax = ax :  히트맵을 그릴 격자 
    - linewidths  : 선의 굵기 
    - linecolor = 'white' : 선의 색깔 
    - fmt  :  값 포맷팅 형태  (소수: '.1f' | 정수: d | 실수: f)
    - cmap = 'YlOrRd' :  colormap 형태
    - anno : 갑 표출 (T/F)

```py
flights_pv = pd.pivot_table(flights,
                           index='month',
                            columns='year',
                            values='passengers',
                            fill_value=0)

plt.figure(figsize=(6,4))
sns.heatmap(flights_pv, annot=True, fmt='d', cmap='RdBu')
plt.show()
```
<br>

- heatmap으로 상관관계 표현

```py
# 상관계수 구하기 : 상관행렬 생성
tips.corr(numeric_only=True)  # numeric = T 이면, 숫자 형태의 자료들 사이의 상관관계만 분석

# heatmap으로 상관관계 표현
plt.figure(figsize=(6,4))
sns.heatmap(tips.corr(numeric_only=True), annot=True, fmt='f', cmap='viridis')
```

### 7. pairplot()
- 3차원 이상의 데이터에 적용

```py
sns.pairplot(iris)

sns.pairplot(iris, hue='species', diag_kind='hist')
```
<br>

## folium 
- 지도를 이용해 data를 시각화 하는 도구
- !pip install folium
- https://jsonviewer.stack.hu/

<br>

- method
    - 중심좌표 인수 : location=[위도, 경도]  # 위도(latitude)와 경도(longitude) 
    - 확대비율 정의 인수 : zoon_start= (기본은 13) 
    - tiles : 맵 색상? 버전? 설정
        - OpenStreetMap (기본 값)
        - Mapbox Bright (Limited levels of zoom for free tiles)
        - Mapbox Control Room (Limited levels of zoom for free tiles)
        - Stamen (Terrain, Toner, and Watercolor)
        - Cloudmade (Must pass API key)
        - Mapbox (Must pass API key)
        - CartoDB (positron and dark_matter)

    <br>
    - folium.Marker(): 위,경도 값 리스트, popup, icon 설정
    - marker를 지도에 부착
        <br>
        folium.Marker().add_to(지도객체변수)
        <br>
        folium.CircleMarker().add_to(지도객체변수)

```py
seoul_cityhall_map = folium.Map(location=[37.566345, 126.977893], zoom_start=17)
folium.Marker([37.566345, 126.977893], popup='시청').add_to(seoul_cityhall_map)

```

### 단계 구분도  솔직히 뭔소린지 모르겠음 작동원리도 모르겠고 이해 안됨...
- 데이터를 지도 그림에 반영시켜서 전달하는 그래프
- 보통 folium 에 layer로 올려서 표시
- map 객체의 choropleth() 이용
- 사용 인수
    - geo_data : 지도 파일 경로와 파일명
    - data : 지도에 표현되어야 할 값 변수
    - columns =  [key로 사용할 data, 실제 data의 필드명]
    - key_on : 지도 경계파일인 json에서 사용할 키 값이며 지도 Data는 표준 형식으로 만들어 져야 함
    - key_on 지칭 문법 : feature(키워드).json에서 나타나키 필드명
    - folium.LayerControl().add_to(map)  : 단계구분도를 map에 표시하는 함수

```py
# 단계 구분도 :  choropleth()
geo_path = 'data/skorea_municipalities_geo_simple.json'  # json 파일
geo_str = json.load(open(geo_path, encoding='utf-8'))  # json 파일 로드
pop_df = pd.read_csv('data/population.csv', index_col='구별')

map.choropleth(geo_data=geo_str,  # 
              data=pop_df,
              columns=[pop_df.index, '소계'],
              key_on = 'feature.properties.name',  
              fill_color='PuRd',
              legend_name='인구 현황')

folium.LayerControl().add_to(map)
map

# 값이 클수록 색상이 진하게 표시


# key_on으로 설정가능한 값
# 사용하는 데이터의 key : 구별
# skorea_municipalities_geo_simple.jso 파일에서 구에 해당되는 값이 key_on으로 설정 가능
# 다음 4개 모두 구이름 (중복값 없음 : 유일한 값)
# (1) id
# (2) properties.name
# (3) feature.id
# (4) feature.properties.name
```