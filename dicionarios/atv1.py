#Faça um programa que leia nome e média de um aluno, 
#guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.








cont = 0
contn = 0
nome = input("digite seu nome:")
for i in range(4):
    contn +=1
    n = int(input(f"digite nota {contn}: "))
    cont += n 
    nota = cont / 4
    dic = {"nome": nome, "media": nota}

print()
print(f"a media final do aluno {dic["nome"]} foi: {dic["media"]}")
if dic["media"] <= 5:
    print(f"{dic["nome"]} está reprovado")
    situação = "reprovado"
    dic['situaçao'] = situação
elif dic["media"] > 5 and dic["media"] < 7:
    print(f"{dic['nome']} está de recuperaçao")
    situação = "recuperaçao"
    dic["situaçao"] = situação
else:
    print(f'{dic["nome"]} está aprovado')
    situação = "aprovado"
    dic['situação'] = situação
    print("boas ferias!!")
print(dic)