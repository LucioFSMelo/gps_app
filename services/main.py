import streamlit as st
import pages.introducao as introducao
import pages.gerador_mapa as gerador_mapa
import pages.geo_espacial as geo_espacial
import pages.rotas as rotas



st.sidebar.title("MENU")
page_acao = st.sidebar.selectbox(['Introdução', 'Gerar Mapa', 'Rotas', 'Geoespacial'])
    
if page_acao == 'Introdução':
        introducao.conteudo()
    
if page_acao == 'Gerar Mapa':
        gerador_mapa.gerando_mapa()

if page_acao == 'Rotas':
        rotas.exibir()

if page_acao == 'Geoespacial':
        geo_espacial.espacial()
