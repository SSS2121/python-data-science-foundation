def Numeros_Primos(n):
    if not isinstance(n, int):
        raise ValueError("La entrada debe ser un número entero.")


    primos = []
    valores_iniciales = [1,2]
    for num in range(2, n + 1):
        if not valores_iniciales in primos:
            for valor in valores_iniciales:
                if valor not in primos:
                    primos.append(valor)
        es_primo = True
        if num % 2 == 0 and num > 2:
            es_primo = False
        elif num % 2 == 1 and num > 2:
            es_primo = True
            primos.append(num)
    return print(primos)


Numeros_Primos(10)
Numeros_Primos(20)