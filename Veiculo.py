class Veiculo:
    def __init__(self, placa, renavam, marca, modelo, cor, anoFabr):
        self.placa = placa
        self.renavam = renavam
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.anoFabr = anoFabr
    
    def __str__(self):
        return 'Placa: {} \nRenavam: {} \nMarca: {} \nModelo: {} \nCor: {} \nAno de Fabricação: {}'.format(self.placa, self.renavam, self.marca, self.modelo, self.cor, self.anoFabr)
   
    def __repr__(self):
        return 'Placa: {} \nRenavam: {} \nMarca: {} \nModelo: {} \nCor: {} \nAno de Fabricação: {}'.format(self.placa, self.renavam, self.marca, self.modelo, self.cor, self.anoFabr)