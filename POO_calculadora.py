class Calculadora:
    
    def __init__ (self,entrada1:int,entrada2:int):
        
        self.entrada1 = entrada1
        self.entrada2 = entrada2
    
    def somar(self):
        print(f'A soma de {self.entrada1} e {self.entrada2} é = {self.entrada1 + self.entrada2} ')
    
    def subtrair(self):
        print(f'A subtração de {self.entrada1} e {self.entrada2} é = {self.entrada1  - self.entrada2}')
    
    def multiplicar(self):
        print(f'A multiplicação entre {self.entrada1} e {self.entrada2} é = {self.entrada1 * self.entrada2}')
        
    def dividir(self):
        print(f'A divisão entre {self.entrada1} e {self.entrada2} é = {self.entrada1 / self.entrada2}')


calculo = Calculadora(4,2)

calculo.somar()
calculo.multiplicar()
calculo.subtrair()
calculo.dividir()