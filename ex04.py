class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
    def mostrar_saldo(self):
        print("Seu saldo é:", self.__saldo)
    def mostrarTitular(self):
        print("Correntista:", self.__titular)

conta = ContaBancaria("Ana")
conta.depositar(5000)
conta.sacar(1400)
conta.mostrar_saldo()
conta.mostrarTitular()