import streamlit as st
import mysql.connector

st.set_page_config(
    page_title='Estacionamento',
    page_icon="🚗"
)

st.title('Página de Cadastro')

# Faz a conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='estacionamento2'
)
cursor = conexao.cursor()


# Consulta para verificar vagas disponíveis
def verificar_vagas():
    cursor.execute("SELECT id, vaga_numero FROM vagas WHERE ocupada = 0")
    return cursor.fetchall()


vagas_disponiveis = verificar_vagas()

# Formulário para cadastro do veículo e seleção da vaga
with st.form('form-cadastrar-veiculo', clear_on_submit=True):
    st.header('Informar placa')
    informar_placa = st.text_input('Informe a placa do veiculo', placeholder='Ex: AAA1A11')

    st.header('Selecionar vaga')
    vaga_selecionada = st.selectbox('Selecione a vaga', [vaga[1] for vaga in vagas_disponiveis])

    botao_cadastro = st.form_submit_button('Cadastrar')
    if botao_cadastro:
        if len(informar_placa) == 7:
            try:
                # Inicia uma transação
                conexao.start_transaction()

                # Insere o veículo
                sql_veiculo = "INSERT INTO veiculos (placa_veiculo) VALUES (%s)"
                cursor.execute(sql_veiculo, (informar_placa,))

                # Marca a vaga como ocupada
                sql_vaga = "UPDATE vagas SET ocupada = 1 WHERE vaga_numero = %s"
                cursor.execute(sql_vaga, (vaga_selecionada,))

                # Confirma a transação
                conexao.commit()

                st.success('Veículo cadastrado com sucesso e vaga ocupada!')
            except mysql.connector.Error as err:
                conexao.rollback()
                st.error(f'Erro ao cadastrar veículo ou ocupar vaga: {err}')
        else:
            st.warning('Por favor, preencha a placa corretamente.')

# Fechar a conexão
conexao.close()
