# leia o preço de um produto e mostre com 5%  de desconto


p = float(input("digite o preço do produto que deseja comprar: "))
d = float(input("quantos por cento de desconto? "))
print("liquidaçao de {}%  de desconto em qualquer produto")
print("o valor do produto é {}, e com desconto fica {}".format(p, -p * d / 100 + p))