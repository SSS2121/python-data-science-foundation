def Procesar_Datos(Peso, Altura):
    if not isinstance(Peso, (int, float)) or not isinstance(Altura, (int, float)):
        raise TypeError("El peso y la altura deben ser números")
     
    IMC = Peso / (Altura ** 2)
    print(f"Su Índice de Masa Corporal (IMC) es: {IMC:.2f}\n")
    if IMC < 18.5:
        print("Bajo peso")
    elif 18.5 <= IMC < 25:
        print("Peso normal")
    elif 25 <= IMC < 30:
        print("Sobrepeso")
    return IMC


Procesar_Datos(60, 1.70)