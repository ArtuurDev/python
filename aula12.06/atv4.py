# crie um cadastro de clientes recebendo nome, idade, data de aniversairo e endereço 
#completo(rua, numero da residencia e bairro). adicione todas as informaçoes em um dicionario. imprima ao final
print("CADASTRO")
print("=" * 20)
lista  = []
n = input("digite seu nome : ")
i = int(input("digite sua idade:"))
a = (input("data de aniversairo: "))
e = input("seu endereço")

dic = {}

dic.update({'nome': n, 'idade':i, 'data':a,'endereço':e})

print(dic)