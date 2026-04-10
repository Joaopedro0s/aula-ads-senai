class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Depósito de", valor, "efetuado")
        else:
            print("Valor inválido para depósito") 
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                print("Saque de R$", valor, "efetuado")
            else:
                print("Saldo insuficiente para o saque")
        else:
            print("Valor de saque incorreto")
    def mostrarSaldo(self):
        status = "Devendo ao banco." if self.__saldo < 0 else "Em dia"
        print("Saldo RS$", self.__saldo, "-", status)
    def getTitular(self):
        return self.__titular
    
class Banco:
    def __init__(self):
        self.correntistas = []
    def abrirConta(self):
        nome = input("Digite seu nome: ")
        conta = ContaBancaria(nome)
        self.correntistas.append(conta)
        print("Conta aberta com sucesso!!")
    def encontrarConta(self, nome):
        for conta in self.correntistas:
            if conta.getTitular() == nome:
                return conta
        return None
    def depositarFundos(self):
        nome = input("Digite o nome do titular: ")
        conta = self.encontrarConta(nome)
        if conta:
            try:
                valor = float(input("Digite o depósito: "))
                conta.depositar(valor)
            except ValueError:
                print("Entrada de valor inválido")
        else:
            print("Correntista não encontrado")
    def sacarFundos(self):
        nome = input("Digite o nome do titular: ")
        conta = self.encontrarConta(nome)
        if conta:
            try:
                valor = float(input("Digite o valor de saque: "))
                conta.sacar(valor)
            except ValueError:
                print("Valor de saque inválido")
        else:
            print("Correntista não encontrado")
    def mostrarSaldoCorrentista(self):
        nome = input("Digite o nome do titular: ")
        conta = self.encontrarConta(nome)
        if conta:
            conta.mostrarSaldo()
        else:
            print("Correntista não encontrado")
    def listarContas(self):
        if not self.correntistas:
            print("Nenhuma conta encontrada") 
            return
        print("Lista de correntistas:")
        for conta in self.correntistas:
            print(conta.getTitular(), "Saldo de R$", conta.mostrarSaldo())

def main():
    banco = Banco()
    while True:
        print("\n --- Menu Bancário ---")
        print("1. Abrir conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Mostrar Saldo")
        print("5. Listar Correntistas")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            banco.abrirConta()
        elif opcao == '2':
            banco.depositarFundos()
        elif opcao == '3':
            banco.sacarFundos()
        elif opcao == '4':
            banco.mostrarSaldoCorrentista()
        elif opcao == '5':
            banco.listarContas()
        elif opcao == '6':
            print("Encerrando o sistema bancário")
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente")
main()