import sys
sys.path.append(r"C:\Users\luciu\Workspace\App_Gps\gps_app")
import streamlit as st
from pages import introducao, gerador_mapa, rotas, geo_espacial

print(sys.path)

st.sidebar.title("MENU")
st.sidebar.markdown('### Visite as páginas na seguinte ordem: \
                    Introdução, Gerar Mapas, Rotas e Geoespacial')

page_acao = st.sidebar.selectbox("Escolha uma página", ('Introdução', 'Gerar Mapa', 'Rotas', 'Geoespacial'))
    
if page_acao == 'Introdução':
        introducao.conteudo()
    
if page_acao == 'Gerar Mapa':
        gerador_mapa.gerando_mapa()

if page_acao == 'Rotas':
        rotas.exibir()

if page_acao == 'Geoespacial':
        geo_espacial.espacial()
