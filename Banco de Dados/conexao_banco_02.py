import mysql.connector
import streamlit as st

conexao = mysql.connector.connect(
    host='',
    username='',
    password='',
    database=''
)

cursor = conexao.cursor()

sql = 'SELECT * FROM produtos'
cursor.execute(sql)

for linha in cursor.fetchall():
    st.write(linha)

D

# comando para rodar: cd "Banco de Dados"
# streamlit run conexa_banco_02.py

