# AP 1
n = 7
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
    
# Recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(7):
    print(fib(i), end=" ")
    
# dynamic programming
n = 7
fib = [0, 1]

for i in range(2, n):
    fib.append(fib[i - 1] + fib[i - 2])

print(*fib)