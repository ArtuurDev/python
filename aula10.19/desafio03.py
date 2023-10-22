# crie um codigo que receba o salario atual de um funcionario, que receba o valor em porcentagem de reajuste e calcule o valor do novo salario reajustado de acordo com o valor de reajuste



salario_atual = float(input("informe seu salario atual:"))
valor_porcentagem = float(input("informe o valor da porcentagem:"))
calculo_porcentagem = salario_atual * valor_porcentagem / 100
valor_novo_salario = salario_atual + calculo_porcentagem 

print(salario_atual)
print(valor_porcentagem)
print(calculo_porcentagem)
print("seu novo salario é:", valor_novo_salario)