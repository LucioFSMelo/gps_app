import streamlit as st
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static
from geopy.distance import geodesic


def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers


def gerando_mapa():
    st.title("Aplicação prática com latitude e longitude")

    # Input para inserir as coordenadas
    latitude = st.number_input("Insira a Latitude:")
    longitude = st.number_input("Insira a Longitude:")

    # Botão para gerar o mapa
    if st.button("Gerar Mapa"):
        # Criação do mapa com base na latitude e longitude inseridas
        mapa1 = folium.Map(location=[latitude, longitude], zoom_start=15)
        folium.Marker([latitude, longitude], popup="Localização").add_to(mapa1)

        # Exibindo o mapa no Streamlit usando streamlit_folium
        folium_static(mapa1)
    
    st.title("Calculadora de Distância entre Localizações")

    # Input para inserir as coordenadas da primeira localização
    st.write("### Localização A")
    lat_a = st.number_input("Latitude A:")
    lon_a = st.number_input("Longitude A:")

    # Input para inserir as coordenadas da segunda localização
    st.write("### Localização B")
    lat_b = st.number_input("Latitude B:")
    lon_b = st.number_input("Longitude B:")

    # Botão para calcular a distância e gerar o mapa
    if st.button("Calcular Distância"):
        # Criação do mapa com base nas coordenadas inseridas
        mapa = folium.Map(location=[lat_a, lon_a], zoom_start=10)

        # Adiciona marcadores de A e B no mapa
        folium.Marker([lat_a, lon_a], popup="Localização A").add_to(mapa)
        folium.Marker([lat_b, lon_b], popup="Localização B").add_to(mapa)

        # Calcula a distância entre as duas localizações
        distance = calculate_distance((lat_a, lon_a), (lat_b, lon_b))
        st.write(f"Distância entre Localização A e B: {distance:.2f} km")

        # Exibindo o mapa no Streamlit usando streamlit_folium
        folium_static(mapa)
    
if __name__ == "__main__":
    gerando_mapa()