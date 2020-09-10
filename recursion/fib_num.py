def calc_fib(n):
    if (n < 2):
        return n
    fib_n1 = 0
    fib_n2 = 1
    for _ in range(2, n):
        t = fib_n2
        fib_n2 = fib_n2 + fib_n1
        fib_n1 = t  
    return fib_n2 + fib_n1


for i in range(100):
    print(calc_fib(i) % 10)    
