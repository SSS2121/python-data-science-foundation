def resolver_ecuacion_lineal(a, b):
    """Resuelve ecuaciones del tipo ax + b = 0."""
    if a == 0:
        if b == 0:
            return "Infinitas soluciones (0x + 0 = 0)"
        else:
            return "Sin solución (0x + b = 0, con b != 0)"
    
    x = -b / a
    return x

# Prueba: 2x - 4 = 0 -> x = 2
print("El valor de x es:", resolver_ecuacion_lineal(2, -4))