raw_data <- read.csv("C:/Users/simjiyoung/mulcam/R_TEMP/project material/Korea Income and Welfare.csv")

library(ggplot2)
library(dplyr)

data <- raw_data
id_count <-count(data,id,sort = F)
tail(id_count)
table(id_count$n)
pie(id_count$n, main= "활동 기간별 패널 수")
prop.table(table(id_count$n))

# 10046명의 데이터
# 패널로 활동한 기간별 패널 수 (년단위)

# 1      2      3      4     5      6      7      8     9      10     11     12    13     14 
# 810    618    403    426   439    260    276   1599   199    280    276    206   236    4018 
# 0.08   0.06   0.04  0.04   0.04   0.026  0.027 0.16   0.028  0.027  0.027  0.02  0.023  0.4



id_unique <- unique(data)
summary(data$year)
table(data$year)
hist(data$year, main = "년도별 패널 수")

# 년도별 패널 수 
# 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 
# 7072 6580 6314 6207 6034 5735 7532 7312 7048 6914 6723 6581 6474 6331 

data2005 <- data %>% filter(data$year == 2005)
data2006 <- data %>% filter(data$year == 2006)
data2007 <- data %>% filter(data$year == 2007)
data2008 <- data %>% filter(data$year == 2008)
data2009 <- data %>% filter(data$year == 2009)
data2010 <- data %>% filter(data$year == 2010)
data2011 <- data %>% filter(data$year == 2011)
data2012 <- data %>% filter(data$year == 2012)
data2013 <- data %>% filter(data$year == 2013)
data2014 <- data %>% filter(data$year == 2014)
data2015 <- data %>% filter(data$year == 2015)
data2016 <- data %>% filter(data$year == 2016)
data2017 <- data %>% filter(data$year == 2017)
data2018 <- data %>% filter(data$year == 2018)

# 지역 ----------------------------------------------------------------
data.unique <- unique(data [, c("id","region")])
summary(data.unique$region)
table(data.unique$region)
hist(data.unique$region, main = "지역별 패널 수")
prop.table(table(data.unique$region))

# 1서울    2 경기    3경남    4경북    5충남   6 강원&충북   7전라& 제주 
#  1923     2440     1811      1340     968      801           1747 
#  0.17     0.22     0.16      0.12     0.087    0.07          0.15


summary(data2005$region)
table(data2005$region)
hist(data2005$region, main = "지역별 패널 수")
prop.table(table(data2005$region))

summary(data2012$region)
table(data2012$region)
hist(data2011$region, main = "지역별 패널 수")
prop.table(table(data2011$region))

#2005년
# 1          2          3          4          5          6          7 
# 1335       1569       1219       915        529        456        1049 
# 0.18877262 0.22186086 0.17236991 0.12938348 0.07480204 0.06447964 0.14833145 

# 2006년
# 1          2          3          4          5          6          7 
# 1198       1413       1153       864        507        434        1011 
# 0.18877262 0.22186086 0.17236991 0.12938348 0.07480204 0.06447964 0.14833145 


# 2007년 
# 1          2          3          4          5          6          7 
# 1110       1351       1093       832        511        420        997
# 0.17579981 0.21396896 0.17310738 0.13177067 0.08093126 0.06651885 0.15790307 

# 2008년
# 1          2          3          4          5          6          7 
# 1044       1340       1091       816        492        417        1007 
# 0.16819720 0.21588529 0.17576929 0.13146448 0.07926535 0.06718221 0.16223618 

#2009년
# 1          2          3          4          5          6          7 
# 994        1292       1039       796        518        413        982
# 0.16473318 0.21411999 0.17219092 0.13191912 0.08584687 0.06844548 0.16274445 

# 2010년
# 1          2          3          4          5          6          7 
# 932        1234       961        755        496        403        954 
# 0.16251090 0.21517001 0.16756757 0.13164778 0.08648649 0.07027027 0.16634699 

#2011년
# 1          2          3          4          5          6          7 
# 1132       1510       1312       1002       694        590        1292 
# 0.15029209 0.20047796 0.17419012 0.13303240 0.09214020 0.07833245 0.17153478 

#2012년



summary(data$income)
table(data$income)
barplot(data$income)

income_box <- as.data.frame(data$income)
boxplot(income_box)$stats

# Min. 1     st Qu.  Median    Mean    3rd Qu.    Max. 
# -232174    1140    2428      3441    4695       468209 
# 수입은 반드시 범주화 필요할 듯. 범위가 너무 큼...

data.unique <- unique(data [, c("id","family_member")])
summary(data.unique$family_member)
table(data$family_member)
hist(data.unique$family_member, main = "가족구성원 수(본인포함)")
prop.table(table(data.unique$family_member))



#가족구성원 수 (본인포함)
# 1     2      3      4       5     6       7       8       9 
# 4254  5142   3781   3220    998   289     77      11      4 
# 0.23  0.29   0.21   0.18    0.057  0.016  0.0045  0.0005  0.0002

data.unique <- unique(data [, c("id","gender")])
summary(data.unique$gender)
table(data.unique$gender)
hist(data.unique$gender, main = "성별 수 ")
prop.table(table(data.unique$gender))

# 남         여 
# 7612       3718 
# 0.6718447  0.3281553 

# id 고유 번호만 봤을 때 10046명이었는데, 성별로 봤을 때 11330명임. 
# 확인해보니까 id는 같은데 gender를 1로 기록했을 때도 있고 2로 기록했을 때도 있음;


max(data$year_born)


# 소득 이상치 해결

# income_c <- data %>% filter(income >=0 & income < 10000) %>% filter(company_size==NA| company_size==1 | company_size==2|company_size==3 |company_size==4 | company_size==5 |company_size==6 | company_size==7 |company_size==8 | company_size==9 | company_size==10 )


income_c <- ifelse(income_c <0 | income_c > 10000, NA , income_c )

company_size_c <- ifelse(data$company_size == 11 | data$company_size == 99, NA, data$company_size)


head(income_c)
tail(income_c)

clear_data <- cbind(data$id,data$year, data$region, data$family_member, data$gender, data$year_born, data$education_level,data$marriage, data$religion, data$occupation, company_size_c, data$reason_none_worker, data$job, data$income, income_c)

colnames(clear_data)<- c("id","year","region","family_member","gender","year_born","education_level","marriage","religion","occupation","company_size","reason_none_worker","job","income","income_c")

clear_data_f <- as.data.frame(clear_data)

head(clear_data)

table(income_c)

head(income_c, 100)



boxplot(income_c$income)$stats
summary(income_c$income)


#--------------

lm(income_c ~ region + family_member+ gender+year_born+education_level+marriage+religion+company_size + job, data = clear_data_f)

lm(income_c ~ region, data = clear_data_f)
lm_1<-lm(education_level ~ region, data = clear_data_f)
summary(lm_1)

lm_2<-lm(education_level ~ company_size, data = clear_data_f)
summary(lm_2)




