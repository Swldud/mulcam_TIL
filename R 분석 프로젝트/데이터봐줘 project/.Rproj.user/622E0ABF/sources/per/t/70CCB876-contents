a <- read.csv("C:/Users/simjiyoung/mulcam/R_TEMP/project material/Korea Income and Welfare_clear.csv")

a$e_level[a$education_level == 1| a$education_level == 2] <- 1 # 무학
a$e_level[a$education_level == 3] <- 2 #"초등학교"
a$e_level[a$education_level == 4] <- 3 #"중학교"
a$e_level[a$education_level == 5] <- 4 #"고등학교"
a$e_level[a$education_level == 6 | a$education_level == 7] <- 5  #"대학교"
a$e_level[a$education_level == 8] <- 6  # "석사"
a$e_level[a$education_level == 9] <-7  # "박사"

table(a$e_level)

# mariage
#1) 해당 없음(18세 미만) 2) 기혼 3) 사망으로 별거 4) 별거 5) 미혼 6) 기타
a$marriage_1[a$marriage ==0 | a$marriage == 5] <- 1 # 미혼
a$marriage_1[a$marriage ==1] <- 2 # 기혼
a$marriage_1[a$marriage ==2] <-3 # 사별
a$marriage_1[a$marriage ==3] <- 4 # 이혼
a$marriage_1[a$marriage ==4] <- 5 #  별거
a$marriage_1[a$marriage ==6] <- 6 # 기타

table(a$marriage_1)

# religion 
# 1 있음 2 없음 9는 없음으로
a$religion<- ifelse(a$religion==9 ,2, a$religion)
table(a$religion)


# occupation
#install.packages("readxl")
library(dplyr)
library(readxl)
setwd("C:/R_TEMP/r프로젝트")
occupation_1 <- read_xlsx("7__F.xlsx")

View(occupation_1)
# 소분류
occ <- occupation_1[,3:4]
occ_1 <- na.omit(occ)
View(occ_1)


#company_size
table(a$company_size) 
#99 해당사항 없음 => 결측치 처리
a$company_size <- ifelse(a$company_size==99 ,0, a$company_size)
a$company_size <- ifelse(a$company_size==0 ,0, a$company_size)
table(a$company_size)


# reason_none_worker 
# 1) 능력없음 2) 군입대 3) 학교공부 4) 취학준비
# 5) 취업준비 6) 가사노동자 7) 집에서 아이 돌보기 8) 간호 
# 9) 경제활동 포기 10) 근로의사없음 11) 기타

# 0 과 99 기타로 
a$reason_none_worker <- ifelse(a$reason_none_worker==0 |a$reason_none_worker==99,11,                                            a$reason_none_worker)

table(a$reason_none_worker)

#------------------------------------------

data <- a

#######################
data <-read.csv("C:/Users/simjiyoung/mulcam/R_TEMP/project material/train_dataset_1.csv")

#-----------------------------------------
data$gender_2[data$gender == 2] <- 0
data$gender_2[data$gender ==1 ]<-1


data$marriage_2[data$marriage == 2] <- 1
data$marriage_2[data$marriage == 1] <- 0
data$marriage_2[data$marriage == 3] <- 0
data$marriage_2[data$marriage == 4] <- 0
data$marriage_2[data$marriage == 5] <- 0
data$marriage_2[data$marriage == 6] <- 0

table(data$marriage_2)

data$religion_2[data$religion == 1] <- 1
data$religion_2[data$religion == 2] <- 0


#-------------------------------
data$job[substr(data$occupation,1,2) == 11] <- 11 
data$job[substr(data$occupation,1,2) == 12] <- 12 
data$job[substr(data$occupation,1,2) == 13] <- 13 
data$job[substr(data$occupation,1,2) == 14] <- 14 
data$job[substr(data$occupation,1,2) == 15] <- 15
data$job[substr(data$occupation,1,2) == 21] <- 21 
data$job[substr(data$occupation,1,2) == 22] <- 22 
data$job[substr(data$occupation,1,2) == 23] <- 23 
data$job[substr(data$occupation,1,2) == 24] <- 24 
data$job[substr(data$occupation,1,2) == 26] <- 26 
data$job[substr(data$occupation,1,2) == 27] <- 27 
data$job[substr(data$occupation,1,2) == 28] <- 28 
data$job[substr(data$occupation,1,2) == 31] <- 31 
data$job[substr(data$occupation,1,2) == 32] <- 32 
data$job[substr(data$occupation,1,2) == 33] <- 33 
data$job[substr(data$occupation,1,2) == 39] <- 39 
data$job[substr(data$occupation,1,2) == 41] <- 41 
data$job[substr(data$occupation,1,2) == 42] <- 42 
data$job[substr(data$occupation,1,2) == 43] <- 43 
data$job[substr(data$occupation,1,2) == 44] <- 44 
data$job[substr(data$occupation,1,2) == 51] <- 51 
data$job[substr(data$occupation,1,2) == 52] <- 52 
data$job[substr(data$occupation,1,2) == 53] <- 53 
data$job[substr(data$occupation,1,2) == 61] <- 61 
data$job[substr(data$occupation,1,2) == 62] <- 62 
data$job[substr(data$occupation,1,2) == 63] <- 63
data$job[substr(data$occupation,1,2) == 71] <- 71
data$job[substr(data$occupation,1,2) == 72] <- 72
data$job[substr(data$occupation,1,2) == 73] <- 73 
data$job[substr(data$occupation,1,2) == 74] <- 74
data$job[substr(data$occupation,1,2) == 75] <- 75 
data$job[substr(data$occupation,1,2) == 76] <- 76 
data$job[substr(data$occupation,1,2) == 77] <- 77 
data$job[substr(data$occupation,1,2) == 78] <- 78 
data$job[substr(data$occupation,1,2) == 79] <- 79 
data$job[substr(data$occupation,1,2) == 81] <- 81 
data$job[substr(data$occupation,1,2) == 82] <- 82 
data$job[substr(data$occupation,1,2) == 83] <- 83 
data$job[substr(data$occupation,1,2) == 84] <- 84 
data$job[substr(data$occupation,1,2) == 85] <- 85 
data$job[substr(data$occupation,1,2) == 86] <- 86 
data$job[substr(data$occupation,1,2) == 87] <- 87 
data$job[substr(data$occupation,1,2) == 88] <- 88
data$job[substr(data$occupation,1,2) == 89] <- 89 
data$job[substr(data$occupation,1,2) == 91] <- 91 
data$job[substr(data$occupation,1,2) == 92] <- 92 
data$job[substr(data$occupation,1,2) == 93] <- 93
data$job[substr(data$occupation,1,2) == 94] <- 94
data$job[substr(data$occupation,1,2) == 95] <- 95
data$job[substr(data$occupation,1,2) == 99] <- 99 
data$job[substr(data$occupation,1,2) == "A0"] <- "A0" 


