# aprendendo interpolçao
# crie um codigo que receba um salario, que receba  o valor em porcentagem de reajuste e calcule o novo salario

salario = float(input("informe seu salario:"))
porcentagem = float(input("informe a porcentagem:"))
                
print(f'seu novo salario é {salario * porcentagem / 100 + salario}')                