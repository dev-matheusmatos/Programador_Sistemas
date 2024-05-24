import streamlit as st
import mysql.connector
# Faz a conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    username='root',
    password='',
    database='estacionamento'
)
cursor = conexao.cursor()
# Titulo do projeto
st.title('Projeto de estacionamento')
# Cria as tabs para separar as telas de um jeito organizado
tab1, tab2, tab3, tab4 = st.tabs(['Cadastrar veiculo', 'Login', 'Visualizar informações', 'Pagar'])
# Começa a tab1 para o cadastro do veiculo
with tab1:
    with st.form('form-cadastrar-veiculo', clear_on_submit=True):
        # Cria os inputs para o usuario informes os dados necessarios
        st.header('Tela cadastro')
        cadastrar_placa = st.text_input('Informe a placa do veiculo', placeholder='Ex: AAA1A11')
        cadastrar_modelo = st.text_input('Informe o modelo', placeholder='Ex: Palio')
        cadastrar_cor = st.text_input('Informe a cor', placeholder='Ex: Vermelho')
        botao_cadastro = st.form_submit_button('Enviar')
        if botao_cadastro:
            # Verifica se todos os campos estão preenchidos
            if botao_cadastro and len(cadastrar_placa) == 7 and cadastrar_modelo != '' and cadastrar_cor != '':
                # Insere os dados na tabela do banco de dados
                cursor.execute("INSERT INTO veiculos (placa_veiculo, modelo, cor) VALUES (%s, %s, %s)",
                               (cadastrar_placa, cadastrar_modelo, cadastrar_cor))
                conexao.commit()
                st.success('Veículo cadastrado com sucesso!')
            else:
                st.warning('Por favor, preencha todos os campos corretamente.')
# Começa a tab2 para o login do veiculo
with tab2:
    with st.form('form-login-veiculo', clear_on_submit=True):
        st.header('Tela login')
        # Cria o input para o usuario informar a placa que ja foi cadastrada no banco
        login_placa = st.text_input('Informe a placa cadastrada', placeholder='Ex: AAA1A11')
        botao_login = st.form_submit_button('Enviar')
        if botao_login:
            # Verifica se a placa existe no banco de dados
            cursor.execute("SELECT * FROM veiculos WHERE placa_veiculo = %s", (login_placa,))
            veiculo = cursor.fetchone()
            if veiculo:
                st.success('Login bem-sucedido!')
                # Aqui você pode redirecionar o usuário para a tela de escolha de vaga
            else:
                st.warning('Placa não encontrada. Por favor, verifique os dados informados.')
# Começa a tab3 para o usuario visualizar os dados cadastrados
with tab3:
    with st.form('form-visualizar-dados', clear_on_submit=True):
        # Cria o input para puxar a placa digita com as informações cadastradas
        st.header('Tela de dados')
        informacoes_veiculo = st.text_input('Informe sua placa para ver seus dados', placeholder='Ex: AAA1A11')
        botao_dados = st.form_submit_button('Enviar')
        if botao_dados:
            # Busca os dados do veículo no banco de dados
            cursor.execute("SELECT * FROM veiculos WHERE placa_veiculo = %s", (informacoes_veiculo,))
            veiculo = cursor.fetchone()
            if veiculo:
                st.write(f"Códico do veiculo: {veiculo[0]}, Placa: {veiculo[1]}, Modelo: {veiculo[2]}, Cor: {veiculo[3]}")
            else:
                st.warning('Placa não encontrada. Por favor, verifique os dados informados.')
# Começa a tab4 para o usuario pagar o estacionamento
with tab4:
    with st.form('form-pagar', clear_on_submit=True):
        # Cria o input para o usuario informar seu códico do veiculo para poder fazer o pagamento do estacionamento
        st.header('Tela de pagamento')
        codico_saida = st.number_input('Informe seu códico do veiculo', 1, 10000)
        botao_pagar = st.form_submit_button('Enviar')
        if botao_pagar and len(codico_saida) == 7:
            st.image('qrcode_openai.png')