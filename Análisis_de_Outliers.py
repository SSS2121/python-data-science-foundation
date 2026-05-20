def calcular_desviacion_estandar(datos):
    """Calcula la media y desviación estándar de los datos."""
    if not datos:
        raise ValueError("La lista de datos no puede estar vacía")
    
    media = sum(datos) / len(datos)
    varianza = sum((x - media) ** 2 for x in datos) / len(datos)
    desviacion_estandar = varianza ** 0.5
    return media, desviacion_estandar

def detectar_outliers(datos, desviaciones=2):
    """
    Detecta valores atípicos (outliers) usando el método de desviación estándar.
    
    Args:
        datos: Lista de números
        desviaciones: Número de desviaciones estándar para el umbral (por defecto 2)
    
    Returns:
        Tupla (outliers, datos_limpios)
    """
    media, std = calcular_desviacion_estandar(datos)
    limite_superior = media + (desviaciones * std)
    limite_inferior = media - (desviaciones * std)
    
    outliers = [x for x in datos if x > limite_superior or x < limite_inferior]
    datos_limpios = [x for x in datos if limite_inferior <= x <= limite_superior]
    
    return outliers, datos_limpios

if __name__ == '__main__':
    dataset = [10, 12, 11, 15, 12, 100, 14, 13, -50, 12]
    anomalos, limpios = detectar_outliers(dataset)
    
    print("Outliers detectados:", anomalos)
    print("Datos limpios:", limpios)
    print(f"Total outliers: {len(anomalos)}/{len(dataset)}")