import streamlit as st


st.set_page_config(
    page_title="Professor de Taekwondo",
    page_icon='🥋',
    layout="centered",
    initial_sidebar_state="expanded")

st.logo("arquivos/logo.png", size = 'large') 

paginas = {
    "LTC - Lee Taekwondo Clube": [
        st.Page("paginas/mate56-inicial.py", title="Conheça nossa escola", icon = '', default = True), 
    ], 

    "Aplicativos para os Alunos": [
        st.Page("paginas/mate56-chatbot.py", title="TaekwonBot", icon='🥋'), 
    ],
}

pg = st.navigation(paginas)
pg.run()
  
