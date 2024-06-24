import streamlit as st
import mysql.connector
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime

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

st.title('Pagamento')

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

                # Registrar hora de saída do veículo
                hora_saida = datetime.now()

                cursor.execute("""
                    UPDATE veiculo_estacionado
                    SET hora_saida = %s
                    WHERE placa_veiculo = %s AND hora_saida IS NULL
                """, (hora_saida, informacoes_veiculo))
                conexao.commit()

                # Formatando hora de saída
                hora_saida_formatada = hora_saida.strftime('%Y-%m-%d %H:%M:%S')
                st.write(f"Hora de Saída: {hora_saida_formatada}")

                # Calcular valor a ser pago
                hora_entrada = estacionamento[1]
                tempo_estacionado = hora_saida - hora_entrada
                horas_estacionado = tempo_estacionado.total_seconds() / 3600
                valor_a_pagar = round(horas_estacionado * 5, 2)

                st.write(f"Tempo estacionado: {horas_estacionado:.2f} horas")
                st.write(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")

                # Gerar QR Code com informações do veículo e da vaga
                dados_qr_code = f"""
Veículo: {veiculo[1]} 

Vaga: {estacionamento[0]} 

Hora de Entrada: {hora_entrada}

Hora de Saída: {hora_saida_formatada}

Valor a Pagar: R$ {valor_a_pagar:.2f}

Chave PIX: 1a887996-985d-4e0d-8b94-85b342f6f208
"""
                qr_code_img = gerar_qr_code_pix(dados_qr_code)
                if qr_code_img:
                    st.image(qr_code_img, caption='QR Code com informações do veículo, vaga e valor a pagar')
            else:
                st.warning('Veículo não está estacionado no momento.')
        else:
            st.warning('Placa não encontrada. Por favor, verifique os dados informados.')

# Fecha o cursor e a conexão com o banco de dados
cursor.close()
conexao.close()
