import streamlit as st
from PIL import Image


st.markdown("# Introdução 🎈")
st.sidebar.markdown("Página de Introdução")

st.title("Mapeamento e GPS :earth_americas: ")
st.write('EREFEM PRESIDENTE CASTELO BRANCO')
st.write('DISCIPLINA: Mapeamento e GPS')
st.write('PROFESSORA TITULAR: SANDRA GONÇALVES')
st.write('PROFESSOR CONVIDADO: LUCIO FLAVIO')

st.text('O que é catografia?')
st.markdown('A palavra cartografia tem origem na língua portuguesa, tendo sido registrada pela primeira vez em 1839 numa correspondência \n,' 
            'indicando a ideia de um traçado de mapas e cartas. Hoje entende­mos cartografia como a representação geométrica plana, simplifica­da \n'
            ' e convencional de toda a superfície terrestre ou de parte desta, apresentada através de mapas, cartas ou plantas.')

st.text('O que é latitude e  longitude?')
st.markdown('A latitude é a medida em graus de qualquer ponto da superfície terrestre até a Linha do Equador.')
st.markdown("A longitude é a medida em graus de qualquer ponto da superfície terrestre até o Meridiano de Greenwich.")
st.markdown("Os paralelos são linhas imaginárias que cortam o planeta Terra no sentido leste-oeste. O principal paralelo é a Linha do Equador.")

image = Image.open('image/cartografia.jpg')

st.image(image)