class Aula:
    def disciplina(self, aula: any): # escolhe qual disciplina vai ser ministrada
        aula.ministrar_aula()

class Matematica:
    def ministrar_aula(self):
        ... # aula de matemática

class Biologia:
    def ministrar_aula(self):
        ... # aula de biologia

class Historia:
    def ministrar_aula(self):
        ... # aula de historia