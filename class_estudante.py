class Estudante:
    
    def __init__(self,nome,idade,notas):
        
        self.nome = nome
        self.idade = idade
        self.notas = notas
    
    def media(self):
       return sum(self.notas)/len(self.notas)
    