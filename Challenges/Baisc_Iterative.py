def function(x):
    return x**2 + 5*x + 6

def derivative(x):
    return 2*x + 5

x = 0

learning_rate = 0.2
num_iterations = 100

for _ in range(num_iterations):
    gradient = derivative(x)
    x = x - learning_rate * gradient

print("the min value at a =",x)
