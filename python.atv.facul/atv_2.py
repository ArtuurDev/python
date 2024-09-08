# Precisamos criar um programa que seja capaz de percorrer todos of filmes 
# (Filme 1, Filme 2, Filme 3, Filme 4 e Filme 5)
# e para cada filme termos a nota de 1 a 5. 
# note que é importante sempre deixar uma forma da pessoa encerrar o 
# programa caso queira




lista_nota_filmes = {'homem aranha': 0, 'a freira': 0, 'picapau': 0, 'ta chovendo hamburguer': 0, 'deadpool': 0}

for filme in lista_nota_filmes:
    nota = float(input(f'de uma nota para o {filme}: '))
    lista_nota_filmes[filme] = nota
    if filme == 4:
        break
    else:
        saida = int(input('deseja sair encerrar? 0 para sim 1 para não:'))
        if (saida == 0):
            break
        
        else:
            continue
print(lista_nota_filmes)