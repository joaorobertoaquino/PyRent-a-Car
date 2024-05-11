import os

########################################################
#####                Menu Pricipal                 #####
########################################################
def menuPrincipal():
    os.system("clear")
    print("############################################")
    print("######      Locadora de Carros        ######")
    print("############################################")
    print("#####      1 - Módulo Cliente          #####")
    print("#####      2 - Módulo Funcionários     #####")
    print("#####      3 - Módulo Veículos         #####")
    print("#####      4 - Módulo Reserva          #####")
    print("#####      5 - Módulo Relatório        #####")
    print("#####      6 - Módulo Informações      #####")
    print("#####      0 - Sair                    #####")
    op_pric = input("##### Escolha sua opção: ")
    return op_pric
    
###############################################  
#####          Módulo Cliente             #####  
###############################################  
def modCliente():
    os.system("clear")
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
    return op_cliente

def cadastrarCliente():
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

def exibirDadosCliente():
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

def alterarDadosCliente():
    os.system("clear")
    print()
    print("############################################")
    print("#####      Alterar Dados do Cliente    #####")
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

def excluirCliente():
    os.system("clear")
    print()
    print("############################################")
    print("#####         Excluir Cliente          #####")
    print("############################################")
    print()
    nome = input("##### Nome: ")
    print()
    cpf = input("##### CPF: ")
    print()
    print("Aluno excluído com sucesso!")
    input("Tecle <ENTER> para continuar...")
    
############################################### 
#####          Módulo Funcionários        #####        
###############################################    
def modFunc():
    os.system("clear")
    print()
    print("#############################################")
    print("##### Você está no Módulo Funcionários  #####")
    print("#############################################")
    print("##### 1 - Cadastrar Funcionários        #####")
    print("##### 2 - Exibir Dados do Funcionários  #####")
    print("##### 3 - Alterar Dados do Funcionários #####")
    print("##### 4 - Excluir Funcionário           #####")
    print("##### 0 - Retornar ao Menu Principal    #####")
    op_func = input("##### Escolha sua opção: ")
    print()
    input("Tecle <ENTER> para continuar...")
    return op_func

def cadastrarFunc():
    os.system("clear")
    print()
    print("#############################################")
    print("#####      Cadastrar Funcionário        #####")
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

def exibirDadosFunc():
    os.system("clear")
    print()
    print("############################################")
    print("#####   Exibir Dados do Funcionário    #####")
    print("############################################")
    print()
    print("##### Nome: ")
    print("##### Idade: ")
    print("##### Email: ")
    print("##### Celular: ")
    print()
    input("Tecle <ENTER> para continuar...")

def alterarDadosFunc():
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

def excluirFunc():
    os.system("clear")
    print()
    print("############################################")
    print("#####       Excluir Funcionário        #####")
    print("############################################")
    print()
    nome = input("##### Nome: ")
    print()
    cpf = input("##### CPF: ")
    print()
    print("Funcionário excluído com sucesso!")
    input("Tecle <ENTER> para continuar...") 

###########################################
#####         Módulo Veículos         #####         
###########################################
def modVeic():
    os.system('clear')    
    print()
    print("############################################")
    print("#####         Módulo Veículos          #####")
    print("############################################")
    print("##### 1 - Cadastrar Veículo            #####")
    print("##### 2 - Exibir Dados do Veículo      #####")
    print("##### 3 - Alterar Dados do Veículo     #####")
    print("##### 4 - Excluir Veículo              #####")
    print("##### 0 - Retornar ao Menu Principal   #####")
    op_veic = input("##### Escolha sua opção: ")
    print()
    input("Tecle <ENTER> para continuar...")
    return op_veic

def cadastrarVeic():
    os.system('clear')
    print()
    print("############################################")
    print("#####        Cadastrar Veículo         #####")
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

def exibirDadosVeic():
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

def alterarDadosVeic():
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

def excluirVeic():
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
    print("Veículo excluído com sucesso!")
    input("Tecle <ENTER> para continuar...")

############################################
#####          Módulo Reserva          #####        
############################################
def modReserva():
    os.system('clear')
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
    op_reserva = input("##### Escolha sua opção: ")
    print()
    input("Tecle <ENTER> para continuar...")
    return op_reserva

#############################################
#####         Módulo Relatório          #####   
#############################################
def modRelatorio():
    os.system('clear')
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
    op_relatorio = input("##### Escolha sua opção: ")
    print()
    input("Tecle <ENTER> para continuar            #####")
    return op_relatorio 

   
##############################################
#####         Módulo Informações         #####    
##############################################
def modInfo():
    os.system('clear')
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
    input("Tecle <ENTER> para voltar ao menu principal...")