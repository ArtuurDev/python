# crie abstração para uma super classe funcionario com duas subclasses


class Funcionario:
    def __init__(self, nome, salario, horas_trabalhadas):
        self.salario = float(salario)
        self.horas_trabalhadas = horas_trabalhadas
        self.nome = nome
    




class JovemAprendiz(Funcionario):
    def __init__(self, nome, salario, horas_trabalhadas, idade):
        super().__init__(nome, salario, horas_trabalhadas)
        self.idade = idade 

    def get_idade(self):
        return self.idade
    


    def __str__(self):
        return f'o funcionario {self.nome} tem um salario de {self.salario}, trabalha {self.horas_trabalhadas} e sua idade é {self.idade}'




class Estagiario(Funcionario):
    def __init__(self, nome, salario, horas_trabalhadas, nome_escola):
        super().__init__(nome, salario,horas_trabalhadas)
        self.nome_escola = nome_escola



    def __str__(self):
       return f' o funcionario {self.nome} trabalha {self.horas_trabalhadas} horas e ganha R${self.salario} reais e sua escola é {self.nome_escola}'




    def get_ver_escola(self):
        return self.nome_escola


estagiario = JovemAprendiz("artur", 800, 6, 17 )
print(estagiario)

