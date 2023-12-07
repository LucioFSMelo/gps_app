import streamlit as st
from introducao import conteudo
from gerador_mapa import gerando_mapa
from rotas import exibir
from home import home

#print(sys.path)


st.sidebar.title("MENU")

page_acao = st.sidebar.selectbox("Escolha uma página", ('Home','Introdução', 'Gerar Mapa', 'Rotas'))

if page_acao == 'Home':
        home()

if page_acao == 'Introdução':
        conteudo()
    
if page_acao == 'Gerar Mapa':
        gerando_mapa()

if page_acao == 'Rotas':
        exibir()
