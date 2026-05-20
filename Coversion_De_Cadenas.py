def Convertir_Cadena_Min_Y_May(cadena):
    if not isinstance(cadena, str):
        raise TypeError("El valor de cadena debe ser una cadena de texto")
    
    cadena_convertida = ""
    for caracter in cadena:
        if caracter.isupper():
            cadena_convertida += caracter.lower()
        elif caracter.islower():
            cadena_convertida += caracter.upper()
        else:
            cadena_convertida += caracter
    return cadena_convertida[::-1]

def Convertir_Cadena(cadena):
    if not isinstance(cadena, str):
        raise TypeError("El valor de cadena debe ser una cadena de texto")
    
    cadena_convertida = cadena[::-1]
    return cadena_convertida

1
print ("Tenga en cuenta que solo se admite texto\n")
print(Convertir_Cadena("Hola Mundo\n"))
print(Convertir_Cadena("Python es Genial\n"))