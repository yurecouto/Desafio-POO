from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = list()
        self.numero = list()
        self.saldo = list()

    def deposito(self, valor):
        self.saldo += valor

    def detalhes(self):
        print(f'Agencia: {self.agencia} \nNumero: {self._numero} \nSaldo: {self.saldo}')

    @abstractmethod
    def sacar(self, valor): pass

class Conta_corrente(Conta):
    def __init__(self):
        pass