import streamlit as st
from pages import introducao, gerador_mapa, geo_espacial, rotas


def main():
    st.sidebar.title("MENU")
    page_acao = st.sidebar.selectbox(['Introdução', 'Gerar Mapa', 'Rotas', 'Geoespacial'])
    
    if page_acao == 'Introdução':
        introducao.conteudo()
    
    if page_acao == 'Gerar Mapa':
        gerador_mapa.gerando_mapa()
