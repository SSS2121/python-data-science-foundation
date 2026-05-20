def Factorial_Recursivo(n):
    if n == 0:
        return 1
    else:
        return n * Factorial_Recursivo(n - 1)

# Se ve algo estilo asi " n! "
print(Factorial_Recursivo(5))  # Debería imprimir 120
print(Factorial_Recursivo(0))  # Debería imprimir 1