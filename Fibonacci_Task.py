def fibonacci(n):
    a=[1,1]
    for i in range(n-2):
        x=len(a)-1
        a+=[a[x]+a[x-1]]
    print(f"Fibonacci sequence = {a}")
    print(f" & the last number is {a[-1]}")
    return a[-1]
fibonacci(15)


