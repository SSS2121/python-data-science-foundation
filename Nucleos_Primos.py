
def Nucleos_Primos(n):
    if not isinstance(n, int):
        raise ValueError("La entrada debe ser un número entero.")
    primos = []
    for num in range(2, n + 1):
        is_primo = True
        for divisor in range(2, int(num**0.5) + 1):
            if num % divisor == 0:
                is_primo = False
                break
        if is_primo:
            primos.append(num)
    return print(primos)

Nucleos_Primos(10)
Nucleos_Primos(20)