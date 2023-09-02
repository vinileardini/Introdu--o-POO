from class_produto import Produto

class Loja:

    def __init__(self,produtos):

        self.produtos = produtos
        
    def valor_inventario(self):
        valor_total = 0
        for produto in self.produtos:
            valor_total += produto.preco * produto.quantidade
        return valor_total

p1 = Produto('lapis',2,50)
p2 = Produto('borracha',4,30)
p3 = Produto('caneta',5,20)

loja = Loja([p1,p2,p3])

valor_estoque = loja.valor_inventario()

print(valor_estoque)

p1.comprar(10)

venda = loja.valor_inventario()

print(venda)






        






            
                
                
                
                
            
            
            
            

            

