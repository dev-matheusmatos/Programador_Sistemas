import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime


# Função para gerar QR Code
def gerar_qr_code_pix(valor, chave_pix, descricao):
    dados_pix = f"Valor: {valor}, Chave: {chave_pix}, Descrição: {descricao}"
    url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={dados_pix}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        return resposta.content
    else:
        st.error("Erro ao gerar o QR Code PIX")
        return None


# Função para calcular o valor do estacionamento
def calcular_valor_estacionamento(entrada, saida, taxa_por_hora = 5.00):
    duracao = saida - entrada
    horas = duracao.total_seconds() / 3600
    valor = horas * taxa_por_hora
    return round(valor, 2)


# Função principal
def main():
    st.title("Pagamento")

    st.header("Gerar Pagamento")

    # Entrada dos dados do cliente
    nome_cliente = st.text_input("Nome do Cliente")
    placa_carro = st.text_input("Placa do Carro")
    horario_entrada = st.text_input("Horário de Entrada", placeholder="ex: 08:30")
    horario_saida = st.text_input("Horário de Saída", placeholder="ex: 18:45")

    # Botão para gerar nota fiscal
    if st.button("Gerar Nota Fiscal"):
        if nome_cliente and placa_carro and horario_entrada and horario_saida:
            try:
                # Converter horários para datetime
                entrada = datetime.strptime(horario_entrada, "%H:%M")
                saida = datetime.strptime(horario_saida, "%H:%M")

                if saida > entrada:
                    valor = calcular_valor_estacionamento(entrada, saida)
                    chave_pix = "123e4567-e89b-12d3-a456-426614174000"  # Chave PIX fictícia
                    descricao = f"Pagamento estacionamento - Placa {placa_carro}"

                    st.subheader("Nota Fiscal")
                    st.text(f"Nome: {nome_cliente}")
                    st.text(f"Placa do Carro: {placa_carro}")
                    st.text(f"Horário de Entrada: {entrada.strftime('%H:%M')}")
                    st.text(f"Horário de Saída: {saida.strftime('%H:%M')}")
                    st.text(f"Valor: R$ {valor:.2f}")
                    st.text(f"Descrição: {descricao}")

                    # Gerar QR Code PIX
                    qr_code_url = gerar_qr_code_pix(valor, chave_pix, descricao)
                    st.subheader("QR Code PIX para Pagamento")
                    st.image(qr_code_url)
                else:
                    st.error("Horário de saída deve ser após o horário de entrada.")
            except ValueError:
                st.error("Horário deve estar no formato HH:MM.")
        else:
            st.error("Por favor, preencha todos os campos.")

if __name__ == "__main__":
    main()
