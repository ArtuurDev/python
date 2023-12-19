class Pessoa:
 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = None

    def __str__(self):
        return f'nome: {self.nome}, idade {self.idade}, e cpf {self.__cpf}'
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, meu_cpf):
        self.__cpf = meu_cpf



pessoa = Pessoa("artur",17,)


print(pessoa)


class Homem(Pessoa):
    pass


class Mulher(Pessoa):
    pass



elvis = Homem("elvis", 28)

print(elvis)


elvis.set_cpf(62240847344)
print(elvis)