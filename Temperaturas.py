def Cambio_temp_Cel (Celcius):
    if not isinstance(Celcius, (int, float)):
        raise TypeError("La temperatura en Celsius debe ser un número")

    Farenheit = (Celcius * 9/5) + 32
    return Farenheit


def Cambio_temp_Far (Farenheit):
    if not isinstance(Farenheit, (int, float)):
        raise TypeError("La temperatura en Farenheit debe ser un número")

    Celcius = (Farenheit - 32) * 5/9
    return Celcius

print(Cambio_temp_Cel(100))
print(Cambio_temp_Cel(0))
print(Cambio_temp_Cel(-40))
print(Cambio_temp_Cel(37.5))
try:
    print(Cambio_temp_Cel("veinte"))  # Esto generará un error
except TypeError as e:
    print(e)
print("--------------------------------------------------")

print(Cambio_temp_Far(212))
print(Cambio_temp_Far(32))
print(Cambio_temp_Far(98.6))
