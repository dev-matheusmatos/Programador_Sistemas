import streamlit as st
import mysql.connector

# Função para conectar ao banco de dados MySQL
def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="estacionamento"
        )
        return conn
    except mysql.connector.Error as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para verificar o status das vagas no estacionamento
def verificar_vagas(conn):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vagas")
            vagas = cursor.fetchall()
            return vagas
        except mysql.connector.Error as e:
            st.error(f"Erro ao executar a consulta: {e}")
            return None

# Função para atualizar o status de uma vaga
def atualizar_vaga(conn, vaga, status):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE vagas SET status = %s WHERE numero = %s", (status, vaga))
            conn.commit()
        except mysql.connector.Error as e:
            st.error(f"Erro ao atualizar vaga: {e}")

# Função para registrar a entrada de um carro
def registrar_entrada(conn, vaga, nome, placa):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO clientes (vaga, nome, placa) VALUES (%s, %s, %s)", (vaga, nome, placa))
            conn.commit()
            atualizar_vaga(conn, vaga, "ocupada")
            st.success("Entrada registrada com sucesso!")
        except mysql.connector.Error as e:
            st.error(f"Erro ao registrar entrada: {e}")

# Função para registrar a saída de um carro
def registrar_saida(conn, vaga):
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE clientes SET hora_saida = CURRENT_TIMESTAMP() WHERE vaga = %s AND hora_saida IS NULL", (vaga,))
            conn.commit()
            atualizar_vaga(conn, vaga, "vaga livre")
            st.success("Saída registrada com sucesso!")
        except mysql.connector.Error as e:
            st.error(f"Erro ao registrar saída: {e}")

# Página principal
def main():
    conn = conectar_bd()
    if conn is not None:
        st.title("Sistema de Estacionamento")
        vagas = verificar_vagas(conn)

        if vagas is not None:
            st.write("Vagas Disponíveis:")
            for vaga in vagas:
                st.write(f"Vaga {vaga[0]} - {vaga[1]}")

            vaga_selecionada = st.selectbox("Selecione a vaga desejada:", [vaga[0] for vaga in vagas])

            if st.button("Registrar Entrada"):
                nome = st.text_input("Nome do Cliente:")
                placa = st.text_input("Placa do Carro:")
                registrar_entrada(conn, vaga_selecionada, nome, placa)

            if st.button("Registrar Saída"):
                registrar_saida(conn, vaga_selecionada)

# Executar o aplicativo
if __name__ == "__main__":
    main()
