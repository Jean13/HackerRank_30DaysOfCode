def factorial(N):
    i = 1
    x = 1
    for _ in range(N):
        x = x * i
        i += 1
    print(x)

N = int(input())
factorial(N)
