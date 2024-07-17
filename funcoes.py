
import pickle
import interfaces as ifc 
from dicionarios import clientes, veiculos, historico_aluguel, funcionarios

########################################################
#####            Escrever Arquivos                 #####
########################################################
def escreverArquivos():
    arq_clientes = open("clientes.dat", "wb")
    pickle.dump(clientes, arq_clientes)
    arq_clientes.close()

    arq_funcionarios = open("funcionarios.dat", "wb")
    pickle.dump(funcionarios, arq_funcionarios)
    arq_funcionarios.close()

    arq_veiculos = open("veiculos.dat", "wb")
    pickle.dump(veiculos, arq_veiculos)
    arq_veiculos.close()

    arq_historico_aluguel = open("historico_aluguel.dat", "wb")
    pickle.dump(historico_aluguel, arq_historico_aluguel)
    arq_historico_aluguel.close()

########################################################
#####                Menu Pricipal                 #####
########################################################
def menuPrincipal():
    ifc.interface_principal()
    op_pric = input("=====❱ Escolha sua opção: ")
    return op_pric

##################################### 
#####          Menus            #####  
##################################### 

#Módulo Clientes
def modCliente():
    ifc.interface_clientes()
    op_cliente = input("=====❱ Escolha sua opção: ") 
    return op_cliente

#Módulo Funcionários
def modFunc():
    ifc.interface_funcionarios()
    op_func = input("=====❱ Escolha sua opção: ")
    return op_func

#Módulo Veículos   
def modVeic():
    ifc.interface_veiculos()
    op_veic = input("=====❱ Escolha sua opção: ")
    return op_veic

#Módulo Reserva
def modReserva():
    ifc.interface_reserva()
    op_reserva = input("=====❱ Escolha sua opção: ")
    return op_reserva

#Módulo Relatórios
def modRelatorio():
    ifc.interface_relatorio()
    op_relatorio = input("=====❱ Escolha sua opção: ")
    return op_relatorio 

#Módulo Informações
def modInfo():
    ifc.interface_informacoes()
    input("Tecle <ENTER> para voltar ao menu principal...")

