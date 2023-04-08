import os
import time
from Veiculo import Veiculo
from HashTable import HashTable

os.system("cls")

print("Bem Vindo ao Sistema de Cadastro de Placas - Tabela Hash \n" 
    "Desenvolvido por Alexandre Kovaleski Fochi \n"
    "Disciplina de Estritura de Dados Avançada \n"
    "Prof. Me. Fahad Kalil \n\n")

time.sleep(5)
os.system("cls")
            
hashtable = HashTable()

cadastro = True

while cadastro == True:

    print("==============================MENU============================== \n\n"
        "Esolha Sua Opção: \n\n"
        "1 - Inserir Placa \n"
        "2 - Consultar Placa \n"
        "3 - Remover Placa \n"
        "4 - Ver Todas Placas \n"
        "0 - Sair \n\n")
    opcao = input()
    
    print("Carregando ...")
    time.sleep(2)
    os.system("cls") 

    if opcao == "1":
        print("==========================CADASTRO========================== \n\n")
        placa = input("Informe a placa do veículo: ")
        renavam = input("Informe o renavan do veiculo: ")
        marca = input("Informe a marca do veiculo: ")
        modelo = input("Informe o modelo do veículo: ")
        cor = input("Informe a cor do veiculo: ")
        anoFabr = input("Informe o ano de fabricação do veículo: ")
        
        print("\nCadastrando ...")
        time.sleep(2)
        print("Veiculo cadastrado com sucesso")
        time.sleep(2)
        os.system("cls")
        
        veiculo = Veiculo(placa, renavam, marca, modelo, cor, anoFabr)
        hashtable.__setitem__(veiculo.placa, veiculo.__str__())
        
    elif opcao == "2":
        print("==========================CONSULTAR========================== \n\n")
        placa = input("Informe a Placa: ")
        print("\nBuscando...")
        time.sleep(2)
        os.system("cls")
        print(hashtable.__getitem__(placa))
        
    elif opcao == "3":
        print("===========================REMOVER=========================== \n\n")
        placa = input("Informe a Placa: ")
        print("\nRemovendo placa...")
        time.sleep(2)
        os.system("cls")
        hashtable.delete(placa)
    
    elif opcao == "4":
        print("==========================VER TODAS========================== \n\n")
        print("\nBuscando...")
        time.sleep(2)
        os.system("cls")
        hashtable.showAll()
       
    elif opcao == "0":
        print("\nNunca é um adeus...")
        time.sleep(4)
        exit()
        
    else:
        print("Entrada inválida, tente novamente")