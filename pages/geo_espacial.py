import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import folium_static

def carregar_shapefile():
    # Permitir ao usuário fazer upload de um Shapefile
    shapefile_path = "dataset/mtaflorane.shp"

    if shapefile_path:
        # Ler o Shapefile com GeoPandas
        gdf = gpd.read_file(shapefile_path)

        # Definir um CRS se não estiver definido
        if gdf.crs is None:
            # Substitua 'EPSG:4326' pelo CRS desejado EPSG:4671
            gdf = gdf.to_crs(epsg=32723)

        # Exibir as informações básicas sobre o GeoDataFrame
        st.subheader("Informações do Shapefile:")
        st.write(f"Total de Registros: {len(gdf)}")
        st.write("Esquema (Schema):")
        st.write(gdf.dtypes)

        # Exibir o GeoDataFrame em uma tabela
        st.subheader("Visualização do GeoDataFrame:")
        st.write(gdf)

        # Exibir o GeoDataFrame no mapa usando Folium
        st.subheader("Visualização no Mapa:")
        m = folium.Map(location=[gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()], zoom_start=10)
        folium.GeoJson(gdf).add_to(m)
        folium_static(m)

def espacial():
    st.title("Aplicação GeoPandas e Streamlit")

    # Carregar e exibir Shapefile
    carregar_shapefile()

if __name__ == "__main__":
    espacial()