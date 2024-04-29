class Veiculo:
    def __init__(self, marca, modelo, cor, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.placa = placa

    def ligar(self):
        print(f'{self.modelo} está ligado!')


veiculo1 = Veiculo('Hyundai', 'Tucson',
                   'Prata', 2012, 'MKE-0E09')
veiculo2 = Veiculo('Chevrolet', 'Astra',
                   'Preto', 2007, 'MEI-8308')

print(veiculo1.cor)
print(veiculo2.cor)
veiculo1.ligar()
veiculo2.ligar()



