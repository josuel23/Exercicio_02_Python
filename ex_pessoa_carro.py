
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.carro = Carro

    def comprar_carro(self, carro):
        self.carro = carro

class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

meucarro = Carro('Hiunday', 'HB20', 'ABC-1234', 2020)
eu = Pessoa ('Josuel', 46)
eu.comprar_carro(meucarro)
print('Meu nome:', eu.nome)
print('Modelo do meu carro:', eu.carro.modelo)
print('Placa do meu carro:', eu.carro.placa)
print('O ano do meu carro é:', eu.carro.ano)