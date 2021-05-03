

x = []
value = 0

n = int(input("Enter the total number of values: "))

for i in range(0,n):
    value = int(input("\nEnter the value of x: "))

    x.append(value)

print(f"\nValues of X are: {x}")

sum_x = 0

for i in range(len(x)):
    sum_x = sum_x + x[i]

print(f"\nSum of X values is: {sum_x}")

mean_x = sum_x / n
print(f"\nMean of X is: {mean_x}")


y = []

for i in range(0, n):
    value = int(input("\nEnter the value of y: "))

    y.append(value)

print(f"\nValues of Y are: {y}")

sum_y = 0

for i in range(len(x)):
    sum_y = sum_y + y[i]

print(f"\nSum of Y values is: {sum_y}")

mean_y = sum_y / n
print(f"\nMean of Y is: {mean_y}")

diff_x = []
diff = 0

# calculating beta_one

for i in range(len(x)):
    diff = x[i] - mean_x

    diff_x.append(diff)

# print(diff_x)

square_diff_x = []

for i in range(len(diff_x)):
    value = diff_x[i]*diff_x[i]

    square_diff_x.append(value)

# print(square_diff_x)

sum_square_diff_x = 0

for i in range(len(square_diff_x)):
    sum_square_diff_x = sum_square_diff_x + square_diff_x[i]

# print(sum_square_diff_x)

diff_y = []

for i in range(len(y)):
    diff = y[i] - mean_y

    diff_y.append(diff)

# print(diff_y)

mul_diff_x_diff_y = []

for i in range(len(diff_x)):
    value = diff_x[i]*diff_y[i]

    mul_diff_x_diff_y.append(value)

# print(mul_diff_x_diff_y)

square_mult = 0

for i in range(len(mul_diff_x_diff_y)):
    square_mult = square_mult + mul_diff_x_diff_y[i]

# print(square_mult)

beta_one = square_mult / sum_square_diff_x
print(f"\nBeta one value is: {beta_one}")

# calculating beta_zero

beta_zero = mean_y - beta_one*mean_x
print(f"\nBeta zero value is: {beta_zero}")

# calculating Rss

rss_y = []

for i in range(len(y)):
    value = beta_zero + beta_one * x[i]

    rss_y.append(value)
# print(rss_y)

diff_rss = []

for i in range(len(rss_y)):
    value = y[i] - rss_y[i]
    diff_rss.append(value)

for i in range(len(diff_rss)):
    diff_rss[i] = diff_rss[i] * diff_rss[i]

sum_diff_rss = sum(diff_rss)
print("\nThe Permissible Error allowed is: " + str(sum_diff_rss))



# Applying Linear Regression logic to predict the values

X = int(input("\nEnter the value of x for which u want predict the value of Y: "))

Y = beta_zero + beta_one * float(X)
print("\nThe Predicted value is: " + str(Y))



