from tamagotchi import tamagotchi
import streamlit as st

st.title('Bichinho Virtual')
col1, col2 = st.columns(2)
with col1:
    nome = st.text_input('Nome do Tamagotchi')
    tipo = st.radio('Modelo',['Tigre','Coelho', 'Dinossauro'])

with col2:
    st.subheader('Tamagotchi!')
    if nome != '':
        tamagotchi.nome = nome
        tamagotchi.tipo = tipo
        st.write(tamagotchi.apresentar())
        col2_1,col2_2, col2_3, col2_4 = st.columns(4)
        with col2_1:
            st.metric('XP',tamagotchi.xp)
        with col2_2:
            st.metric('Higiene',tamagotchi.higiene)
        with col2_3:
            st.metric('Fome',tamagotchi.fome)
        with col2_4:
            st.metric('Cansaço', tamagotchi.cansaco)

        caminhar = st.button('Caminhar')
        if caminhar:
            tamagotchi.caminhar(100)