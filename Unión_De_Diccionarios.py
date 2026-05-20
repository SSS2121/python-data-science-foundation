def Union(Diccionario1, Diccionario2):
    if not isinstance(Diccionario1, dict) or not isinstance(Diccionario2, dict):
        raise ValueError("Ambas entradas deben ser diccionarios.")
    Diccionario3 = {}
    for clave in Diccionario1:
        Diccionario3[clave] = Diccionario1[clave]
    for clave in Diccionario2:
        if clave not in Diccionario3:
            Diccionario3[clave] = Diccionario2[clave]
        elif clave in Diccionario1 and clave in Diccionario2:
            Diccionario3[clave] = Diccionario1[clave] + Diccionario2[clave]

    return print(Diccionario3)
Diccionario1 = {'a': 1, 'b': 2, 'c': 3}
Diccionario2 = {'b': 4, 'c': 5, 'd': 6}
Union(Diccionario1, Diccionario2)