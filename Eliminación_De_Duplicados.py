Eliminacion_De_Duplicados = lambda x: list(set(x))

def Funcion_Eliminacion_De_Duplicados(b):
    lista_En_b =list(set(b))
    if not isinstance(b, list):
        raise ValueError("La entrada debe ser una lista.")
    return print(lista_En_b)

def Funcion_Eliminacion_De_Duplicados_Con_Mas_Datos(x,y,z):
    if not isinstance(x, list) or not isinstance(y, list) or not isinstance(z, list):
        raise ValueError("Todas las entradas deben ser listas.")
  
    return print(list(set(x + y + z)))

print(Eliminacion_De_Duplicados([1, 2, 2, 3, 4, 4, 5]))

Funcion_Eliminacion_De_Duplicados_Con_Mas_Datos([1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3])

Funcion_Eliminacion_De_Duplicados([1, 2, 3, 4, 5, 5, 5, 5])