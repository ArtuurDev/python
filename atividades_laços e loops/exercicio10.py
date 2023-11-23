#faca um progrma que mostre quantas vendas na semana

vendas_s = 0
for i in range(1,8):
    vendas = int(input("quantas vendas hoje: "))
    vendas_s = vendas_s + vendas
print("o total de vendas na semana é: ",vendas_s)