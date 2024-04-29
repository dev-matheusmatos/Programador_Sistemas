# 5 Crie um programa que simule as operações básicas de um banco:
# Todas as opções devem funcionar. A conta só é acessada caso seja
# apresentada a senha correta.
# Inicialmente devem ser Solicitado informado nº da Conta e Senha;
# Caso a conta e senha estejam corretos, redireciona para o seguinte menu:
# a.  Consultar saldo
# b.  Pagar conta
# c.   Depositar na conta
# d.  Saque
# e.  Sair
# O programa só deve se encerrar quando for selecionada  a opção SAIR.

senha = '123123'
conta = '0000'
saldo = 1000.42
limite_saldo = 2000.00

while True:
    conta_fornecida = input('Digite a conta:')
    senha_fornecida = input('Digite a senha:')
    if senha == senha_fornecida and conta_fornecida == conta:
        break

while True:
    print('''
[a] Consultar saldo
[b] Pagar conta
[c] Depositar na conta
[d] Saque
[e] Sair
    ''')
    opcao = input('Digite a opção: ').lower()

    if opcao == 'e':
        break
    elif opcao == 'a':
        print(f'Saldo Atual: R$ {saldo}')
    elif opcao == 'b':
        valor_conta = float(input('Valor da Fatura:'))
        if valor_conta > saldo + limite_saldo:
            print('Sem saldo para o pagamento')
        else:
            saldo -= valor_conta
    elif opcao == 'c':
        valor_deposito = float(input('Qual valor deseja depositar:'))
        saldo += valor_deposito
    elif opcao == 'd':
        valor_saque = float(input('Valor do Saque'))
        if valor_saque > saldo + limite_saldo:
            print('Sem saldo para o saque')
        else:
            saldo -= valor_saque
    else:
        print('Opção inexistente')