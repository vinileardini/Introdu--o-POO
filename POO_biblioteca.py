from class_livro import Livro

class Biblioteca:

    def __init__(self,livros):

        self.livros = livros
    
    def livros_disponiveis(self):
        lista_livros_disponiveis = []
        for livro in self.livros:
            if livro.status == 'Disponivel':
                lista_livros_disponiveis.append(livro.titulo)
        return lista_livros_disponiveis
    

livro1 = Livro('Senhor do anéis','J. R. R. Tolkien')
livro2 = Livro('O Hobbit','J. R. R. Tolkien')
livro3 = Livro('Jogador N°1','Ernest Cline')

livrosBiblioteca = Biblioteca([livro1,livro2,livro3])


livro2.emprestar()

livrosDisponiveis = livrosBiblioteca.livros_disponiveis()

print(livrosDisponiveis)
        