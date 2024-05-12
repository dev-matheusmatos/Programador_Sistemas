import streamlit as st
import mysql.connector
from funcoes import validar_cpf
from datetime import datetime

conn = mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='barbas'
)

cursor = conn.cursor()

tab1, tab2, tab3 = st.tabs(['+ Barbeiro', '+ Cliente', '+ Agenda'])

with tab1:
    with st.form('novo-barbeiro', clear_on_submit=True):
        st.header('Cadastrar Barbeiro')
        novo_barbeiro = st.text_input('Nome: ')
        cadastrar_novo_barbeiro = st.form_submit_button('Cadastrar')
        if cadastrar_novo_barbeiro and novo_barbeiro != "":
            sql = 'INSERT INTO barbeiros (nome) VALUES (%s)'
            dados = (novo_barbeiro,)
            cursor.execute(sql, dados)
            conn.commit()
            st.success(f'Barbeiro {novo_barbeiro} cadastrado', icon="✅")

with tab2:
    with st.form('novo-cliente', clear_on_submit=True):
        st.header('Cadastrar Cliente')
        novo_cliente = st.text_input('Nome:')
        novo_cliente_cpf = st.text_input('CPF:')
        cadastrar_novo_cliente = st.form_submit_button('Cadastrar')
        if cadastrar_novo_cliente and novo_cliente != "" and len(novo_cliente_cpf) == 14:
            if validar_cpf(novo_cliente_cpf):
                sql = 'INSERT INTO clientes (nome, cpf) VALUES (%s, %s)'
                dados = (novo_cliente, novo_cliente_cpf)
                cursor.execute(sql, dados)
                conn.commit()
                st.success(f'Cliente {novo_cliente} cadastrado', icon="✅")
            else:
                st.text('CPF Inválido!')


with tab3:
    with st.form('novo-agendamento', clear_on_submit=True):
        st.header('Agendamento')
        cpf = st.text_input('Informe seu CPF:')
        data_escolhida = st.date_input('Selecione uma data:', datetime.today())
        horario_escolhido = st.time_input('Selecione um horário:')
        barbeiro = st.selectbox('Selecione o Barbeiro:', [])
        agendar = st.form_submit_button('Agendar')
