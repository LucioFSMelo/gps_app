import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import pandas as pd
import plotly.express as px

st.markdown("# Traçando Localização/Rotas")

st.markdown("Você já deve ter notado que é bastante chato estarmos colocando as coordenadas. \n"
            "Agora vamos fazer diferente, aqui iremos inserir o nome dos locais de origem e destino.")

geolocator = Nominatim(user_agent="app_geocode")

# Dados fictícios para exemplos de uso do GPS em diferentes setores
dados_gps = pd.DataFrame({
    'Setor': ['Navegação', 'Agricultura', 'Transporte Terrestre', 'Logística', 'Geologia'],
    'Exemplos': [25, 45, 30, 20, 15]
})

def calculate_distance(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

def calculate_fuel(distance, fuel_efficiency):
    return (distance / fuel_efficiency)

def calculate_fuel_cost(distance, fuel_price, fuel_efficiency):
    return (distance / fuel_efficiency) * fuel_price

def calculate_estimated_time(distance, average_speed):
    time_in_hours1 = distance / average_speed
    time_in_hours2 = distance // average_speed
    if time_in_hours1 == time_in_hours2:
        return f"{time_in_hours1} horas"
    else:
        parameter = time_in_hours1 - time_in_hours2
        converter = parameter * 60
        return f"{time_in_hours2} horas e {int(converter)} minutos"


def plot_exemplos_gps():
    # Crie um gráfico de barras interativo com Plotly Express
    fig = px.bar(dados_gps, x='Setor', y='Exemplos', color='Setor', labels={'Exemplos': 'Número de Exemplos'})
    fig.update_layout(title='Exemplos de Uso do GPS em Diferentes Setores', xaxis_title='Setor', yaxis_title='Número de Exemplos')
    
    # Adicione o gráfico ao Streamlit
    st.plotly_chart(fig)

def detalhes_setor(setor_selecionado):
    # Adicione informações detalhadas para o setor selecionado
    st.markdown(f"### Detalhes sobre o setor de {setor_selecionado}")
    
    if setor_selecionado == 'Navegação':
        st.write("A navegação utiliza o GPS para fornecer informações de localização em tempo real, facilitando a orientação e a navegação em ambientes desconhecidos.")
    elif setor_selecionado == 'Agricultura':
        st.write("Na agricultura, o GPS é usado em tratores e máquinas agrícolas para otimizar o plantio, a colheita e o monitoramento de safras.")
    elif setor_selecionado == 'Transporte Terrestre':
        st.write("No transporte terrestre, o GPS é amplamente utilizado para rastreamento de veículos, planejamento de rotas e otimização do transporte público.")
    elif setor_selecionado == 'Logística':
        st.write("O setor de logística depende do GPS para rastreamento de mercadorias, gerenciamento de estoque e otimização de rotas de entrega.")
    elif setor_selecionado == 'Geologia':
        st.write("Na geologia, o GPS é utilizado para mapeamento de terrenos, coleta de dados em campo e monitoramento de movimentos tectônicos.")

# Carregue dados geoespaciais fictícios para ilustração
dados_geoespaciais = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

def exibir_mapa_geoespacial():
    # Crie um mapa interativo com Folium
    m = folium.Map(location=[0, 0], zoom_start=2, control_scale=True)

    # Adicione as geometrias dos países ao mapa
    for index, row in dados_geoespaciais.iterrows():
        folium.GeoJson(row.geometry.__geo_interface__,
                       name=row['name']).add_to(m)

    # Exiba o mapa no Streamlit
    folium_static(m)

def mostrar_informacoes_pais(pais_selecionado):
    # Exiba informações detalhadas sobre o país selecionado
    st.markdown(f"### Informações sobre {pais_selecionado}")
    
    # Selecione os dados do país
    info_pais = dados_geoespaciais[dados_geoespaciais['name'] == pais_selecionado]

    # Exiba informações na barra lateral
    st.sidebar.subheader(f'Dados de {pais_selecionado}')
    st.sidebar.write(f"**População:** {info_pais['pop_est'].values[0]}")
    st.sidebar.write(f"**Área:** {info_pais['area'].values[0]} km²")

def exibir():
    st.title("Calculadora de Distância, Consumo e Custo de Combustível e Tempo Estimado")

    # Input para inserir o nome do local da primeira localização
    st.write("### Origem")
    location_a_name = st.text_input("Local de Origem: ")

    # Input para inserir o nome do local da segunda localização
    st.write("### Destino")
    location_b_name = st.text_input("Destino: ")

    # Inputs para preço do combustível, desempenho do carro e velocidade média
    fuel_price = st.number_input("Preço do Combustível por Litro:")
    fuel_efficiency = st.number_input("Desempenho do Carro (km por litro):")
    average_speed = st.number_input("Velocidade Média em km/h:")

    # Botão para calcular distância, gerar mapa e exibir resumo
    if st.button("Calcular e Gerar Resumo"):
        try:
            location_a = geolocator.geocode(location_a_name)
            location_b = geolocator.geocode(location_b_name)

            # Criação do mapa com base nas coordenadas geocodificadas
            mapa = folium.Map(location=[location_a.latitude, location_a.longitude], zoom_start=10)

            # Adiciona marcadores de A e B no mapa
            folium.Marker([location_a.latitude, location_a.longitude], popup="Localização A").add_to(mapa)
            folium.Marker([location_b.latitude, location_b.longitude], popup="Localização B").add_to(mapa)

            # Calcula a distância entre as duas localizações
            distance = calculate_distance((location_a.latitude, location_a.longitude),
                                           (location_b.latitude, location_b.longitude))
            st.write(f"Distância entre {location_a_name} e {location_b_name}: {distance:.2f} km")

            # Exibindo o mapa no Streamlit usando streamlit_folium
            folium_static(mapa)

            # Botão para calcular custo de combustível e tempo estimado
            fuel_ida = calculate_fuel(distance, fuel_efficiency)
            fuel_ida_volta = 2 * calculate_fuel(distance, fuel_efficiency)
            fuel_cost = calculate_fuel_cost(distance, fuel_price, fuel_efficiency)
            estimated_time = calculate_estimated_time(distance, average_speed)

            st.write(f"Consumo estimado de combustível ida: {fuel_ida:.2f} litros")
            st.write(f"Consumo estimado de combustível ida e volta: {fuel_ida_volta:.2f} litros")
            st.write(f"Custo de Combustível estimado: R${fuel_cost:.2f}")
            st.write(f"Tempo estimado de viagem: {estimated_time}")

        except AttributeError:
            st.error("Erro ao geocodificar. Certifique-se de inserir nomes de locais válidos.")

    if st.button("Mostrar Exemplos"):
        st.title('Exemplos de Uso do GPS em Diferentes Setores')
        # Seção de gráficos interativos
        st.header('Exemplos de Uso do GPS por Setor')
        plot_exemplos_gps()

        # Seção de detalhes sobre setor selecionado
        st.sidebar.title('Detalhes por Setor')
        setor_selecionado = st.sidebar.selectbox('Selecione um setor:', dados_gps['Setor'])
        detalhes_setor(setor_selecionado)

    if st.button("Brincar com dados Geoespaciais"):
        st.title('Demonstração Básica de SIG com GeoPandas e Streamlit')

        # Seção de mapa geoespacial
        st.header('Mapa Geoespacial Mundial')
        exibir_mapa_geoespacial()

        # Seção de detalhes sobre país selecionado
        st.sidebar.title('Detalhes por País')
        pais_selecionado = st.sidebar.selectbox('Selecione um país:', dados_geoespaciais['name'].unique())
        mostrar_informacoes_pais(pais_selecionado)

if __name__ == "__main__":
    exibir()