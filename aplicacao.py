import os
import time
from Veiculo import Veiculo
from HashTable import HashTable

print("Bem Vindo ao Sistema de Cadastro de Placas - Tabela Hash \n" 
    "Desenvolvido por Alexandre Kovaleski Fochi \n"
    "Disciplina de Estritura de Dados Avançada \n"
    "Prof. Me. Fahad Kalil \n\n")
    
hashtable = HashTable()

cadastro = True

while cadastro == True:

    print("==============================MENU============================== \n\n"
        "Esolha Sua Opção: \n\n"
        "1 - Inserir Placa \n"
        "2 - Verificar Placa \n"
        "3 - Remover Placa \n"
        "4 - Ver Todas Placas \n"
        "0 - Sair \n\n")
    opcao = input()
    
    print("Carregando ...")
    time.sleep(2)
    os.system("cls") 

    if opcao == "1":
        placa = input("Imforme a placa do veículo: ")
        renavam = input("Informe o renavan do veiculo: ")
        marca = input("Informe a marca do veiculo: ")
        modelo = input("Informe o modelo do veículo: ")
        cor = input("Informe a cor do veiculo: ")
        anoFabr = input("Informe o ano de fabricação do veículo: ")
        
        print("Cadastrando ...")
        time.sleep(2)
        print("Veiculo cadastrado com sucesso")
        time.sleep(2)
        os.system("cls")
        
        veiculo = Veiculo(placa, renavam, marca, modelo, cor, anoFabr)
        hashtable.__setitem__(veiculo.placa, veiculo.__str__())
        
    if opcao == "2":
        placa = input("Informe a Placa: ")
        print(hashtable.get(placa))