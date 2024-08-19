# verifica si un numero es primo

def es_primo(num):
    for i in range(2,num-1):
        if num%i==0: 
            return False
    return True

def primos_hasta(num):
    primos=[]
    for i in range(2,num+1 ):
        resultado = es_primo(i)
        if resultado == True : 
            primos.append(i)
    return primos, len(primos)

lista, num = primos_hasta(55)
print(lista)
print(f"Se han generado {num} numeros primos")

x1 = list(map(lambda x:x   ,lista ))
x1 = list(filter(lambda x:x , lista))
x1 = [v for v in lista]
x1 = [v for v in range(num)]
x1 = list(map(lambda x:x   ,range(num) ))
x1 = list(filter(lambda x:x   ,range(1,num+1) ))
# print(x1)

primos_en = lambda num: list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5)+1)),range(2,num)))
print(primos_en(15))