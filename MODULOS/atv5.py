#faça um programa que leia o nome completo de uma pessoa e mostre 
# o nome com todas a letras maisculas
# o nome com todas a sletras minusculas
# quantas caraqteres ao todo sem considerar os espaços
#quantas letras tem o primeiro nome




nome =  input("informe seu nome completo: ").strip()
print("O seu nome em letras maisculas é {}".format(nome.upper()))
print("O seu nome em letras minusculas é {}".format(nome.lower()))
print("a quantidade de letras em seu nome é {}".format(len(nome) - nome.count(" ")))
print(" a quantidade de letras do seu primeiro nome é {}".format(nome.find(" ")))