# sempre que criar uma classe em python deve separar os metodos por categoria
# ordem: get, set, comuns

class Automovel:
    def _init_(self, placa, cor):
        self.placa = placa
        self.cor = cor
    
    def get_placa(self):
        return self.placa
    
    def get_cor(self):
        return self.cor
    
    def set_cor(self, nova_cor):
        self.cor = nova_cor

    def velocidade(self, velocidade):
        print(f'Eu estava dirigindo a {velocidade} Km/h')

# Instâncias
carro = Automovel('TYT-0000', 'azul')
moto = Automovel('WMS-1570', 'preta')
caminhao = Automovel('CHB-2684', 'vermelho')

carro.velocidade(10000)

