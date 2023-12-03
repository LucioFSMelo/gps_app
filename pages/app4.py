import streamlit as st
from streamlit_folium import folium_static
import folium
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

st.sidebar.markdown("Traçando Localização/Rotas")
st.markdown("# Traçando Localização/Rotas")

st.markdown("Você já deve ter notado que é bastante chato estarmos colocando as coordenadas. \n"
            "Agora vamos fazer diferente, aqui iremos inserir o nome dos locais de origem e destino.")

geolocator = Nominatim(user_agent="app_geocode")

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

def main():
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

if __name__ == "__main__":
    main()