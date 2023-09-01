class Estudante:
    
    def __init__(self,nome,idade,notas):
        
        self.nome = nome
        self.idade = idade
        self.notas = [notas]
        
    
    def media(self):
        print(f'A média do aluno é de {sum(self.notas)/len(self.notas)}')
    

class Turma:
    
    def __init__(self):
        self.list_estudantes = []
        
    def adicionaEstudante(self,estudante):
        self.list_estudantes.append(estudante)
        
    def mediaGeral(self):
       for i in range(len(self.list_estudantes)):
           print(i)






        
         
            

