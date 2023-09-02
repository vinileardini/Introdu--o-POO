class Produto:

    def __init__(self,nome,preco,quantidade):
        
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def comprar(self,quantidadeCompra):
        self.quantidadeCompra = quantidadeCompra

        self.quantidade = self.quantidade - self.quantidadeCompra

    def vender(self,quantidadeEstoque):

        self.quantidadeEstoque = quantidadeEstoque

        self.quantidade = self.quantidade + self.quantidadeEstoque
    