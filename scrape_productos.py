import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la subcategoría "Labiales"
URL = "https://listado.mercadolibre.com.ar/labiales#D[A:labiales]"

# Solicitud HTTP con encabezado para evitar bloqueos
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0 Safari/537.36"
}
response = requests.get(URL, headers=headers)

# Verificar estado de la respuesta
if response.status_code == 200:
    print("Conexión exitosa a Mercado Libre")
else:
    print(f"Error al conectar: {response.status_code}")
    exit()

# Procesar contenido HTML con BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extraer nombres de los productos
productos = []
productos_html = soup.find_all('li', class_="ui-search-layout__item")

for producto in productos_html:
    try:
        # Nombre del producto
        nombre_element = producto.find('h2', class_="poly-box poly-component__title")
        nombre = nombre_element.text.strip() if nombre_element else "Nombre no disponible"

        # Marca del producto
        marca_element = producto.find('span', class_="poly-component__brand")
        marca = marca_element.text.strip() if marca_element else "Marca no disponible"

        # Precio del producto
        precio_element = producto.find('span', class_="andes-money-amount andes-money-amount--cents-superscript")
        precio = precio_element.text.strip() if precio_element else "Precio no disponible"

        # Imagen del producto
    
        # get the url image
        try:
            img_link = producto.find("img")["data-src"]
        except:
            img_link = producto.find("img")["src"]
        

        # Reseñas del producto
        reseñas_element = producto.find('span', class_="poly-reviews__rating")
        reseñas = reseñas_element.text.strip() if reseñas_element else "Sin reseñas"

        # Agregar datos al diccionario
        productos.append({
            "Nombre": nombre,
            "Marca": marca,
            "Precio": precio,
            "Imagen": img_link,
            "Reseñas": reseñas
        })
    except Exception as e:
        print(f"Error procesando un producto: {e}, Producto HTML: {producto}")

# Crear un DataFrame con los nombres extraídos
df = pd.DataFrame(productos)

# Exportar a CSV
output_file ='D:/usuarios/CIN/MIS DOCUMENTOS/Mis proyectos/Proyecto_WS/productos_labiales_nombres.csv'
try:
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Nombres guardados en {output_file}")
except PermissionError as e:
    print(f"Error al guardar el archivo CSV: {e}")


