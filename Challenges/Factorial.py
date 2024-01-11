def factorial_func(n):
    if n == 0:
        return 1
    else:
        return n * factorial_func(n-1)

n = 5
func = factorial_func(n)
print(func)