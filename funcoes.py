import os
import pickle
from datetime import datetime
from dicionarios import clientes, funcionarios, veiculos, historico_aluguel
import interfaces as ifc 
from collections import Counter


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

#Clientes
def modCliente():
    ifc.interface_clientes()
    op_cliente = input("=====❱ Escolha sua opção: ") 
    return op_cliente

#Funcionários
def modFunc():
    ifc.interface_funcionarios()
    op_func = input("=====❱ Escolha sua opção: ")
    return op_func

#Veículos   
def modVeic():
    ifc.interface_veiculos()
    op_veic = input("=====❱ Escolha sua opção: ")
    return op_veic

#Reserv
def modReserva():
    ifc.interface_reserva()
    op_reserva = input("=====❱ Escolha sua opção: ")
    return op_reserva



#############################################
#####         Módulo Relatório          #####   
#############################################
def modRelatorio():
    ifc.interface_relatorio()
    op_relatorio = input("=====❱ Escolha sua opção: ")
    return op_relatorio 

def lista_geral_clientes():
    ifc.interface_listaclientes()
    for cpf in clientes:
        print("| %-15s "%(cpf), end='')
        print("| %-35s "%(clientes[cpf][0]), end='')
        print("| %-34s "%(clientes[cpf][1]), end='')
        print("| %-15s "%(clientes[cpf][2]), end='')
        print("| %-20s "%(clientes[cpf][3]), end='')
        print("| %-20s |"%(clientes[cpf][4]))
    print("|-----------------|-------------------------------------|------------------------------------|-----------------|----------------------|----------------------|")
    input("Tecle <ENTER> para continuar...")

def lista_geral_funcionarios():
    ifc.interface_listfucionarios()
    for cpf in funcionarios:
        print("| %-15s "%(cpf), end='')
        print("| %-35s "%(funcionarios[cpf][0]), end='')
        print("| %-34s "%(funcionarios[cpf][1]), end='')
        print("| %-15s "%(funcionarios[cpf][2]), end='')
        print("| %-20s "%(funcionarios[cpf][3]), end='')
        print("| %-20s |"%(funcionarios[cpf][4]))
    print("|-----------------|-------------------------------------|------------------------------------|-----------------|----------------------|----------------------|")
    print()
    input("Tecle <ENTER> para continuar...")

def lista_geral_veiculos():
    os.system('clear' if os.name == 'posix' else 'cls')
    ifc.interface_listaveiculos()
    for placa, dados in veiculos.items():
            print("| %-9s "%placa, end='')
            print("| %-27s "%dados['marca'], end='')
            print("| %-18s "%dados['modelo'], end='')
            print("| %-7s "%dados['ano'], end='')
            print("| %-15s "%dados['cor'], end='')
            print("| %-9s "%dados['categoria'], end='')
            print("| %-16s "%dados['data_cadastro'], end='')
            print("| %-9s |"%dados['hora_cadastro'])
    print("|-----------|-----------------------------|--------------------|---------|-----------------|-----------|------------------|-----------|")
    print()
    input("Tecle <ENTER> para continuar...") 

def veiculos_mais_procurados():
    ifc.interface_maisprocurados()
    contador = Counter()
    for placa, alugueis in historico_aluguel.items():
        contador[placa] += len(alugueis)
        
    top10 = contador.most_common(10)
    for placa, contagem in top10:
        carro = veiculos[placa]
        print("| %-9s "%placa, end='')
        print("| %-27s "%carro['marca'], end='')
        print("| %-8s "%carro['modelo'], end='')
        print("| %-5s "%carro['ano'], end='')
        print("| %-13s "%carro['cor'], end='')
        print("| %-9s "%carro['categoria'], end='')
        print("| %-10s |"%contagem)
        print("|-----------|-----------------------------|----------|-------|---------------|-----------|------------|")
        print()
    input("Tecle <ENTER> para continuar...")

def historicoAlugueis():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    placa = input("❱ Informe a placa do veículo para ver o histórico: ").upper()
    if placa in historico_aluguel:
        ifc.interface_historico()
        for aluguel in sorted(historico_aluguel[placa], key=lambda x: datetime.strptime(x['data_inicio'], "%d/%m/%Y")):  
            hora = '--------------' if aluguel['status'] else aluguel['hora_fim']
            status = 'Ativo' if aluguel['status'] else 'Devolvido'
            print("| %-7s "%placa, end='')
            print("| %-35s "%aluguel['nome_cliente'], end='')
            print("| %-15s "%aluguel['cpf_cliente'], end='')
            print("| %-12s "%aluguel['data_inicio'], end='')
            print("| %-12s "%aluguel['hora_inicio'], end='')
            print("| %-14s "%aluguel['data_fim'], end='')
            print("| %-14s "%hora, end='')
            print("| %-10s |"%status)
    else:
        print("🚫 Não há histórico de aluguéis para este veículo.")
    print("|---------|-------------------------------------|-----------------|--------------|--------------|----------------|----------------|------------|")
    input("\nTecle <ENTER> para continuar...")

##############################################
#####         Módulo Informações         #####    
##############################################
def modInfo():
    ifc.interface_informacoes()
    input("Tecle <ENTER> para voltar ao menu principal...")

