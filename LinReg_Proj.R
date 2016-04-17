# Get processed data set and create lists containing x and y values 
data_set = read.csv("/Users/brian/Desktop/SimpleLinearRegression/xy_sorted.csv")
x = data_set$x
y = data_set$y

plot(x,y)

x_bar = mean(x)
y_bar = mean(y)

# Calculate Sxx and Sxy
sxx = sum((x - x_bar) ^2)
sxy = sum((x - x_bar) * (y - y_bar))

# Get out estimates of B0 and B1
b1 = sxy / sxx
b0 = y_bar - (b1 * x_bar)

# Create list of projected y_values based on our fit equation
y_hat = b0 + (b1 * x)

# Get mean square error and estimate standard deviation
mse = sum((y - y_hat)^2) / (length(y) - 2)
s = sqrt(mse)

b0_stderr = s / sqrt(sxx)
b1_stderr = s * sqrt( (1/length(x) ) + (x_bar^2 / sxx))