#------------------------------

data$age[data$year - data$year_born +1 < 20]<- 1
data$age[data$year - data$year_born +1 >= 20 & 
           data$year - data$year_born +1 < 30]<- 2 
data$age[data$year - data$year_born +1 >= 30 &
           data$year - data$year_born +1 < 40]<- 3 
data$age[data$year - data$year_born +1 >= 40 &
           data$year - data$year_born +1 < 50]<- 4
data$age[data$year - data$year_born +1 >= 50 &
           data$year - data$year_born +1 < 60]<- 5 
data$age[data$year - data$year_born +1 >= 60 &
           data$year - data$year_born +1 < 70]<- 6 
data$age[data$year - data$year_born +1 >= 70 &
           data$year - data$year_born +1 < 80]<- 7 
data$age[data$year - data$year_born +1 >= 80 &
           data$year - data$year_born +1 < 90]<- 8 
data$age[data$year - data$year_born +1 >= 90 &
           data$year - data$year_born +1 < 100]<- 9 

table(data$age)
#--------------------------

# write.csv(data, "C:/Users/simjiyoung/mulcam/R_TEMP/project material/dataset_final_F.csv", row.names = F)



# data <- read.csv("C:/Users/simjiyoung/mulcam/R_TEMP/project material/dataset_final_F.csv")


table(data$marriage)

multi <-lm(quantile_group ~region + family_member+ gender+year_born+education_level+marriage+religion+company_size+ occupation, data = data)
summary(multi)

library(car)
vif(multi)


# 지역이 서열화가 안 되어있음, 나이 역코딩 안함, 더미변수로 변환 안 함. 직업의 숫자에 의미 없음  => 전처리 다시!
# r^2 = 0.654 

multi1 <-lm(quantile_group ~region + family_member+ gender_2+age+education_level+marriage_2+religion_2+company_size+ occupation, data = data)
summary(multi1)

# r^2 = 0.644 


multi2 <-lm(quantile_group~ family_member+ gender_2+age+education_level+marriage_2+religion_2+company_size, data = data)

summary(multi2)

# 나이 범주화, 지역과 직업 빼고, 명목변수 더미변수로 전환 
#  r^2 = 0.638 

multi2_1 <-lm(quantile_group~ family_member+ gender+ age+education_level+company_size, data = data)

summary(multi2_1)

vif(multi2_1)

# 종교 제거
# 나이를 범주화 시켜야 그나마 e가 들어가지 않는 소숫점 자리의 계수가 나옴...
#  r^2 =0.6378 


shapiro.test(data$quantile_group)
# install.packages("psy")
library(psy)
cronbach(data)
# 크론바흐는 왜 안 돌아가는지 잘 모르겠따...
library(car)
vif(multi1_1)
install.packages("MASS")
library(MASS)
AIC <- stepAIC(multi1)



multi2 <-lm(quantile_group ~age + education_level + company_size , data = data)
summary(multi2)

# 서열변수들만 넣고 해보기!
# r^2 = 0.4826


multi_m <-lm(income ~ region + family_member+ gender+education_level+marriage+religion+company_size + occupation, data = data)






table(data$job)

plot(multi)

#VIF
install.packages("car")
library(car)
vif(multi) # vif 5가 넘는 변인X


library(tidyr)
# 소득분위 = 4.472945 -0.371971*(나이 앞자리ㅎ) +0.774379*(교육수준) + 0.223727*(회사규모)
#

lm2 <- lm(income~ quantile_group, data = data)
lm2
summary(lm2)

lm3 <- lm(quantile_group ~ company_size, data = data)
lm3
summary(lm3)
# 0.4827

lm4 <- lm(quantile_group ~ age, data = data)
lm4
summary(lm4)
# 0.1063 


lm6 <- lm(data$quantile_group ~ data$family_member)
lm6
summary(lm6)
# 1.502  

lm7 <- lm(data$quantile_group ~ data$education_level)
lm7
summary(lm7)
# 1.269 

lm8 <- lm(data$quantile_group ~ data$religion)
lm8
summary(lm8)
# 0.3968

lm9 <- lm(data$quantile_group ~ data$gender)
lm9
summary(lm9)

df1 <- data %>% filter(quantile_group ==2)
table(df1$job)

df1_0 <- df1 %>% filter(occupation > 0)
table(df1_0$job)

df1_0_10 <- df1_0 %>% filter(reason_none_worker == 1)
table(df1_0_10$year_born)

table(df1_0_10$education_level)

df2 <- data %>% filter(job == 61)
table(df2$quantile_group)



