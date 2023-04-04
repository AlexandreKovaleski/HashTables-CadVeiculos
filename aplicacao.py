import os
import time
from Definitions import HashTable, Veiculo

print("Bem Vindo ao Sistema de Cadastro de Placas - Tabela Hash \n" 
      "Desenvolvido por Alexandre Kovaleski Fochi \n"
      "Disciplina de Estritura de Dados Avançada \n"
      "Prof. Me. Fahad Kalil \n\n"
      "==============================MENU============================== \n\n")


hashtable = HashTable
cadastro = True

print("Esolha Sua Opção: \n\n"
      "1 - Inserir Placa \n"
      "2 - Verificar Placa \n"
      "3 - Remover Placa \n"
      "4 - Ver Todas Placas \n"
      "0 - Sair \n\n")

opcao = input()
print("Carregando ...")
time.sleep(1.5)
os.system("cls") 

