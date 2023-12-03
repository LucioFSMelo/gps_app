import streamlit as st
from streamlit_folium import folium_static
import folium
from geopy.distance import geodesic

st.markdown("# Traçando Rotas")
st.sidebar.markdown("Traçando Rotas")

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

def main():
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
    main()