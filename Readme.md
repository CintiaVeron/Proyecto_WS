# Sistema de Scraping de Productos, Dashboard y Recomendaciones

## 🔮 Proyecto
Este proyecto consta de tres módulos principales que interactúan entre sí para ofrecer un ecosistema completo relacionado con productos y su gestión:

1. **Scraping de Productos**: Obtiene información de productos desde sitios web, procesando datos como nombre, marca, precio, reseñas e imagen.
2. **Dashboard Interactivo**: Permite analizar los datos obtenidos mediante gráficos y KPIs.
3. **Sistema de Recomendación**: Basado en similitudes de texto y características, este módulo sugiere productos relacionados.

---

## 🔍 Scraping de Productos

### ✅ **Funcionalidad**
El módulo de scraping se encarga de extraer información de productos como:
- **Nombre del Producto**
- **Marca**
- **Precio**
- **Número de Reseñas**
- **Imagen**

### 🔧 **Tecnologías Utilizadas**
- **Python**
  - Bibliotecas: `requests`, `BeautifulSoup`, `pandas`
- **Exportación**: CSV para almacenar los datos.

### ⚖️ **Ejemplo de Uso**
```bash
python scraper_productos.py
```

### 📄 **Salidas**
Archivo CSV con las columnas:
- Nombre
- Marca
- Precio
- Imagen (URL)
- Reseñas

---

## 📊 Dashboard Interactivo

### ✅ **Funcionalidad**
Permite analizar y visualizar los datos obtenidos mediante scraping. Incluye:

- **Gráficos de distribución de precios y reseñas**.
- **Ranking de marcas más populares**.
- **Marca mas Recomendada y con mas productos.**
-**Galeria de Imagenes de producto por marca para hacerlo mas dinamico**

### 🔧 **Tecnologías Utilizadas**
- **Power BI**
  - Gráficos de barras, tablas y segmentadores.
  - KPIs como: Precio Promedio, Total de Reseñas, Marca con Más Productos.

### ⚖️ **Instrucciones**
1. Importar el archivo CSV generado por el scraper.
2. Actualizar los visuales en Power BI para reflejar los datos.

---

## 💡 Sistema de Recomendación

### ✅ **Funcionalidad**
El sistema de recomendación utiliza los datos procesados para sugerir productos similares a uno seleccionado.

### 🔧 **Tecnologías Utilizadas**
- **Python**
  - Bibliotecas: `streamlit`, `pandas`, `scikit-learn`.
  - Algoritmo: Similaridad de coseno sobre texto procesado.

### 📈 **Características Clave**
- Entrada: Nombre de un producto.
- Salida: 5 productos similares basados en características (precio,reseña).


## 🌐 Desploy

### 🔥 **Streamlit Cloud**
3. Accede a la URL pública generada.
   
### https://proyectows-7fkdkopd6xacxvrkteowkg.streamlit.app/
---

## 📊 Estructura del Proyecto

```
/
|-- scrape_productos.py Script de scraping.
|-- app.py Sistema de recomendación con Streamlit
|-- requirements.txt Dependencias del proyecto.
|-- productos_labiales_nombres.csv Archivo con los datos extraídos (entrada para el dashboard).
|-- analisis de precios  Dashboard en PBI
```

---

## 🚀 Futuras Mejoras
- Integración con APIs de productos.
- Dashboard totalmente interactivo en Streamlit o herramientas similares.
- Incorporar métricas adicionales al sistema de recomendación (reseñas, precio).

---

## 📚 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

