import requests
import re

def extraer_titulos(url):

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status() # Verifica si hay errores HTTP
        html = respuesta.text
        
        # Expresión regular para encontrar <h1>...</h1>
        titulos = re.findall(r'<h1>(.*?)</h1>', html, re.IGNORECASE)
        return titulos
    except Exception as e:
        return f"Error: {e}"

# Prueba (Nota: usar una URL real permitida para scraping)
print("Títulos H1:", extraer_titulos("https://www.example.com"))