import random as rm

def Simular_Dados():
    Dado1 = rm.randint(1, 6)
    Dado2 = rm.randint(1, 6)
    Suma = Dado1 + Dado2
    print(f"El resultado de los dados es: {Dado1} y {Dado2}. La suma es: {Suma}")

Simular_Dados()