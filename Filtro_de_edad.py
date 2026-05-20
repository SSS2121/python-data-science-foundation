def Mayores_De_Edad(lista):
    if not isinstance(lista,(list,int,float)):
        raise TypeError("Solo se permite numeros")

    Mayores_De_Edad = []
    Menores_De_Edad = []
    for numero in lista:
        if numero >= 18:
            Mayores_De_Edad.append(numero)
        elif numero < 18:
            Menores_De_Edad.append(numero)
    return {"Mayores de edad": Mayores_De_Edad, "Menores de edad": Menores_De_Edad}


resultado = Mayores_De_Edad([5,7,3,17,19,19,20,34,35,56])
print(resultado)

