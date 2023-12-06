# CRUD - CREATED, READED, UPDATED, DELETED


dic = {"nome": 'paulo'} # created
dic2 = dict(idade = 23)

dic['nome'] #readed
reading = dic2.get('idade') #readed

dic.update(sobrenome = 'junior') # updated



dic.update({ 'idade': 23})


print(dic)
print(dic2)


dic.clear() #deleted

print('dados do dicionario:', dic)