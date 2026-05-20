def Identificador_de_Polindromos(palabra):
    if not isinstance(palabra, str):
      return  "La entrada debe ser una cadena de texto" 
      #si la funcion no se llama con "Print" toca cambiar al return con un print al inicio
      '''print(Identificador_de_Polindromos(0)) no se puede imprimir con el
      "return print("la entrada debe ser una cadena de texto")" por que devuelve un None,
       pero si la funcion se ejecuta sin el print, entonces si se usa el print en el return.
        '''
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

print(Identificador_de_Polindromos("Anita lava la tina"))
print(Identificador_de_Polindromos("radar"))
print(Identificador_de_Polindromos("Hola Mundo"))
print(Identificador_de_Polindromos(0))
