import requests

cep = '89020220'

dados = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
dados = dados.json()

print()

for chave, valor in dados.items():
    print(f'{chave} --- {valor}')

