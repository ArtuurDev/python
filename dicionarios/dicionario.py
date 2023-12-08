''''
pessoas = {'nome': 'artur', 'sexo': 'masculino', 'idade': 17  }
print(pessoas)

print(pessoas['nome'])

print("O {} tem {} anos".format(pessoas['nome'],pessoas['idade']))

print(f'O {pessoas['nome']} é do sexo {pessoas['sexo']}')

print(pessoas.keys())

print(pessoas.values())

print(pessoas.items())

for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(k,v)
pessoas['idade'] = 18
print(pessoas)
pessoas['peso'] = 68.00
print(pessoas)

print(f"o {pessoas['nome']} tem {pessoas['idade'] } anos")

'''
lista = []
dic = {'nome': 'artur','idade': '17',
}

dic2 = {'nome2': 'meire', 'idade': '37',
}

lista.append(dic)
lista.append(dic2)
print(lista)