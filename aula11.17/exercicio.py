contador = 0

while contador < 20:
    aluno =int(input("digite sua idade:"))
    if aluno > 13:
        print(f'o aluno {contador} tem mais de 13 anos')
    if aluno <13:
        print(f'o aluno{contador}nao tem mais de 13 anos')
    contador += 1
    
