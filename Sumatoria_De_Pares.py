def Sumatoria_De_Pares(n):
    if not isinstance(n, int):
        raise TypeError("El valor de n debe ser un número entero")
    sumatoria = 0
    while n > 0:
        if n % 2 == 0:
            sumatoria += n
        n -= 1
    return sumatoria
print(Sumatoria_De_Pares(10))
print(Sumatoria_De_Pares(15))