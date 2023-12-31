import streamlit as st
from PIL import Image

def conteudo():
    st.markdown("# Introdução 🎈")

    st.title("Mapeamento e GPS :earth_americas: ")
    
    st.markdown('### O que é catografia?')
    st.markdown('''A palavra cartografia tem origem na língua portuguesa, tendo sido registrada pela primeira vez em \
                1839 numa correspondência, indicando a ideia de um traçado de mapas e cartas. Hoje entende­mos \
                cartografia como a representação geométrica plana, simplifica­da e convencional de toda a \
                superfície terrestre ou de parte desta, apresentada através de mapas, cartas ou plantas.''')

    st.markdown('### O que é latitude e  longitude?')
    st.markdown('''A latitude é a medida em graus de qualquer ponto da superfície terrestre até a Linha do Equador. \
                A longitude é a medida em graus de qualquer ponto da superfície terrestre até o Meridiano de Greenwich. \
                Os paralelos são linhas imaginárias que cortam o planeta Terra no sentido leste-oeste. O principal \
                paralelo é a Linha do Equador.''')
    

    image = Image.open('image/cartografia.jpg')

    st.image(image)

    st.markdown("### Pontos Cardeais")
    pontos_card = """Os pontos cardeais são os quatro principais pontos de orientação em uma \
    bússola ou em um sistema de coordenadas geográficas. \
    Eles são referências fundamentais para determinar direções na Terra.  
    Os quatro pontos cardeais são:  
    * :blue[**Norte (N):**] Aponta para o Polo Norte geográfico.  
    * :blue[**Sul (S):**] Aponta para o Polo Sul geográfico.  
    * :blue[**Leste (L ou E):**] Indica a direção para onde o Sol nasce.  
    * :blue[**Oeste (O ou W):**] Indica a direção para onde o Sol se põe."""

    st.markdown(pontos_card)

    st.markdown("### Pontos Colaterais")
    pontos_col = """Os pontos colaterais são direções intermediárias situadas entre os pontos \
    cardeais na rosa dos ventos. \
    Eles representam direções mais específicas do que os pontos cardeais e \
    são obtidos pela combinação de um ponto cardeal com outro adjacente.  
    Os quatro pontos colaterais são:  
    * :blue[**Nordeste (NE):**] Localizado entre Norte (N) e Leste (L), \
    indicando uma direção que é simultaneamente ao norte e ao leste.  
    * :blue[**Sudeste (SE):**] Encontra-se entre Sul (S) e Leste (L), \
    apontando para uma direção que é ao mesmo tempo ao sul e ao leste.  
    * :blue[**Sudoeste (SO ou SW):**] Posicionado entre Sul (S) e Oeste (O), \
    representando uma direção que é tanto ao sul quanto ao oeste.  
    * :blue[**Noroeste (NO ou NW):**] Situado entre Norte (N) e Oeste (O), \
    indicando uma direção que é ao norte e ao oeste simultaneamente."""

    st.markdown(pontos_col)

    st.markdown("### Rosa dos Ventos")
    rosa_ventos = '''A rosa dos ventos é um diagrama gráfico que mostra as principais \
    direções cardeais e colaterais em relação aos pontos cardeais na superfície terrestre.\
    Ela é usada como uma ferramenta de orientação em mapas, bússolas e cartas náuticas. \
    A rosa dos ventos geralmente possui um formato circular, onde os pontos cardeais \
    (Norte, Sul, Leste e Oeste) estão dispostos nos quatro pontos cardeais da circunferência.'''

    st.markdown(rosa_ventos)

    st.image('image/rosa_dos_ventos.jpg', caption='Rosa dos Ventos')

    st.markdown("Agora que já aprendemos sobre os :blue[**Pontos Cardinais, Pontos \
                Colaterais e sobre a Rosa dos Ventos**], \
            vamos aprender sobre o **mapa** e suas **características**.")

    st.markdown("### O que é um mapa?")
    definicao = """Um mapa é uma representação gráfica e simbólica da superfície da \
        Terra ou de uma parte específica dela. Mapas são ferramentas essenciais na \
        comunicação de informações geoespaciais, mostrando características físicas, \
        políticas, sociais ou outras de uma área geográfica. Eles podem ser usados \
        para diversos propósitos, como navegação, planejamento urbano, análise \
        geográfica, representação de dados estatísticos, entre outros.  
        **Principais características de um mapa:**  
        * :red[**Representação Gráfica:**] Mapas utilizam símbolos, linhas, cores \
        e outros elementos visuais para representar a realidade tridimensional de \
        forma bidimensional.  
        * :red[**Escala:**] Mapas geralmente possuem uma escala que relaciona as \
        dimensões do mapa com as dimensões reais da área representada. Isso \
        permite medir distâncias no mapa e convertê-las para o mundo real. \\
        * :red[**Orientação:**] Mapas indicam a direção, geralmente usando uma \
        bússola, para orientar o observador. \\
        * :red[**Legenda:**] Uma legenda fornece explicações sobre os símbolos, \
        cores e linhas usados no mapa, tornando-o compreensível para o usuário. \\
        * :red[**Projeção:**] Como a Terra é tridimensional e os mapas são \
        bidimensionais, é necessário projetar a superfície curva do planeta em \
        uma superfície plana. Diferentes projeções podem ser usadas para \
        minimizar distorções em diferentes características. \\
        * :red[**Coordenadas:**] Mapas usam coordenadas geográficas (latitude \
        e longitude) para localizar pontos específicos na Terra. \\
        * :red[**Finalidade:**] Mapas são criados para finalidades específicas,\
        como topografia, navegação, análise climática, planejamento urbano, \
        entre outros.""" 

    st.markdown(definicao)

    
if __name__ == "__main__":
    conteudo()