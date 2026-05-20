def Ordenamiento_Burbuja(lista):
    if not isinstance(lista, list):
        raise ValueError("La entrada debe ser una lista.")
    if not all(isinstance(x, (int, float)) for x in lista):
        raise ValueError("Todos los elementos de la lista deben ser números.")
    
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

Ordenamiento_Burbuja([64, 34, 25, 12, 22, 11, 90])
Ordenamiento_Burbuja([5, 1, 4, 2, 8])
Ordenamiento_Burbuja([3.5, 2.1, 4.6, 1.0])
Ordenamiento_Burbuja([1, 2, 3, 4, True])  # Esto debería generar un error