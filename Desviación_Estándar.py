def Desviacion_Estandar(lista):
    if not all(isinstance(lista[i], (int, float)) for i in range(len(lista))):
        return "La lista solo puede contener números enteros o decimales."
    if len(lista) == 0:
        return "La lista no puede estar vacía."
    if len(lista) == 1:
        return "La desviación estándar de una lista con un solo elemento es 0."
    n = len(lista)
    media = sum(lista) / n
    varianza = sum((x - media) ** 2 for x in lista) / n
    desviacion_estandar = varianza ** 0.5
    cercania = round(desviacion_estandar)
    if cercania == desviacion_estandar:
        cercania = "Exacta"
    return "resultado: " + str(round(desviacion_estandar, 4)) + " | cercanía: " + str(cercania)

print(Desviacion_Estandar([1, 12, 23, 23, 16, 23, 21, 16]))