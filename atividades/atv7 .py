#faça um programa que leia a altura e a largura de um parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta la
#sabendo que um litro de tinta pinta 2m**


a = float(input("digite a altura em metros: "))
l = float(input("digite a largura metros: "))
print("a area desse quadrado é {:.2f} m², sao necessarios {:.2f} litros de tinta para {:.2f} m² de area dessa parede".format(a * l,a * l / 2, a * l))

