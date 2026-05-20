def numero_a_romano(numero):
    if not 0 < numero < 4000:
        return "Número fuera de rango"
        
    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    resultado = ""
    for valor, simbolo in valores:
        while numero >= valor:
            resultado += simbolo
            numero -= valor
            
    return resultado

# Prueba
print("2026 en romano es:", numero_a_romano(2026))