#faça um programa que pergunte a quantidade km percorridos por um carro alugado e a quantidade de dias pelo qual ele foi alugado
#calcule o o preço a pagar sabendo que o dia custa 60 reais e 0.15 por km rodado
preço_por_dia = 60
preço_por_km = 0.15  
dias = float(input("quantos dias o  carro foi alugado? "))
km_r = float(input("quantos quilometros foi percorrido? "))

print("o preço a pagar é {}".format((dias * preço_por_dia) + (km_r * preço_por_km)))