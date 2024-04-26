class Aula:
    def disciplina(self, num): # escolhe qual disciplina vai ser ministrada
        if num == 1:
            self.matematica()
        if num == 2:
            self.biologia()
        if num == 3:
            self.historia()

    def matematica(self):
        ... # aula de matemática
    
    def biologia(self):
        ... # aula de biologia

    def historia(self):
        ... # aula de história