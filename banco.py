class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = list()
        self.contas = list()
    
    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def inserir_conta(self, conta):
        self.contas.append(conta)

    