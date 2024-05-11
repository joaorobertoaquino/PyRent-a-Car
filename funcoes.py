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

########################################################  
#####               Módulo Cliente                 #####  
########################################################  
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


######################################
#####     Cadastrar Cliente      #####
###################################### 





########################################################
#####              Módulo Funcionários             #####
########################################################    
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

########################################################
#####               Módulo Veículos                #####
########################################################
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

#######################################################
#####                Módulo Reserva               #####
#######################################################




######################################################
#####             Módulo Informações             #####
######################################################