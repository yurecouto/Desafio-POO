# DESAFIO POO
## Desafio de programação orientada a objetos em Python. // Python object-oriented programming challenge.

Na pasta "SOLUÇÃO" está a solução dos professores o seguinte desafio:
//
In the "SOLUÇÃO" folder there's the teachers soluction the following challenge:

- 

Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)

//

Exercise with Abstraction, Inheritance, Encapsulation and Polymorphism
Create a banking system (extremely simple) that has customers, accounts and
a bank. The idea is that the customer has an account (savings or checking) and that
can withdraw / deposit into that account. Checking accounts have an extra limit. Bank
has customers and accounts.

Tips:
Create Customer class that inherits from the Person class (Inheritance)
    Person has name and age (with getters)
    Customer TEM account (Aggregation of the class ContaCorrente or ContaPoupanca)
Create ContaPoupanca and ContaCurrente classes that inherit from Conta
    Current Account must have an extra limit
    Accounts have branch, account number and balance
    Accounts must have a deposit method
    Conta (super class) must have the abstract withdrawal method (Abstraction and
    polymorphism - the subclasses that implement the withdraw method)
Create Bank class to AGGREGATE customer and account classes (Aggregation)
Bank will be responsible for authenticating the customer and the accounts as follows:
    Bank has accounts and customers (Aggregation)
    * Check if the branch is from that bank
    * Check if the customer is from that bank
    * Check if the account belongs to that bank
It will only be possible to withdraw if you pass the bank authentication (described above)
