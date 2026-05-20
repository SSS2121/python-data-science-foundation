def Maximo(lista):
    if not isinstance(lista, (list, int, float)):
        return print("El argumento debe contener numeros y ser una lista.")
    if len(lista) == 0:
        return print("la lista está vacia.")
    maximo = lista[0] 
    minimo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero 
        elif numero < minimo:
            minimo = numero
    return f"maximo: {maximo}, minimo: {minimo}"

print(Maximo([3, 5, 2, 8, 1]))
Maximo([])