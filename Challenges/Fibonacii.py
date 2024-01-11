def fibonacci_func(n):
    series = [0, 1]
    new_num = 0
    while new_num < n:
        new_num = series[-1] + series[-2]
        if new_num > n:
            break
        series.append(new_num)
    return series


n = 1000
fibmsg = fibonacci_func(n)
print(fibmsg)