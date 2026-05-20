def Frecuencia_de_Palabras(texto):
    if not isinstance(texto, str):
        return "Error: El argumento debe ser una cadena de texto."
    palabras = texto.split()
    frecuencia = {}
    
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
            
    return frecuencia

# Ejemplo de uso
Resultado = Frecuencia_de_Palabras("hola mundo hola, no pasa nada mundo, por que estoy contigo, no ?")
print(Resultado)