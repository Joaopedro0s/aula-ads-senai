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