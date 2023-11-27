# crie um codigo que receba o salario atual de um funcionario, que receba o valor em porcentagem de reajuste e calcule o valor do novo salario reajustado de acordo com o valor de reajuste



salario_atual = float(input("informe seu salario atual:"))
valor_porcentagem = float(input("informe o valor da porcentagem:"))
calculo_porcentagem = salario_atual * valor_porcentagem / 100
valor_novo_salario = salario_atual + calculo_porcentagem 

print("Seu salario atual é {}, o valor da porcentagem adicionada é {:.0f}%, e seu novo salario é {}.".format(salario_atual,valor_porcentagem,valor_novo_salario),  end="")
print("Tenha uma bom dia")