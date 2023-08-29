class Livro:

    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.status = 'Disponível'
    
    def emprestar(self):

        self.status = 'Emprestado'

    
    def devolucao(self):

        self.status = 'Disponível'


class Biblioteca:

    def __init__(self):

        self.livros = []
    
    def livros_disponiveis(self):
        lista_livros_disponiveis = []
        for i in range(len(self.livros)):
            if(self.livros.__getattribute__ == 'status'):
                lista_livros_disponiveis.append()
        