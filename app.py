import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

# Cargar los datos
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Ruta del archivo CSV
data = load_data("productos_labiales_nombres.csv") 

# Preprocesar datos
data['Precio'] = data['Precio'].str.replace('$', '', regex=False).str.replace(',', '.', regex=False)
data['Precio'] = data['Precio'].fillna(0).astype(float)
data['Reseñas'] = data['Reseñas'].fillna(0).astype(float)

# Crear una representación para similitudes
data['Features'] = data['Marca'] + " " + data['Nombre']
vectorizer = TfidfVectorizer()
features_matrix = vectorizer.fit_transform(data['Features'])

# Similitud basada en características
similarity_matrix = cosine_similarity(features_matrix)

# Sistema de recomendación
def recommend_products(product_name, top_n=5):
    if product_name not in data['Nombre'].values:
        return "Producto no encontrado"
    
    product_idx = data[data['Nombre'] == product_name].index[0]
    similar_indices = similarity_matrix[product_idx].argsort()[-top_n-1:-1][::-1]
    recommendations = data.iloc[similar_indices]
    return recommendations[['Nombre', 'Marca', 'Precio', 'Imagen', 'Reseñas']]

# Interfaz de Streamlit
st.title("Sistema de Recomendación de Productos")

# Selección de producto
product_list = data['Nombre'].unique()
selected_product = st.selectbox("Selecciona un producto:", product_list)

# Mostrar recomendaciones
if st.button("Recomendar"):
    recomendaciones = recommend_products(selected_product)
    
    if isinstance(recomendaciones, str):
        st.write(recomendaciones)  # Mostrar mensaje de error si no se encuentra el producto
    else:
        st.write("### Productos Recomendados")
        for _, row in recomendaciones.iterrows():
            st.write(f"**Nombre**: {row['Nombre']}")
            st.write(f"**Marca**: {row['Marca']}")
            st.write(f"**Precio**: ${row['Precio']}")
            st.write(f"**Reseñas**: {row['Reseñas']}")
            st.image(row['Imagen'], width=150)  # Mostrar imagen del producto si está disponible
            st.write("---")
