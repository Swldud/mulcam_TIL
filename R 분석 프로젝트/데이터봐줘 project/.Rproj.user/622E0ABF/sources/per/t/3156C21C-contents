# 전처리 효과 확인

raw <- read.csv("C:/Users/simjiyoung/mulcam/R_TEMP/project material/Korea Income and Welfare.csv")
clear <- train_data

qqnorm(raw$income)
qqline(raw$income)

qqnorm(clear$income)
qqline(clear$income)


#
qqnorm(raw$year_born)
qqline(raw$year_born)

qqnorm(clear$age)
qqline(clear$age)


pie( x = table(raw$region))
pie(table(raw$gender))
pie(table(raw$education_level))
pie(table(clear$education_level))

library(tidyr)

library(dplyr)
하<- data %>% filter(quantile_group ==1 | quantile_group ==2 | quantile_group ==3 | quantile_group ==4 | quantile_group ==5)

상 <- data %>% filter(quantile_group ==6 | quantile_group ==7 | quantile_group ==8 | quantile_group ==9 | quantile_group ==10)

# 등분산 가정
# var.test(하$,상$)

 
var.test(하$region,상$region) # p-value = 0.01081  var.equal=TRUE 분산이 같음.

table(raw$region)
table(저소득$region)
pie(table(raw$region), main = "전체 지역 분포")
pie(table(저소득$region), main ="50% 이하 분위 지역 분포")

prop.table(table(저소득$region))
#

var.test(하$gender,상$gender) # p-value < 2.2e-16  var.equal=TRUE

table(data$gender)
table(하$gender)
pie(table(raw$gender), main ="전체 성별 분포")
pie(table(하$gender), main ="50%이하 분위 성별 분포")
prop.table(table(하$gender))
#

var.test(하$age,상$age) # p-value < 2.2e-16  var.equal=TRUE

table(data$age)
table(하$age)
pie(table(data$age), main ="전체 나이대별 분포")
pie(table(하$age), main ="50% 이하 분위 나이대별 분포")

# 

var.test(하$family_member,상$family_member)# p-value < 2.2e-16  var.equal=TRUE

table(data$family_member)
table(하$family_member)
pie(table(data$family_member),main = "전체 가족구성원 수 분포")
pie(table(하$family_member), main = "50% 이하 분위 가족구성원 수 분포")

#

var.test(하$education_level,상$education_level)# p-value < 2.2e-16  var.equal=TRUE

table(data$education_level)
table(하$education_level)
      
pie(table(data$education_level), main = "전체 교육수준별 분포")
pie(table(저소득$education_level), main = "50% 이하 분위 교육수준별 분포")

#
var.test(하$marriage,상$marriage)# p-value < 3.16e-05  var.equal=TRUE

table(data$marriage)
table(하$marriage)
pie(table(data$marriage), main = "전체 배우자 유무 분포")
pie(table(하$marriage), main = "50% 이하 분위 배우자 유무 분포")


#
var.test(하$company_size,상$company_size)# p-value < 2.2e-16  var.equal=TRUE

table(data$company_size)
table(하$company_size)

pie(table(data$company_size), main = "전체 회사규모별 분포")
pie(table(하$company_size), main = "50% 이하 분위 회사규모별 분포")


#
var.test(하$reason_none_worker,상$reason_none_worker)# p-value < 2.2e-16  var.equal=TRUE

table(data$reason_none_worker)
table(하$reason_none_worker)

pie(table(data$reason_none_worker), main = "전체 무직 사유")
pie(table(하$reason_none_worker), main = "50% 이하 분위 무직 사유")

a <- rep(1.1)
b <- rep(2,10)
c <- rep(3,56)
d <- rep(4,200)
e <- rep(5,539)
f <- rep(6,911)
g <- rep(7,1649)
h <- rep(8,814)
i <- rep(9,73)

전체무직이유 <- data.frame(c(a,b,c,d,e,f,g,h,i,j,k))
하무직이유 <- data.frame(c(a,b,c,d,e,f,g,h,i,j,k))
상무직이유 <- data.frame(c(a,b,c,d,e,f,g,h,i,j,k))

연령별실업자 <- data.frame(c(a,b,c,d,e,f,g,h,i))

pie(table(전체무직이유))
pie(table(하무직이유))
pie(table(상무직이유))
pie(table(연령별실업자))


sum(table(저소득$reason_none_worker))
sum(table(data$reason_none_worker))

table(하$reason_none_worker)


저소득연령_1 <- 저소득 %>% filter(age == 1) 
table(저소득연령_1$reason_none_worker)

저소득연령_2 <- 저소득 %>% filter(age == 2) 
table(저소득연령_2$reason_none_worker)

저소득연령_3 <- 저소득 %>% filter(age == 3) 
table(저소득연령_3$reason_none_worker)

저소득연령_4 <- 저소득 %>% filter(age == 4) 
table(저소득연령_4$reason_none_worker)

저소득연령_5 <- 저소득 %>% filter(age == 5) 
table(저소득연령_5$reason_none_worker)

저소득연령_6 <- 저소득 %>% filter(age == 6) 
table(저소득연령_6$reason_none_worker)

저소득연령_7 <- 저소득 %>% filter(age == 7) 
table(저소득연령_7$reason_none_worker)

저소득연령_8 <- 저소득 %>% filter(age == 8) 
table(저소득연령_8$reason_none_worker)

저소득연령_9 <- 저소득 %>% filter(age == 9) 
table(저소득연령_9$reason_none_worker)

저소득무직자수입0 <- 저소득 %>% filter(income==0)
table(저소득무직자수입0$age)

table(data$income==0)
