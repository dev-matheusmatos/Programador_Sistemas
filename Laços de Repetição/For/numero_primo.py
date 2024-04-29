numero = int(input('Informe um número: '))
print()

primos = 0
e_primo = True

for i in range(1, numero + 1):

    for j in range(2, i):

        e_primo = True

        if i % j == 0:
            e_primo = False
            break

    if e_primo:

        print(i)
        primos += 1

print(f'\nA quantidade de número primos até o número {numero} é de {primos}!')
