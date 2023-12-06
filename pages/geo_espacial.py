import streamlit as st
import pydeck as pdk
import folium
from streamlit_folium import folium_static

# Dados fictícios para ilustração
dados_3d = [
    {'position': [0, 0, 0], 'color': [255, 0, 0]},
    {'position': [10, 10, 0], 'color': [0, 255, 0]},
    {'position': [20, 0, 0], 'color': [0, 0, 255]},
]

# Função para criar visualização 3D com pydeck
def criar_visualizacao_3d():
    layer = pdk.Layer(
        'ScatterplotLayer',
        data=dados_3d,
        get_position='position',
        get_radius=200,
        get_fill_color='color',
    )

    view_state = pdk.ViewState(
        longitude=-34.89130304634319,
        latitude=-7.957734131420149,
        zoom=1,
        pitch=45,
        bearing=0
    )

    r = pdk.Deck(layers=[layer], initial_view_state=view_state)
    st.pydeck_chart(r)

# Função para criar mapa interativo com Folium
def criar_mapa_folium():
    m = folium.Map(location=[-7.957734131420149, -34.89130304634319], zoom_start=2)

    # Adicione marcadores ao mapa (pode ser personalizado com seus próprios dados)
    folium.Marker([-7.957734131420149, -34.89130304634319], popup='Marcador 1').add_to(m)
    folium.Marker([-7.968104509921116, -34.890315993333395], popup='Marcador 2').add_to(m)

    return m


def espacial():
    st.title('Demonstração de Realidade Aumentada e Mapeamento 3D')

    # Seção de visualização 3D com pydeck
    st.header('Visualização 3D com pydeck')
    criar_visualizacao_3d()

    # Seção de mapa interativo com Folium
    st.header('Mapa Interativo com Folium')
    folium_map = criar_mapa_folium()
    folium_static(folium_map)

if __name__ == "__main__":
    espacial()