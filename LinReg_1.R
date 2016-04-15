# Create data for X and Y
x = c(3.3, 2.8, 1.9, 2.5, 2.2, 3.0);
y = c(9.5, 9.1, 8.8, 9.0, 8.6, 9.4);

# Get mean of X and Y and store in vars
x_bar = mean(x);
y_bar = mean(y);

# Plot the graph of X vs Y
plot(x,y);

# Calculate Sxx and Sxy 
sxx = sum((x - x_bar)^2);
sxy = sum((x - x_bar) * (y - y_bar));

# Calculute B0(intercept) and B1(slope) using Sxx and Sxy
b1 =  sxy / sxx;
b0 = y_bar - (b1 * x_bar);

# Create data for Y-hat (our estimated y values)
y_hat = b0 + (b1 * x);

# Calculate Mean Square Sum and Estimate Standard Deviation
MSE = sum((y - y_hat)^2) / 4;
s = sqrt(MSE);

# Calculate Standard Error of slope and intercept using our estimate
se_b1 = s / (sqrt(sxx));
se_b0 = s * sqrt((1/6) + (x_bar^2 / sxx));

