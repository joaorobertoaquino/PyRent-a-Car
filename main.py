import os
from funcoes import (
    menuPrincipal,
    modCliente,
    modFunc,
    modVeic
)

###################################################
##### Projeto - Locadora de Carros - Versão 4 #####
###################################################

op_pric = ''
while op_pric != '0':
  op_pric = menuPrincipal()
  
  if op_pric == '1':
    op_cliente = ''
    while op_cliente != '0':
      op_cliente = modCliente()
          
      if op_cliente == '1':
        os.system("clear")
        print()
        print("#############################################")
        print("#####        Cadastrar Cliente         #####")
        print("#############################################")
        print()
        nome = input("##### Nome: ")
        print()
        cpf = input("##### CPF: ")
        print()
        email = input("##### Email: ")
        print()
        fone = input("##### Celular: ")
        print()
        print("Aluno cadastrado com sucesso!")
        input("Tecle <ENTER> para continuar...")

      elif op_cliente == '2':
        os.system("clear")
        print()
        print("############################################")
        print("#####      Exibe Dados do Cliente      #####")
        print("############################################")
        print()
        print("##### Nome: ")
        print("##### CPF: ")
        print("##### Email: ")
        print("##### Celular: ")
        print()
        input("Tecle <ENTER> para continuar...")

      elif op_cliente == '3':
        os.system("clear")
        print()
        print("############################################")
        print("#####      Altera Dados do Cliente     #####")
        print("############################################")
        print()
        nome = input("##### Nome: ")
        print()
        cpf = input("##### CPF: ")
        print()
        email = input("##### Email: ")
        print()
        fone = input("##### Celular: ")
        print()
        print("Dados alterados com sucesso!")
        input("Tecle <ENTER> para continuar...")
  
      elif op_cliente == '4':
        os.system("clear")
        print()
        print("############################################")
        print("#####         Exclui Cliente           #####")
        print("############################################")
        print()
        nome = input("##### Nome: ")
        print()
        cpf = input("##### CPF: ")
        print()
        print("Aluno excluído com sucesso!")
        input("Tecle <ENTER> para continuar...")

    
  elif op_pric == '2':
    op_func = ''
    while op_func != '0':
      op_func = modFunc()
           
      if op_func == '1':
        os.system("clear")
        print()
        print("#############################################")
        print("#####      Cadastrar Funcionários       #####")
        print("#############################################")
        print()
        nome = input("##### Nome: ")
        print()
        cpf = input("##### CPF: ")
        print()
        email = input("##### Email: ")
        print()
        fone = input("##### Celular: ")
        print()
        print("Funcionário cadastrado com sucesso!")
        input("Tecle <ENTER> para continuar...")

      elif op_func == '2':
        os.system("clear")
        print()
        print("############################################")
        print("#####    Exibe Dados do Funcionário    #####")
        print("############################################")
        print()
        print("##### Nome: ")
        print("##### Idade: ")
        print("##### Email: ")
        print("##### Celular: ")
        print()
        input("Tecle <ENTER> para continuar...")

      elif op_func == '3':
        os.system("clear")
        print()
        print("############################################")
        print("#####   Alterar Dados do Funcionário   #####")
        print("############################################")
        print()
        nome = input("##### Nome: ")
        print()
        cpf = input("##### CPF: ")
        print()
        email = input("##### Email: ")
        print()
        fone = input("##### Celular: ")
        print()
        print("Dados alterados com sucesso!")
        input("Tecle <ENTER> para continuar...")

      elif op_func == '4':
        os.system("clear")
        print()
        print("############################################")
        print("#####       Exclui Funcionário         #####")
        print("############################################")
        print()
        nome = input("##### Nome: ")
        print()
        cpf = input("##### CPF: ")
        print()
        print("Funcionário excluído com sucesso!")
        input("Tecle <ENTER> para continuar...")

  
  elif op_pric == '3':
    op_veic = ''
    while op_veic != 0:
      op_veic = modVeic()

      if op_veic == '1':
        os.system('clear')
        print()
        print("############################################")
        print("#####        Cadastrar Veículo        #####")
        print("############################################")
        modelo = input("##### Modelo: ")
        print()
        ano = input("##### Ano de lançamento: ")
        print()
        cor = input("##### Cor: ")
        print()
        chassi = input("##### Número do Chassi: ")
        print()
        placa = input("##### Número da placa: ")
        print()
        print("Veículo cadastrado com sucesso!")
        input("Tecle <ENTER> para continuar...")

      elif op_veic == '2':
        os.system('clear')
        print()
        print("############################################")
        print("#####    Exibe Dados do Veículo       #####")
        print("############################################")
        print()
        print("##### Modelo: ")
        print("##### Ano de lançamento: ")
        print("##### Cor: ")
        print("##### Número do Chassi: ")
        print("##### Número da placa: ")
        print()
        input("Tecle <ENTER> para continuar...")

      elif op_veic == '3':
        os.system('clear')
        print()
        print("############################################")
        print("#####    Alterar Dados do Veículo      #####")
        print("############################################")
        modelo = input("##### Modelo: ")
        print()
        ano = input("##### Ano de lançamento: ")
        print()
        cor = input("##### Cor: ")
        print()
        chassi = input("##### Número do Chassi: ")
        print()
        placa = input("##### Número da placa: ")
        print()
        print("Dados alterados com sucesso!")
        input("Tecle <ENTER> para continuar...")

      elif op_veic == '4':
        os.system('clear')
        print()
        print("############################################")
        print("#####       Exclui Veículo             #####")
        print("############################################")
        print()
        modelo = input("##### Modelo: ")
        print()
        ano = input("##### Ano de lançamento: ")
        print()
        cor = input("##### Cor: ")
        print()
        chassi = input("##### Número do Chassi: ")
        print()
        placa = input("##### Número da placa: ")
        print()
    
  elif op_pric == '4':
   print()
   print("#############################################")
   print("#####   Você está no Módulo Reserva     #####")
   print("#############################################")
   print("##### 1 - Lista de Veículos Disponíveis #####")
   print("##### 2 - Lista de Preços               #####")
   print("##### 3 - Opções de Seguro              #####")
   print("##### 4 - Formas de Pagamento           #####")
   print("##### 5 - Política de Combustível       #####")
   print("##### 6 - Suporte ao Cliente            #####")
   print("##### 0 - Retornar ao Menu Principal    #####")
   op_pric = input("##### Escolha sua opção: ")
   print()
   input("Tecle <ENTER> para continuar...")

  elif op_pric == '5':
    print()
    print("#############################################")
    print("#####   Você está no Módulo Relatório   #####")
    print("#############################################")
    print("##### 1 - Lista Geral de Clientes       #####")
    print("##### 2 - Lista Geral de Funcionários   #####")
    print("##### 3 - Lista Geral de Veículos       #####")
    print("##### 4 - Lista de Veículos Alugados    #####")
    print("##### 5 - Veículos mais Procurados      #####")
    print("##### 0 - Retornar ao Menu Principal    #####")
    op_pric = input("##### Escolha sua opção: ")
    print()
    input("Tecle <ENTER> para continuar           #####")

  elif op_pric == '6':
    print()
    print("#############################################")
    print("#####  Você está no Módulo Informações  #####")
    print("#############################################")
    print("##### Projeto   -  Locadora de Veículos #####")
    print("##### Desenvolvimento:                  #####")
    print("##### João Roberto Galvão Aquino        #####")
    print("##### E-mail para comunicação:          #####")
    print("##### joao.roberto.galvao.017@gmail.com #####")
    print()
    input("Tecle <ENTER> para continuar...")


print("Você encerrou o programa!")
print("Até logo!")
