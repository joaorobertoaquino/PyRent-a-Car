import os
import pickle
from datetime import datetime, timedelta
from dicionarios import clientes, funcionarios, veiculos, valor_aluguel, historico_aluguel
import interfaces as ifc 
import validacao as val
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


############################################
#####          Módulo Reserva          #####        
############################################
def modReserva():
    ifc.interface_reserva()
    op_reserva = input("=====❱ Escolha sua opção: ")
    return op_reserva

def reservarVeiculo():
    ifc.cabecalhoModulos("Reservar Veículo")
    placa = input("❱ Informe a placa do veículo a ser alugado: ").upper()
    if placa in veiculos and not veiculos[placa]['alugado']:
        dias = int(input("\n❱ Por quantos dias o veículo será alugado? "))
        data_inicio = datetime.now().strftime("%d/%m/%Y")
        hora_inicio = datetime.now().strftime("%H:%M:%S")
        data_fim = (datetime.now() + timedelta(days=dias)).strftime("%d/%m/%Y")
        preco = valor_aluguel[veiculos[placa]['categoria']]
        
        nome_cliente = input("\n❱ 👤 Informe o nome do cliente: ")
        cpf_cliente = input("\n❱ 🆔 CPF do cliente: ")
        cpf_cliente = val.formatar_cpf(cpf_cliente)
        
        if cpf_cliente in clientes:
            if clientes[cpf_cliente][0] == nome_cliente:
                veiculos[placa]['alugado'] = True
                veiculos[placa]['data_inicio'] = data_inicio
                veiculos[placa]['data_fim'] = data_fim
                
                if placa not in historico_aluguel:
                    historico_aluguel[placa] = []
                historico_aluguel[placa].append({
                    'cpf_cliente': cpf_cliente,
                    'nome_cliente': nome_cliente,
                    'data_inicio': data_inicio,
                    'hora_inicio': hora_inicio,
                    'data_fim': data_fim,
                    'hora_fim': None,
                    'status': True
                })
                print("\nPreço da diária: R$ ", preco)
                print(f"\n✅ Veículo {veiculos[placa]['modelo']} alugado com sucesso até {data_fim}!")
            else:
                print("🚫 Nome do cliente não corresponde ao CPF informado.")
        else:
            print("🚫 Cliente não cadastrado.")
    else:
        print("🚫 Veículo não encontrado ou já está alugado.")
    input("\nTecle <ENTER> para continuar...")
    
    
def devolverVeiculo():
    ifc.cabecalhoModulos("Devolver Veículo")
    placa = input("❱ Digite a placa do veículo a ser devolvido: ").upper()
    
    if placa in veiculos and veiculos[placa]['alugado']:
        cpf_cliente = input("❱ CPF do cliente: ")
        cpf_cliente = val.formatar_cpf(cpf_cliente)
        data_fim = datetime.now().strftime("%d/%m/%Y")
        hora_fim = datetime.now().strftime("%H:%M:%S")
        
        devolucao_valida = False
        for aluguel in historico_aluguel[placa]:
            if aluguel['cpf_cliente'] == cpf_cliente and aluguel['status']:
                devolucao_valida = True
                aluguel['data_fim'] = data_fim
                aluguel['hora_fim'] = hora_fim
                aluguel['status'] = False
                veiculos[placa]['alugado'] = False
                break
            
        if devolucao_valida:
            print(f"\n✅ Veículo {veiculos[placa]['modelo']} devolvido com sucesso!")
        else:
            print("\n🚫 CPF não corresponde ao cliente que alugou o veículo.")
    else:
        print("\n🚫 Veículo não encontrado ou não está alugado.")
    input("\nTecle <ENTER> para continuar...")


def veiculosDisponiveis():
    ifc.interface_Veiculosdisponiveis()
    for placa, dados in veiculos.items():
        if not dados ['alugado']:
            print("| %-9s "%placa, end='')
            print("| %-15s "%dados['marca'], end='')
            print("| %-18s "%dados['modelo'], end='')
            print("| %-5s "%dados['ano'], end='')
            print("| %-15s "%dados['cor'], end='')
            print("| %-9s "%dados['categoria'], end='')
            print("| %-18s "%dados['data_cadastro'], end='')
            print("| %-16s |"%dados['hora_cadastro'])
    print("|-----------|-----------------|--------------------|-------|-----------------|-----------|--------------------|------------------|")
    print()
    input("Tecle <ENTER> para continuar...")

def veiculosAlugados():
    ifc.interface_Veiculosalugados()
    for placa, dados in veiculos.items():
        if dados['alugado']:
            print("| %-9s "%placa, end='')
            print("| %-15s "%dados['marca'], end='')
            print("| %-18s "%dados['modelo'], end='')
            print("| %-5s "%dados['ano'], end='')
            print("| %-15s "%dados['cor'], end='')
            print("| %-9s "%dados['categoria'], end='')
            print("| %-19s "%dados['data_inicio'], end='')
            print("| %-20s "%dados['data_fim'], end='')
            if placa in historico_aluguel:
                # Encontrar o registro ativo (status True)
                for aluguel in historico_aluguel[placa]:
                    if aluguel['status']:
                        print("| %-35s |" % aluguel['nome_cliente'])
                        break
                else:
                    print("| %-35s |" % "Nome não encontrado")
            else:
                print("| %-35s |" % "Não Informado")
            
    print("|-----------|-----------------|--------------------|-------|-----------------|-----------|---------------------|----------------------|-------------------------------------|")
    input("Tecle <ENTER> para continuar...")


def politicaCombustivel():
    ifc.interface_Politicacombustivel()
    input("\nTecle <ENTER> para continuar...")

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

