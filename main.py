from banco import Banco
from cliente import Cliente
from conta import Conta_corrente, Conta_poupanca

banco = Banco()

cliente_1 = Cliente('Yure', 20)
cliente_2 = Cliente('Levi', 3)
cliente_3 = Cliente('Aline', 18)

conta_1 = Conta_corrente(1111, 123451, 0)
conta_2 = Conta_corrente(2222, 123452, 0)
conta_3 = Conta_poupanca(3333, 123453, 0)

cliente_1.inserir_conta(conta_1)
cliente_2.inserir_conta(conta_2)
cliente_3.inserir_conta(conta_3)

banco.inserir_cliente(cliente_1)
banco.inserir_conta(conta_1)

if banco.autenticar(cliente_1):
    cliente_1.conta.deposito(40)
    cliente_1.conta.sacar(20)

else:
    print('Cliente não autenticado')