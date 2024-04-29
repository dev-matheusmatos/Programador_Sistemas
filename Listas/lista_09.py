# x = 'João'
# y = 'Carlos'
#
# x, y = y, x
# print(x)

notas = [4, 6, 8, 2]
pesos = [1, 2, 4, 3]

soma = 0
for i in range(len(notas)):
    soma += notas[i] * pesos[i]

print(soma / 10)
