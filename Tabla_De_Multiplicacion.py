def Tabla_De_Multiplicacion(numero):
    if not isinstance(numero, int):
        raise TypeError("El valor de numero debe ser un número entero")

    tabla = []

    for i in range(1, 12+1):
        tabla.append(f"{numero} x {i} = {numero * i}") 
    return "\n".join(tabla)    

numero = int(input("Ingrese un número para generar su tabla de multiplicación: "))
print(Tabla_De_Multiplicacion(numero))