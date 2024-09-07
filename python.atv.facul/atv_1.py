# Suponha que temos 3 filmes por semana, 
# cada filme tem uma faixa etária
# o primeiro é para menores que 12 anos,
# o segundo é para maiores ou iguais a 12 e menores 
# que 18 e o terceiro filme é para maiores
# de ou igual 18 anos.
# Outro ponto solicitado é a respeito
# da disponibilidade de ingressos




idade = int(input('digite sua idade: '))

if idade <12:
    print('recomendandomos o FILME 1')
elif idade >= 12 and idade <18:
    print('recomendamos o FILME 2')
else:
    print('recomendamos o FILME 3')



    

