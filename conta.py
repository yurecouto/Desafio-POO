from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def detalhes(self):
        print(f'Agencia: {self.agencia} \nNumero: {self.conta} \nSaldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor): 
        pass


class Conta_poupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Seu saldo é insuficiente.')
            return
        
        self.saldo -= valor
        self.detalhes()


class Conta_corrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
        
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Seu saldo é insuficiente.')
            return
        
        self.saldo -= valor
        self.detalhes()
        