def fibonacci(num):
    a,b = 0,1
    fib_lista =[]
    for i in range(num):
        if i > num:
            return fib_lista
        else:
            fib_lista.append(b)
            a,b = b, a+b
    return fib_lista
            
print(fibonacci(10))