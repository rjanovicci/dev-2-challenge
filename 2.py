def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

num = 11

print(f"{num} Faz parte da fibonacci.") if is_fibonacci(num) else print(f"{num} Nao faz parte da fibonacci.")