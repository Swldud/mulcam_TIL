library(readxl)

raw_data <- read.csv("C:/Users/simjiyoung/mulcam/R_TEMP/project material/Korea Income and Welfare.csv")

data <- raw_data

# 나이를 연령대별로 변환------------------
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
# 2     3     4     5     6     7     8     9 
# 1979 10715 16273 15660 16578 21527  9468   656 

# 직업분류 중분류로 변환

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


table(data$job)
shapiro.test(data$job)

