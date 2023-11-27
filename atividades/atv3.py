#faça uma programa que peça duas notas e de a media de uma aluno
''''
n = float(input("digite uma nota: "))
n1 = float(input("digite outra nota: "))
s = n + n1
print(s)
media = (n + n1) / 2
print(media)
'''
''''
while True:
    saida = input("tecle s para sair").upper()
    if saida == "S":
        break
    n = float(input("digite um numero:"))
    n1 = float(input("digite outro numero: "))
    s = (n + n1) / 2
    print(s)
'''

''''
for numero in range(2):
    numero = float(input("digite a primeira nota: "))
media = numero + numero
s = media / 2
print("o soma das notas é {}, e a media é {}".format(media,s))'
'''

n =  float(input("digite um numero: "))
n1 =  float(input("digite um numero: "))
s = n + n1
m = s / 2
print("a soma das notas é {}, e a media é {}".format(s,m),end = "    ")
print("muito bem!")