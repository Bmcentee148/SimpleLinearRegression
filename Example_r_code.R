#Assigning values to x, y, and z

x=3
sqrt(x)
z=2
y=7
x*y*z

#Vectors

x=c(1,2,3,5,7,9)
2*x
x^2
y=c(2,5,8,1,4,6)
sum(x*y)    ##Gives the "dot product"
##Summary statistics
mean(x)
var(x)
sd(x)
##Frmula for variance
sum((x-mean(x))^2)/5

x=read.csv("C:/Users/jcolton/Desktop/Exam 1.csv", header = TRUE)
x=x$EXAM
x=x[-100]
hist(x)
plot(density(x))  ##Approximate by continuous curve
summary(x)
boxplot(x)
length(x)  ## number of students
#test if the mean score was 65
t.test(x,mu=65)

t=(mean(x)-65)/(sd(x)/sqrt(length(x)))

##percentiles of distribution
pnorm(1.96)
1-pt(t,101)
2*(1-pt(t,101))   #2-sided p-value
