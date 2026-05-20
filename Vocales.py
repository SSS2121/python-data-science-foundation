def Contar_Vocales(cadena):
    if not isinstance(cadena, str):
        raise TypeError("La entrada debe ser una cadena de texto")
    
    vocales = "aeiouAEIOU"
    contador = 0

    for letra in cadena:
        if letra in vocales:
            contador += 1

    return contador

print(Contar_Vocales("Hola Mundo"))
print(Contar_Vocales("Python es genial"))