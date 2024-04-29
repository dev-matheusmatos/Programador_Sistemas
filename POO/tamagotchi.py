class Tamagotchi:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.xp = 100
        self.fome = 0
        self.cansaco = 0
        self.higiene = 100

    def caminhar(self, distancia):
        self.higiene -= 10
        self.cansaco += distancia / 10
        self.xp += distancia / 10
        self.fome += distancia / 5

    def mostrar_atributos(self):
        return {'XP': self.xp,
                'Fome': self.fome,
                'Cansaço': self.cansaco,
                'Higiene': self.higiene}

    def comer(self):
        if self.fome <= 0:
            return 'Sem fome'
        self.fome -= 5
        self.higiene -= 2
        self.xp += 1

    def apresentar(self):
        return f'Oi! Eu sou um {self.tipo}, mas pode me chamar de {self.nome}'


tamagotchi = Tamagotchi('', '')