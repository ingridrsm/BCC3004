class Oculos:
    def __init__(self, modelo):
        self.modelo = modelo
    
    def obter_grau(self):
        return self.modelo.obter_grau()

class Modelo:
    def __init__(self, grau):
        self.grau = grau
    
    def obter_grau(self):
        return self.grau.obter_grau()

class Grau:
    def __init__(self, valor):
        self.valor = valor

    def obter_grau(self):
        return self.valor
    
# para acessar o valor do grau do óculos, basta utilizar (oculos.obter_grau())