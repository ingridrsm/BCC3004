class Atendente:
    def __init__(self, nome, atendente_id, horas):
        self.nome = nome
        self.atendente_id = atendente_id
        self.horas = horas

class SalarioMes:
    def salario_mes(horas): # calcula o salario do atendente
        salario = 80*horas
        return salario

class RelatorioPagamento: # faz o relatorio do mês do funcionário
    def relatorio(atendente):
        total = SalarioMes.salario_mes(atendente.horas)
        return f'O salário recebido pelo atendente {atendente.nome} foi de {total} reais, por trabalhar por {atendente.horas} horas'