def Busqueda_binaria(lista, objetivo):
    #Devuelve el índice de 'objetivo' en 'lista' o -1 si no se encuentra.
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = lista[medio]

        if valor_medio == objetivo:
            return medio
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

print(Busqueda_binaria([1, 3, 5, 7, 9], 5))  