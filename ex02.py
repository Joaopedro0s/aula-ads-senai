class Pessoa:
    def __init__(self, nome=None, idade=None): # Função construtora
        if nome is None:
            nome = input("Digite seu nome: ")
        if idade is None:
            idade = int(input("Digite sua idade: "))
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print("Olá", self.nome, "|", self.idade, "anos") 

pessoa1 = Pessoa()
pessoa1.apresentar()
aluna = Pessoa("Ana", 21)
aluna.apresentar()