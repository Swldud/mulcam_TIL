#### F1 Score
# 필요한 패키지 설치
library(caret)
train_data <- read.csv("C:/Users/simjiyoung/mulcam/R_TEMP/project material/train_dataset_1.csv")  # 훈련 데이터셋

table(is.na(train_data))

test_dataset <- sample(rownames(train_data), size=92857) # 1000개의 데이터 추출
test_dataset
# 테스트 데이터셋

# 범주형 변수 목록
factor_vars <- c("gender", "education_level", "marriage",
                 "religion", "occupation", "company_size", "reason_none_worker", "quantile_group")

# 범주형 변수 변환
train_data[factor_vars] <- lapply(train_data[factor_vars], as.factor)
test_dataset[factor_vars] <- lapply(test_dataset[factor_vars], as.factor)

# 회귀분석 모델 훈련
model <- lm(quantile_group ~gender +education_level+marriage+ religion+ occupation+ company_size, data = train_data)

as.factor(train_data$quantile_group)
class(train_data$quantile_group)
class(test_dataset)


# 테스트 데이터셋 예측
predictions <- predict(model, newdata = test_dataset)
class(predictions)
predictions <- as.integer(predictions)
predictions
View(test_data)

# 예측값과 실제값 비교
comparison <- data.frame(Prediction = predictions, 
                         Target = test_data$quantile_group)

# 정확도 계산
accuracy <- sum(comparison$Prediction == comparison$Target) / nrow(comparison)

# 정확도 출력
print(accuracy)