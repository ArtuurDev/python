class Televisao:
    def _init_(self, tamanho):
        self.tamanho = tamanho
        self.canal = None
        self.ligada = False

    def get_tamanho(self):
        return self.tamanho
    
    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
    
    def get_canal(self):
        if self.ligada == False:
            self.canal = None
        return self.canal
    
    def set_canal(self, muda_canal):
        if self.ligada == False:
            print('Ligue a Televisão para poder mudar de canal')
        else:
            
            self.canal = muda_canal
    
    def get_ligada(self):
        if self.ligada == True:
            print('Ligada')
        elif self.ligada == False:
            print('Desligada')

    def ligar(self):
        self.ligada = True
    
    def desligar(self):
        self.ligada = False
    
    def _str_(self):
        return f'O tamanho da Televisão é {self.get_tamanho()}, está no canal {self.get_canal()}. A Televisão está {self.get_ligada()}'

tv = Televisao('32 polegadas')
# tv.ligar()
tv.set_canal(32)

print(tv)