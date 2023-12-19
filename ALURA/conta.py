class Conta:
    

        def __init__(self, titular, senha, saldo= 0 , limite= 1000):
                self.__titular = titular 
                self.__senha = senha 
                self.__saldo = saldo 
                self.__limite = limite

        




        def ver_dados_conta(self):
                print("o nome do titular da conta é", self.__titular)
                print("a senha da conta é", self.__senha)
                print("o sado da conta é ", self.__saldo)
                print("o limite atual da conta é", self.__limite)





        def depositar(self, valor):
                self.__saldo += valor
                print("deposito efetuado")
                
        



        def sacar(self):
                valor = int(input("quanto deseja sacar? "))
                if self.__saldo < valor:
                        print("saldo insuficiente para saque")
                        print("saldo da conta bancaria", conta.__saldo)
                        self.sacar()
                


                else:
                        self.__saldo -= valor
                        print("saque efetuado")
        
        




        def get_saldo(self):
                print(conta.__saldo)





        def get_limite(self):
                print(conta.__limite)





        def set_limite(self, novo_limite):
                self.__limite = novo_limite
                print(novo_limite)
        






conta = Conta("luiz Artur", 96036330,)
conta.depositar(4500.0)
''''
conta.sacar(9000)
conta.set_limite(7000.0)
conta.get_limite()
conta.get_saldo()

conta.set_limite(2000)'''
conta.get_saldo()
conta.sacar()