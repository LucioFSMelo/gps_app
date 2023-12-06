import streamlit as st
from PIL import Image

def home():
    st.title("Mapeamento e GPS")
    st.markdown("### Esta é uma aplicação Interdisciplinar.")
    st.markdown('''Use o menu lateral para navegar entre as páginas da aplicação.  
                Visite as páginas na seguinte ordem (Introdução, Gerar Mapas, Rotas e Geoespacial), \
                para ter um bom acompanhamento da sequência didática abordada pelo seu professor.''')
    
    image = Image.open('image/mundi_brasil.jpg')

    st.image(image)

if __name__ == "__main__":
    home()