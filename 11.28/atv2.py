#escreva uma funçao chmada gorjeta que receba o
#valor da conta de um restaurante calcule e exiba a gorjeta do harcom considerando 12% do valor da conta



def gorgeta():

    receita = float(input("digite a receita do restaurante: "))
    g = receita * 12 / 100
    print("a receita do restaurante é {}, e a gorjeta do garçon é {}".format(receita,g))