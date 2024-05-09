import os

###################################################
##### Projeto - Locadora de Carros - Versão 4 #####
###################################################



# tetetetetetetetettetetetetetetet

op_pric = ''
while op_pric != '0':
  os.system('clear')
  print("############################################")
  print("######      Locadora de Carros        ######")
  print("############################################")
  print("#####      1 - Módulo Cliente          #####")
  print("#####      2 - Módulo Funcionários     #####")
  print("#####      3 - Módulo Veículos         #####")
  print("#####      4 - Módulo Relatório        #####")
  print("#####      5 - Módulo Reserva          #####")
  print("#####      6 - Módulo Informações      #####")
  print("#####      0 - Sair                    #####")
  op_pric = input("##### Escolha sua opção: ")
    
  if op_pric == '1':
    op_cliente = ''
    while op_cliente != '0':
      os.system('clear')
      print()
      print("#############################################")
      print("#####    Você está no Módulo Cliente    #####")
      print("#############################################")
      print("##### 1 - Cadastrar Cliente             #####")
      print("##### 2 - Exibir Dados do Cliente       #####")
      print("##### 3 - Alterar Dados do Cliente      #####")
      print("##### 4 - Excluir Cliente               #####")
      print("##### 0 - Retornar ao Menu Principal    #####")
      op_cliente = input("##### Escolha sua opção: ")
      print()
      input("Tecle <ENTER> para continuar...")
          
      if op_cliente == '1':
        os.system('clear')
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
        os.system('clear')
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
        os.system('clear')
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
        print("Aluno alterado com sucesso!")
        input("Tecle <ENTER> para continuar...")
  
      elif op_cliente == '4':
        os.system('clear')
        print()
        print("############################################")
        print("#####         Exclui Cliente           #####")
        print("############################################")
        print()
        cpf = input("##### CPF: ")
        print()
        print("Aluno excluído com sucesso!")
        input("Tecle <ENTER> para continuar...")

    
  elif op_pric == '2':
    op_func = ''
    while op_func != '0':
      os.system('clear')
      print()
      print("#############################################")
      print("##### Você está no Módulo Funcionários  #####")
      print("#############################################")
      print("##### 1 - Cadastrar Funcionários        #####")
      print("##### 2 - Exibir Dados do Funcionários  #####")
      print("##### 3 - Alterar Dados do Funcionários #####")
      print("##### 4 - Excluir Funcionário           #####")
      print("##### 0 - Retornar ao Menu Principal    #####")
      resp2 = input("##### Escolha sua opção: ")
      print()
      input("Tecle <ENTER> para continuar...")
      
      if op_func == '1':
        os.system('clear')
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
        print("Aluno cadastrado com sucesso!")
        input("Tecle <ENTER> para continuar...")

      elif op_func == '2':
        os.system('clear')
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
        os.system('clear')
        print()
        print("############################################")
        print("#####    Altera Dados do Funcionário   #####")
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
        print("Aluno alterado com sucesso!")
        input("Tecle <ENTER> para continuar...")

      elif op_func == '4':
        os.system('clear')
        print()
        print("############################################")
        print("#####       Exclui Funcionário         #####")
        print("############################################")
        print()
        cpf = input("##### CPF: ")
        print()
        print("Aluno excluído com sucesso!")
        input("Tecle <ENTER> para continuar...")

  
  elif op_pric == '3':          
    print()
    print("############################################")
    print("#####         Módulo Veículos          #####")
    print("############################################")
    print("##### 1 - Cadastrar Veículo            #####")
    print("##### 2 - Exibir Dados do Veículo      #####")
    print("##### 3 - Alterar Dados do Veículo     #####")
    print("##### 4 - Excluir Veículo              #####")
    print("##### 0 - Retornar ao Menu Principal   #####")
    resp2 = input("##### Escolha sua opção: ")
    print()
    input("Tecle <ENTER> para continuar...")


  elif op_pric == '4':
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
      
    
  elif op_pric == '5':
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
