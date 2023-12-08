# Crie uma tupla preenchida com os 5 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
#na ordem de colocação. Depois mostre:
#  a) Os 2 primeiros times.
#  b) Os últimos 2 colocados.
#  c)  Times em ordem alfabética. 
#  d)  Em que posição está o time do flamengo.

tupla = ('palmeiras', 'atletico mg', 'flamengo', 'bragantino', 'botafogo')
tupla1 = (tupla[0:2])
tupla2 = (tupla[3:])
tupla3 = sorted(tupla)
tupla4 = (tupla.index('flamengo')) + 1
print("os dois primeiros times sao {}, os dois ultimos sao {}, os time em ordem alfabetica é {}, e a posiçao do flamengo é {}º ".format(tupla1,tupla2,tupla3,tupla4))

