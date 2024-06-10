import streamlit as st
import mysql.connector
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title='Estacionamento',
    page_icon="🚗"
)


# Função para gerar QR Code usando a API do goqr.me
def gerar_qr_code_pix(dados):
    url = f"https://api.qrserver.com/v1/create-qr-code/?size=350x350&data={dados}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return Image.open(BytesIO(resposta.content))
    else:
        st.error("Erro ao gerar o QR Code")
        return None


# Faz a conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='estacionamento'
)

cursor = conexao.cursor()

st.title('Página dos dados')

with st.form('form-visualizar-dados', clear_on_submit=True):
    # Cria o input para puxar a placa digitada com as informações cadastradas
    informacoes_veiculo = st.text_input('Informe a placa cadastrada', placeholder='Ex: AAA1A11')
    botao_dados = st.form_submit_button('Gerar QR Code')

    if botao_dados:
        # Busca os dados do veículo no banco de dados
        cursor.execute("SELECT * FROM veiculos WHERE placa_veiculo = %s", (informacoes_veiculo,))
        veiculo = cursor.fetchone()

        if veiculo:
            st.write(f"Código do veículo: {veiculo[0]}")
            st.write(f"Placa cadastrada: {veiculo[1]}")

            # Busca a vaga em que o veículo está estacionado
            cursor.execute("""
                SELECT veiculo_estacionado.numero_vaga, veiculo_estacionado.hora_entrada
                FROM veiculo_estacionado
                WHERE veiculo_estacionado.placa_veiculo = %s
                ORDER BY veiculo_estacionado.hora_entrada DESC LIMIT 1
            """, (informacoes_veiculo,))
            estacionamento = cursor.fetchone()

            if estacionamento:
                st.write(f"Vaga: {estacionamento[0]}")
                st.write(f"Hora de Entrada: {estacionamento[1]}")

                # Gerar QR Code com informações do veículo e da vaga
                dados_qr_code = f"Veículo: {veiculo[1]}, Vaga: {estacionamento[0]}"
                qr_code_img = gerar_qr_code_pix(dados_qr_code)
                if qr_code_img:
                    st.image(qr_code_img, caption='QR Code com informações do veículo e da vaga')
            else:
                st.warning('Veículo não está estacionado no momento.')
        else:
            st.warning('Placa não encontrada. Por favor, verifique os dados informados.')

# Fecha o cursor e a conexão com o banco de dados
cursor.close()
conexao.close()
