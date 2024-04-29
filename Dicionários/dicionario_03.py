linguagens = {'Python': 1991,
              'Fortran': 1950,
              'Java': 1991,
              'C#': 2002}

print(linguagens)
linguagens['PHP'] = 1994
print(linguagens)
linguagens['PHP'] = 1993
print(linguagens)
linguagens.update({'Cobol': 1954})
print(linguagens)

chave = 'Assembly'

if print(linguagens.get(chave)) is None:
    print(f'O termo {chave} não foi encontrado!')
