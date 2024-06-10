import streamlit as st
import mysql.connector

st.set_page_config(
    page_title='Estacionamento ',
    page_icon="🚗"
)

st.title('Página de login')

# Faz a conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='estacionamento'
)
cursor = conexao.cursor()

st.header('Informar placa')
informar_placa = st.text_input('Informe a placa do veiculo', placeholder='Ex: AAA1A11')
col1, col2, col3 = st.columns(3)
tiles = list(range(12))
botoes = list(range(12))
i = 0

with col1:
    for i in range(3):
        tiles[i] = st.container(height=200)
        with tiles[i]:
            botoes[i] = st.button(f'Vaga {i + 1}', key=f'bt-c1-{i}')
        i += 1
with col2:
    for i in range(3):
        tiles[i] = st.container(height=200)
        with tiles[i]:
            botoes[i] = st.button(f'Vaga {i + 4}', key=f'bt-c2-{i}')
        i += 1
with col3:
    for i in range(3):
        tiles[i] = st.container(height=200)
        with tiles[i]:
            botoes[i] = st.button(f'Vaga {i + 7}', key=f'bt-c3-{i}')
        i += 1



botao_enviar = st.button('Enviar')
if botao_enviar and botoes and informar_placa !='':
    cursor.execute('INSERT INTO veiculos(placa_veiculo) VALUES (%s)',(informar_placa,))
    cursor.execute(f'UPDATE vagas set ocupado = TRUE where numero_vaga =  {botoes[i]}')
    cursor.execute('INSERT INTO veiculo_estacionado(placa_veiculo,numero_vaga,hora_entrada) VALUES (%s,%s,current_timestamp())',(informar_placa,botoes[i],))
    conexao.commit()
    st.success(f'Veiculo com a placa {informar_placa} cadastrado com sucesso!')