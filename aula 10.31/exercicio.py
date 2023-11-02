# Escreva um programa que leia a distância em Km e a quantidade de litros
# de combustível consumidos por um carro em um percurso qualquer. Calcule 
# o consumo em Km/l e escreva uma mensagem de acordo com a relação 
# abaixo:

km = float(input("informe a quantidade de km percorridos:"))
litros = float(input("informe quantidade de litros gastos:"))
consumo = km / litros

if consumo < 8:
    print("venda o carro")
elif consumo >= 8 and consumo <= 14:
    print("economico")
elif consumo > 14:
    print("super economico")
else:
    print("erro consumo")
    

