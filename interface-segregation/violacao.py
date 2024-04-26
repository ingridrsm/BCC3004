class Funcionario:
    def __init__(self, nome, funcionario_id):
        self.nome = nome
        self.funcionario_id = funcionario_id
    
    def limpeza(self):
        ... #faz a limpeza do ambiente

    def cozinha(self):
        ... #cozinha os pratos

class Cozinheiro(Funcionario):
    ...

