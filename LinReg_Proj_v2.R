data_set = read.csv("/Users/brian/Desktop/SimpleLinearRegression/xy_sorted.csv")
x = data_set$x
y = data_set$y

reg_model <- lm(y ~ x)

print (summary(reg_model))
print (confint(reg_model,'x',level=.95))
print(aov(reg_model))