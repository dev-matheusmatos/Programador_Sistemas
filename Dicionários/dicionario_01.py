# dicionario = {'Jonas': 32,
#               'Matheus': 27,
#               'Gabriel': 29}
#
# print(dicionario['Gabriel'])

estoque_sangue = {'A+': 30,
                  'A-': 25,
                  'AB+': 40,
                  'AB-': 15}

# completo
print(estoque_sangue.items())

for chave, valor in estoque_sangue.items():
    print(f'{chave} ---- {valor}')

# somente valores
print(estoque_sangue.values())

for valor in estoque_sangue.values():
    print(valor)

# somente as chaves
print(estoque_sangue.keys())

for chave in estoque_sangue.keys():
    print(chave)
