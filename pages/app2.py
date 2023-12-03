import streamlit as st
import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static

st.markdown("# Gerador de mapas 🎈")
st.sidebar.markdown("Gerando mapa")


def main():
    st.title("Aplicação com Leaflet e Streamlit")

    # Input para inserir as coordenadas
    latitude = st.number_input("Insira a Latitude:")
    longitude = st.number_input("Insira a Longitude:")

    # Botão para gerar o mapa
    if st.button("Gerar Mapa"):
        # Criação do mapa com base na latitude e longitude inseridas
        mapa = folium.Map(location=[latitude, longitude], zoom_start=15)
        folium.Marker([latitude, longitude], popup="Localização").add_to(mapa)

        # Exibindo o mapa no Streamlit usando streamlit_folium
        folium_static(mapa)

if __name__ == "__main__":
    main()