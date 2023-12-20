class SmartFhone:
    def __init__(self, marca,):
        self.marca = marca
    
    
    
    @property
    def ver_marca(self):
        return self.marca
    

class CelularIOS(SmartFhone):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

    @property
    def ver_modelo(self):
        return self.modelo
    
    def __str__(self):
        return f'o smartfhone {self.modelo}  é da marca {self.marca} '
    

class CelularAndroid(SmartFhone):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    
    @property
    def ver_modelo(self):
        return self.modelo
    
    def __str__(self):
        return f'o smartfohne {self.modelo} é da marca {self.marca}'






celular = CelularIOS("ifhone", "ifhone15 PRO MAX")

print(celular)

celular2 = CelularAndroid("sansung", "m31")
print(celular2)