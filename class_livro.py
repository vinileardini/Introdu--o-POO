class Livro:

    def __init__(self,titulo,autor,status="Disponivel"):
        self.titulo = titulo
        self.autor = autor
        self.status = status
    
    def emprestar(self):

        self.status = 'Emprestado'

    
    def devolucao(self):

        self.status = 'Disponivel'