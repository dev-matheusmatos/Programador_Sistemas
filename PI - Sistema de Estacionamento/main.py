import streamlit as st
import mysql.connector

st.set_page_config(
    page_title='Estacionamento ',
    page_icon="🚗"
)

with open(".\style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title('Estacionamento')

# Faz a conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='estacionamento'
)
cursor = conexao.cursor()

st.header('Informar placa')
informar_placa = st.text_input('Informe a placa do veículo', placeholder='Ex: AAA1A11')
col1, col2, col3 = st.columns(3)

# Consulta SQL para selecionar vagas não ocupadas
cursor.execute('SELECT numero_vaga FROM vagas WHERE vaga_ocupada = FALSE')
vagas_disponiveis = cursor.fetchall()

lista_botoes = []
colunas = [col1, col2, col3]
var_controle = 0

for vaga in vagas_disponiveis:
    with colunas[var_controle]:
        lista_botoes.append(st.button(f'Vaga {vaga[0]}', key=f'{vaga[0]}'))
    var_controle = (var_controle + 1) % 3

if not 'indice_botao' in st.session_state:
    st.session_state['indice_botao'] = 0

for botao in lista_botoes:
    if botao:
        st.session_state['indice_botao'] = lista_botoes.index(botao)
        st.write(f'Vaga selecionada: {vagas_disponiveis[st.session_state["indice_botao"]][0]}')

valor_indice = 1
botao_enviar = st.button('Enviar')

if botao_enviar and informar_placa != '':
    try:
        # Verifica se a vaga está ocupada antes de inserir o veículo
        cursor.execute('SELECT vaga_ocupada FROM vagas WHERE numero_vaga = %s', (vagas_disponiveis[st.session_state["indice_botao"]][0],))
        ocupado = cursor.fetchone()[0]

        if not ocupado:
            # Inserção na tabela veiculos
            cursor.execute('INSERT INTO veiculos(placa_veiculo) VALUES (%s)', (informar_placa,))
            # Atualização da vaga para ocupado
            cursor.execute('UPDATE vagas SET vaga_ocupada = TRUE WHERE numero_vaga = %s', (vagas_disponiveis[st.session_state["indice_botao"]][0],))
            # Inserção na tabela veiculo_estacionado
            cursor.execute(
                'INSERT INTO veiculo_estacionado(placa_veiculo, numero_vaga, hora_entrada) VALUES (%s, %s, current_timestamp())',
                (informar_placa, vagas_disponiveis[st.session_state["indice_botao"]][0],))
            conexao.commit()
            st.success(
                f'Veículo com a placa {informar_placa} cadastrado na vaga {vagas_disponiveis[st.session_state["indice_botao"]][0]} com sucesso!')
        else:
            st.warning(f'A vaga {vagas_disponiveis[st.session_state["indice_botao"]][0]} está ocupada.')
    except mysql.connector.Error as err:
        st.error(f"Erro no banco de dados: {err}")

# Fechamento da conexão com o banco de dados
conexao.close()
