#um professor que escolher alguem para apagar o quadro e vai sortear quatro alunos, leia o nome dos alunos e o aluno escolhido
''''
import random
alun1 = input("digite seu nome: ")
print("o primeiro partipante é {} e seu numero para sorteio é {}:".format(alun1,1))
alun2 = input("digite seu nome: ")
print("o segundo participante é {} e seu numero para sorteio é {}:".format(alun2,2))
alun3 = input("digite seu nome: ")
print("o terceiro participante é {} e seu numero para sorteio é {}:".format(alun3,3))
alun4 = input("digite seu nome: ")
print("o quarto participante é {} e seu numero para sorteio é {}:".format(alun4,4))
n = 1
n2 = 2
n3 = 3
n4 = 4
sorteio = random.randint(1,4)
print("=" * 20)
print(input("vamos para o sorteio"))
print("=" * 20)
print("O numero sorteado foi",sorteio,end=" ==== ")

if sorteio == 1:
    print("O aluno {} foi sorteado".format(alun1))
elif sorteio == 2:
    print("O aluno {} foi sorteado".format(alun2))
elif sorteio == 3:
    print("O aluno {} foi sorteado".format(alun3))
else:
    print("O aluno {} foi sorteado".format(alun4))
'''
''''''
import random


alun1 = input("digite seu nome: ")
print("o primeiro partipante é:",alun1)
alun2 = input("digite seu nome: ")
print("o segundo participante é:",alun2)
alun3 = input("digite seu nome: ")
print("o terceiro participante é:",alun3)
alun4 = input("digite seu nome: ")
print("o quarto participante é:",alun4)

lista = [alun1,alun2,alun3,alun4]

sorteio = random.choice(lista)
print("o aluno escolhido foi o",sorteio)