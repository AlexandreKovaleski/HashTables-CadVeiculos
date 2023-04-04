class Veiculo:
    def __init__(self, placa, ano, marca_modelo, cor):
        self.placa = placa
        self.ano = ano
        self.marca_modelo = marca_modelo
        self.cor = cor
    
    def __str__(self):
        return '{} {} {}'.format(self.placa, self.ano, self.marca_modelo, self.cor)
   
    def __repr__(self):
        return '{} {} {}'.format(self.placa, self.ano, self.marca_modelo, self.cor) 