



def cria_conta(titular,senha,saldo):
    conta = {"titular": titular, "senha": senha, "saldo": saldo}
    return conta

def sacar(dados,saque_valor):
    conta["saldo"] -= saque_valor
    return dados
conta = cria_conta("artur", "96036330", 4500.0)

print(sacar(conta, 200.0))