import mysql.connector
import streamlit as st

conexao = mysql.connector.connect(
    host='LocalHost',
    username='root',
    password='',
    database='Loja'
)

cursor = conexao.cursor()

sql = 'SELECT * FROM produtos'
cursor.execute(sql)

for linha in cursor.fetchall():
    st.write(linha)



# comando para rodar: cd "Banco de Dados"
# streamlit run conexao_banco_02.py

