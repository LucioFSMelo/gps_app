import streamlit as st
from PIL import Image


st.markdown("# Introdução 🎈")
st.sidebar.markdown("Página de Introdução")

st.title("Mapeamento e GPS :earth_americas: ")
st.markdown("### Esta aplicação é pode ser trabalhada de modo interdisciplinar")

st.markdown('### O que é catografia?')
st.markdown('A palavra cartografia tem origem na língua portuguesa, tendo sido registrada pela primeira vez em 1839 numa correspondência \n,' 
            'indicando a ideia de um traçado de mapas e cartas. Hoje entende­mos cartografia como a representação geométrica plana, simplifica­da \n'
            ' e convencional de toda a superfície terrestre ou de parte desta, apresentada através de mapas, cartas ou plantas.')

st.markdown('### O que é latitude e  longitude?')
st.markdown('A latitude é a medida em graus de qualquer ponto da superfície terrestre até a Linha do Equador.')
st.markdown("A longitude é a medida em graus de qualquer ponto da superfície terrestre até o Meridiano de Greenwich.")
st.markdown("Os paralelos são linhas imaginárias que cortam o planeta Terra no sentido leste-oeste. O principal paralelo é a Linha do Equador.")

image = Image.open('image/cartografia.jpg')

st.image(image)

pontos_cardeais = """### Pontos Cardeais \n
Os pontos cardeais são os quatro principais pontos de orientação em uma bússola ou em um sistema de coordenadas geográficas. 
Eles são referências fundamentais para determinar direções na Terra. Os quatro pontos cardeais são:
* Norte (N): Aponta para o Polo Norte geográfico.
* Sul (S): Aponta para o Polo Sul geográfico.
* Leste (L ou E): Indica a direção para onde o Sol nasce.
* Oeste (O ou W): Indica a direção para onde o Sol se põe."""

st.markdown(pontos_cardeais)

pontos_colaterais = """### Pontos Colaterais \n
Os pontos colaterais são direções intermediárias situadas entre os pontos cardeais na rosa dos ventos. \n 
Eles representam direções mais específicas do que os pontos cardeais e são obtidos pela combinação de um ponto cardeal com outro adjacente. \n
Os quatro pontos colaterais são:
* Nordeste (NE): Localizado entre Norte (N) e Leste (L), indicando uma direção que é simultaneamente ao norte e ao leste.
* Sudeste (SE): Encontra-se entre Sul (S) e Leste (L), apontando para uma direção que é ao mesmo tempo ao sul e ao leste.
* Sudoeste (SO ou SW): Posicionado entre Sul (S) e Oeste (O), representando uma direção que é tanto ao sul quanto ao oeste.
* Noroeste (NO ou NW): Situado entre Norte (N) e Oeste (O), indicando uma direção que é ao norte e ao oeste simultaneamente."""

st.markdown(pontos_colaterais)

st.markdown("### Rosa dos Ventos")
rosa_ventos = """A rosa dos ventos é um diagrama gráfico que mostra as principais direções cardeais e colaterais em relação aos pontos cardeais na superfície terrestre.\n
Ela é usada como uma ferramenta de orientação em mapas, bússolas e cartas náuticas. \n
A rosa dos ventos geralmente possui um formato circular, onde os pontos cardeais (Norte, Sul, Leste e Oeste) estão dispostos nos quatro pontos cardeais da circunferência."""

st.markdown(rosa_ventos)

st.image('image/rosa_dos_ventos.jpg', caption='Rosa dos Ventos')
