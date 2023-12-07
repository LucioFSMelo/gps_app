import sys
sys.path.append(r"C:\Users\luciu\Workspace\App_Gps\gps_app")
#sys.path.insert(0, r'C:\Users\luciu\Workspace\App_Gps\gps_app')
import streamlit as st
from pages import introducao, gerador_mapa, rotas, home

#print(sys.path)


st.sidebar.title("MENU")

page_acao = st.sidebar.selectbox("Escolha uma página", ('Home','Introdução', 'Gerar Mapa', 'Rotas'))

if page_acao == 'Home':
        home.home()

if page_acao == 'Introdução':
        introducao.conteudo()
    
if page_acao == 'Gerar Mapa':
        gerador_mapa.gerando_mapa()

if page_acao == 'Rotas':
        rotas.exibir()
