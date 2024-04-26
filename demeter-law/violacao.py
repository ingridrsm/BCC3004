class Oculos:
    def __init__(self, modelo):
        self.modelo = modelo

class Modelo:
    def __init__(self, grau):
        self.grau = grau

class Grau:
    def __init__(self, valor):
        self.valor = valor

# para acessar o valor do grau do óculos, várias dependencias foram criadas (oculos.modelo.grau.valor)