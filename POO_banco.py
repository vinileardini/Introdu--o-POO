class Conta:

    def __init__(self,titular,saldo):
        
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self,deposito):

        self.deposito = deposito
        print(f'O depósito de R${self.deposito} foi creditado a sua conta')
        print(f'O saldo atual da conta é de R${self.saldo + self.deposito}')
        self.saldo = self.saldo+self.deposito
    
    def sacar(self,saque):

        self.saque = saque
        print(f'Saque efetuado no valor de R${saque}')
        print(f'O saldo atual da conta R${self.saldo - self.saque}')
        self.saldo = self.saldo - self.saque
    
    def transferir(self,valor_transferencia,favorecido):

        self.valor_transferencia = valor_transferencia
        self.favorecido = favorecido

        print(f'A transferência de valor R${self.valor_transferencia} foi realizada para {self.favorecido}')

        self.saldo = self.saldo-self.valor_transferencia

        print(f'Saldo atual da conta é R${self.saldo}')


        
exemploConta = Conta('Steve',100)
exemploConta.depositar(50)
exemploConta.sacar(30)
exemploConta.transferir(65,'Bill')


