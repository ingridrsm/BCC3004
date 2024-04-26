class Atendente:
    def __init__(self, nome, atendente_id, horas):
        self.nome = nome
        self.atendente_id = atendente_id
        self.horas = horas

    def salario_mes(self): # calcula o salario do atendente
        salario = 80*self.horas
        return salario
    
    def relatorio_pagamento(self): # faz o relatorio do mês do funcionário
        total = self.salario_mes()
        return f'O salário recebido pelo atendente {self.nome} foi de {total} reais, por trabalhar por {self.horas} horas'