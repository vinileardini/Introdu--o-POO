from class_estudante import Estudante

class Turma:
    
    def __init__(self,listEstudantes):
        self.list_estudantes = listEstudantes
        
        
    def mediaGeral(self):
        media_total = 0
        for estudante in self.list_estudantes:
           media_total += estudante.media()
        return media_total/len(self.list_estudantes)
    


estudante1 = Estudante('Max',22,[9,10,8])
estudante2 = Estudante('Lewis',32,[8,7,8])
estudante3 = Estudante('Fernando',42,[9,8,7])

turma = Turma([estudante1,estudante2,estudante3])

print(f'A média da turma é de {turma.mediaGeral()}')






        
         
            

