import os
import pickle
from datetime import datetime, timedelta
from dicionarios import clientes, funcionarios, veiculos, alugueis_por_veiculo, valor_aluguel, historico_aluguel
from interface import(
    interface_principal,
    interface_clientes,
    interface_funcionarios,
    interface_veiculos,
    interface_reserva,
    interface_relatorio,
    interface_historico,
    interface_informacoes,
    interface_Veiculosalugados,
    interface_Veiculosdisponiveis,
    interface_Politicacombustivel
)



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

    arq_alugueis_por_veiculo = open("alugueis_por_veiculo.dat", "wb")
    pickle.dump(alugueis_por_veiculo, arq_alugueis_por_veiculo)
    arq_alugueis_por_veiculo.close()

    arq_historico_aluguel = open("historico_aluguel.dat", "wb")
    pickle.dump(historico_aluguel, arq_historico_aluguel)
    arq_historico_aluguel.close()

########################################################
#####                Menu Pricipal                 #####
########################################################
def menuPrincipal():
    interface_principal()
    op_pric = input("##### Escolha sua opção: ")
    return op_pric

###############################################  
#####          Módulo Clientes            #####  
############################################### 
def modCliente():
    interface_clientes()
    op_cliente = input("##### Escolha sua opção: ") 
    return op_cliente

def cadastrarCliente():
    os.system('clear' if os.name == 'posix' else 'cls')
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
    dataNascimento = input("##### Data de nascimento (00/00/0000): ")
    print()
    data = datetime.now()
    clientes[cpf] = [nome,email,fone,dataNascimento, data.strftime("%x, %X")]
    print("Cliente cadastrado com sucesso!")
    input("Tecle <ENTER> para continuar...")

def exibirDadosCliente():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####     Exibir Dados do Cliente      #####")
    print("############################################")
    print()
    cpf = input('Qual o CPF do cliente? ')
    if cpf in clientes:
        print("##### Nome: ", clientes[cpf][0])
        print("##### CPF: ", cpf)
        print("##### Email: ", clientes[cpf][1])
        print("##### Celular: ", clientes[cpf][2])
        print("##### Data de Nascimento: ", clientes[cpf][3])
    else:
        print('Cliente inexistente!')
    print()
    input("Tecle <ENTER> para continuar...")

def alterarDadosCliente():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####      Alterar Dados do Cliente    #####")
    print("############################################")
    print()
    cpf = input('Qual o CPF do Cliente? ')
    if cpf in clientes:
        dadosCliente = clientes[cpf]
        print("Informe os novos dados ou deixe o campo em branco para não alterar a informação.")
        nome = input(f"##### Nome ({dadosCliente[0]}): ").strip()
        email = input(f"##### Email ({dadosCliente[1]}): ").strip()
        fone = input(f"##### Celular ({dadosCliente[2]}): ").strip()
        dataNascimento = input(f"##### Data de Nascimento ({dadosCliente[3]}): ").strip()
        # Atualiza apenas os campos que não estão vazios, permitindo que a informação anterior continue a mesma.
        if nome:
            clientes[cpf][0] = nome
        if email:
            clientes[cpf][1] = email
        if fone:
            clientes[cpf][2] = fone
        if dataNascimento:
            clientes[cpf][3] = dataNascimento

        print('\nDados alterados com sucesso!')
    else:
        print('\nCliente inexistente!')
    
    input("Tecle <ENTER> para continuar...")

def excluirCliente():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####         Excluir Cliente          #####")
    print("############################################")
    print()
    cpf = input('Informe o CPF do cliente: ')
    if cpf in clientes:
        print("##### Nome: ", clientes[cpf][0])
        print("##### Email: ", clientes[cpf][1])
        print("##### Celular: ", clientes[cpf][2])
        print("##### Data de Nascimento: ", clientes[cpf][3])
        print()
        resp = input('Tem certeza que deseja excluir este cliente (Sim/Não)?')
        if resp.upper() == 'SIM':
            del clientes[cpf]
            print("Aluno excluído com sucesso!")
        else:
            print('Exclusão não realizada!')
    else:
        print('Cliente inexistente!')
    input("Tecle <ENTER> para continuar...")
    

############################################### 
#####          Módulo Funcionários        #####        
###############################################    
def modFunc():
    interface_funcionarios()
    op_func = input("##### Escolha sua opção: ")
    return op_func

def cadastrarFunc():
    os.system('clear' if os.name == 'posix' else 'cls')
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
    dataNascimento = input("##### Data de Nascimento (00/00/0000): ")
    print()
    data = datetime.now()
    funcionarios[cpf] = [nome,email,fone,dataNascimento,data.strftime("%x, %X")]
    print("Funcionário cadastrado com sucesso!")
    input("Tecle <ENTER> para continuar...")

def exibirDadosFunc():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####   Exibir Dados do Funcionário    #####")
    print("############################################")
    print()
    cpf = input('Qual o CPF do funcionário(a)? ')
    if cpf in funcionarios:
        print("##### Nome: ", funcionarios[cpf][0])
        print("##### CPF: ", cpf)
        print("##### Email: ", funcionarios[cpf][1])
        print("##### Celular: ", funcionarios[cpf][2])
        print("##### Data de Nascimento: ", funcionarios[cpf][3])
    else:
        print('Funcionário(a) inexistente!')
    print()
    input("Tecle <ENTER> para continuar...")

def alterarDadosFunc():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####   Alterar Dados do Funcionário   #####")
    print("############################################")
    print()
    cpf = input('Qual o CPF do funcionário(a)? ')
    if cpf in funcionarios:
        dadosFuncionarios = funcionarios[cpf]
        print("Informe os novos dados ou deixe o campo em branco para não alterar a informação.")
        nome = input(f"##### Nome ({dadosFuncionarios[0]}: )").strip()
        email = input(f"##### Email ({dadosFuncionarios[1]}): ").strip()
        fone = input(f"##### Celular ({dadosFuncionarios[2]}): ").strip()
        dataNascimento = input(f"##### Data de Nascimento ({dadosFuncionarios[3]}): ").strip()
        # Atualiza apenas os campos que não estão vazios, permitindo que a informação anterior continue a mesma.
        if nome:
            funcionarios[cpf][0] = nome
        if email:
            funcionarios[cpf][1] = email
        if fone:
            funcionarios[cpf][2] = fone
        if dataNascimento:
            funcionarios[cpf][3] = dataNascimento
        
        print('\nDados alterados com sucesso!')
    else:
        print('\nFuncionário(a) inexistente!')

    input("Tecle <ENTER> para continuar...")

def excluirFunc():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####       Excluir Funcionário        #####")
    print("############################################")
    print()
    cpf = input('Informe o CPF do funcionário(a): ')
    if cpf in funcionarios:
        print("##### Nome: ", funcionarios[cpf][0])
        print("##### Email: ", funcionarios[cpf][1])
        print("##### Celular: ", funcionarios[cpf][2])
        print("##### Data de Nascimento: ", funcionarios[cpf][3])
        print()
        resp = input('Tem certeza que deseja excluir este funcionário(a)? (Sim/Não)')
        if resp.upper() == 'SIM':
            del funcionarios[cpf]
            print("Funcionário(a) excluído com sucesso!")
        else:
            print('Exclusão não realizada!')
    else:
        print("Funcionário inexistente!")
    input("Tecle <ENTER> para continuar...") 


###########################################
#####         Módulo Veículos         #####         
###########################################
def modVeic():
    interface_veiculos()
    op_veic = input("##### Escolha sua opção: ")
    return op_veic

def cadastrarVeic():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####        Cadastrar Veículo         #####")
    print("############################################")
    print()
    marca = input("##### Marca: ")
    print()
    modelo = input("##### Modelo: ")
    print()
    ano = input("##### Ano de lançamento: ")
    print()
    cor = input("##### Cor: ")
    print()
    placa = input("##### Número da placa: ").upper()
    print()
    categoria = input("##### Informe a categoria do carro: ")
    print()
    data = datetime.now()
    veiculos[placa] = {
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'cor': cor,
        'categoria': categoria,
        'data_cadastro': data.strftime("%d/%m/%Y"),
        'hora_cadastro': data.strftime("%H:%M:%S"),
        'alugado': False,
        'historico_aluguel': []
    }
    print(f"Veículo {modelo} cadastrado com sucesso!")
    input("Tecle <ENTER> para continuar...")

def exibirDadosVeic():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####    Exibir Dados do Veículo       #####")
    print("############################################")
    print()
    placa = input("Digite a placa do veículo: ").upper()
    if placa in veiculos:
        dados = veiculos[placa]
        print(f"##### Marca: {dados['marca']}")
        print(f"##### Modelo: {dados['modelo']}")
        print(f"##### Ano: {dados['ano']}")
        print(f"##### Cor: {dados['cor']}")
        print(f"##### Categoria: {dados['categoria']}")
        print(f"##### Cadastro: {dados['data_cadastro']} às {dados['hora_cadastro']}")
        print(f"##### Alugado: {'Sim' if dados['alugado'] else 'Não'}")
        if dados['alugado']:
            print(f"##### Data de Início: {dados['data_inicio']}")
            print(f"##### Data de Fim: {dados['data_fim']}")
    else:
        print("Veículo não encontrado.")
    input("\nPressione Enter para voltar ao menu...")



def alterarDadosVeic():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####    Alterar Dados do Veículo      #####")
    print("############################################")
    print()
    placa = input('Informe a placa do veículo: ').upper()
    respExcluirDados = input("Deseja mesmo continuar com essa ação (Sim / Não)? ")
    if respExcluirDados.upper() == 'SIM':
        if placa in veiculos:
            veiculo = veiculos[placa]
            print("Deixe o campo em branco para não alterar a informação.")
            marca = input(f"Marca ({veiculo['marca']}): ") or veiculo['marca']
            modelo = input(f"Modelo ({veiculo['modelo']}): ") or veiculo['modelo']
            ano = input(f"Ano ({veiculo['ano']}): ") or veiculo['ano']
            cor = input(f"Cor ({veiculo['cor']}): ") or veiculo['cor']
            categoria = input(f"Categoria ({veiculo['categoria']}): ") or veiculo['categoria']

            veiculos[placa].update({
                'marca': marca,
                'modelo': modelo,
                'ano': ano,
                'cor': cor,
                'categoria': categoria
            })
            print(f"Dados do veículo {modelo} atualizados com sucesso!")
        else:
            print("Veículo não encontrado!")
    else:
        print("Ação não concluída!")

    input("Tecle <ENTER> para continuar...")


def excluirVeic():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####       Excluir Veículo            #####")
    print("############################################")
    print()
    placa = input('Informe a placa do veículo: ').upper()
    respExcluir = input("Deseja mesmo completar essa ação (Sim / Não)? ")
    if respExcluir.upper() == 'SIM':
        if placa in veiculos:
            del veiculos[placa]
            print(f"Veículo com placa {placa} excluído com sucesso!")
        else:
            print("Veículo não encontrado.")
    else:
        print("Ação não concluída!")
    input("Tecle <ENTER> para continuar...")


############################################
#####          Módulo Reserva          #####        
############################################
def modReserva():
    interface_reserva()
    op_reserva = input("##### Escolha sua opção: ")
    return op_reserva

def reservarVeiculo():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####        Reservar Veículo          #####")
    print("############################################")
    print()
    placa = input("Informe a placa do veículo a ser alugado: ").upper()
    if placa in veiculos and not veiculos[placa]['alugado']:
        dias = int(input("\nPor quantos dias o veículo será alugado? "))
        data_inicio = datetime.now().strftime("%d/%m/%Y")
        data_fim = (datetime.now() + timedelta(days=dias)).strftime("%d/%m/%Y")
        preco = valor_aluguel[veiculos[placa]['categoria']]

        veiculos[placa]['alugado'] = True
        veiculos[placa]['data_inicio'] = data_inicio
        veiculos[placa]['data_fim'] = data_fim

        nome_cliente = input("\nInforme o nome do cliente: ")
        cpf_cliente = input("\nCPF do cliente: ")
        historico_aluguel[placa] = {
            'cpf_cliente': cpf_cliente,
            'nome_cliente': nome_cliente,
            'data_fim': data_fim,
            'status': True
        }

        print("\nPreço da diária: R$ ", preco)
        print(f"\nVeículo {veiculos[placa]['modelo']} alugado com sucesso até {data_fim}!")
    else:
        print("Veículo não encontrado ou já está alugado.")
    input("\nTecle <ENTER> para continuar...")

def devolverVeiculo():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####        Devolver Veículo          #####")
    print("############################################")
    print()
    placa = input("Digite a placa do veículo a ser devolvido: ").upper()

    if placa in veiculos and veiculos[placa]['alugado']:
        
        cpf_cliente = input("CPF do cliente: ")
        data_fim = datetime.now().strftime("%d/%m/%Y")
        veiculos[placa]['alugado'] = False

        historico_aluguel[placa] = {
            'cpf_cliente': cpf_cliente,
            'data_fim': data_fim,
            'status': False
        }

        print(f"Veículo {veiculos[placa]['modelo']} devolvido com sucesso!")
    else:
        print("Veículo não encontrado ou não está alugado.")

    input("Tecle <ENTER> para continuar...")


def veiculosDisponiveis():
    interface_Veiculosdisponiveis()
    for placa, dados in veiculos.items():
        if not dados ['alugado']:
            print("| %-9s "%placa, end='')
            print("| %-27s "%dados['marca'], end='')
            print("| %-18s "%dados['modelo'], end='')
            print("| %-15s "%dados['ano'], end='')
            print("| %-15s "%dados['cor'], end='')
            print("| %-9s "%dados['categoria'], end='')
            print("| %-18s "%dados['data_cadastro'], end='')
            print("| %-16s |"%dados['hora_cadastro'])
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|-----------|--------------------|------------------|")
    print()
    input("Tecle <ENTER> para continuar...")

def veiculosAlugados():
    interface_Veiculosalugados()
    for placa, dados in veiculos.items():
        if dados['alugado']:
            print("| %-9s "%placa, end='')
            print("| %-27s "%dados['marca'], end='')
            print("| %-18s "%dados['modelo'], end='')
            print("| %-15s "%dados['ano'], end='')
            print("| %-15s "%dados['cor'], end='')
            print("| %-9s "%dados['categoria'], end='')
            print("| %-19s "%dados['data_inicio'], end='')
            print("| %-20s "%dados['data_fim'], end='')
            if placa in historico_aluguel:
                print("| %-35s |" %historico_aluguel[placa]['nome_cliente'])
            else:
                print("| %-35s |" % "Não Informado")
            
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|-----------|---------------------|----------------------|-------------------------------------|")
    print()
    input("Tecle <ENTER> para continuar...")


def politicaCombustivel():
    interface_Politicacombustivel()
    input("\nTecle <ENTER> para continuar...")

#############################################
#####         Módulo Relatório          #####   
#############################################
def modRelatorio():
    interface_relatorio()
    op_relatorio = input("##### Escolha sua opção: ")
    return op_relatorio 

def lista_geral_clientes():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("##############################################################################################################################################################")
    print("#######################                                            Lista Geral de Clientes                                             #######################")
    print("##############################################################################################################################################################")
    print("|-----------------|-------------------------------------|------------------------------------|-----------------|----------------------|----------------------|")
    print("|       CPF       |            Nome Completo            |               E-mail               |     Celular     |  Data de Nascimento  |   Data do Cadastro   |")
    print("|-----------------|-------------------------------------|------------------------------------|-----------------|----------------------|----------------------|")
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
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("##########################################################################################################################################################")
    print("#######################                                        Lista Geral de Funcionários                                         #######################")
    print("##########################################################################################################################################################")
    print("|-------------|-------------------------------------|------------------------------------|-----------------|----------------------|----------------------|")
    print("|     CPF     |            Nome Completo            |               E-mail               |     Celular     |  Data de Nascimento  |   Data do Cadastro   |")
    print("|-------------|-------------------------------------|------------------------------------|-----------------|----------------------|----------------------|")
    for cpf in funcionarios:
        print("| %-9s "%(cpf), end='')
        print("| %-35s "%(funcionarios[cpf][0]), end='')
        print("| %-34s "%(funcionarios[cpf][1]), end='')
        print("| %-15s "%(funcionarios[cpf][2]), end='')
        print("| %-20s "%(funcionarios[cpf][3]), end='')
        print("| %-20s |"%(funcionarios[cpf][4]))
    print("|-------------|-------------------------------------|------------------------------------|-----------------|----------------------|----------------------|")
    print()
    input("Tecle <ENTER> para continuar...")

def lista_geral_veiculos():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("###############################################################################################################################################")
    print("#######################                                    Lista Geral de Veículos                                      #######################")
    print("###############################################################################################################################################")
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|-----------|------------------|-----------|")
    print("|   Placa   |            Marca            |       Modelo       |       Ano       |       Cor       | Categoria | Data do Cadastro |  Horário  |")
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|-----------|------------------|-----------|")
    for placa, dados in veiculos.items():
            print("| %-9s "%placa, end='')
            print("| %-27s "%dados['marca'], end='')
            print("| %-18s "%dados['modelo'], end='')
            print("| %-15s "%dados['ano'], end='')
            print("| %-15s "%dados['cor'], end='')
            print("| %-9s "%dados['categoria'], end='')
            print("| %-16s "%dados['data_cadastro'], end='')
            print("| %-9s |"%dados['hora_cadastro'])
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|-----------|------------------|-----------|")
    print()
    input("Tecle <ENTER> para continuar...") 

def veiculos_mais_procurados():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("####################################################################################################")
    print("#######################               Veículos Mais Procurados               #######################")
    print("####################################################################################################")
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|")
    print("|   Placa   |            Marca            |       Modelo       |       Ano       |       Cor       |")
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|")
    #tranformar em comentário ctrl + /
    # lista_placas = alugueis_por_veiculo.keys()
    # lista_alugueis = alugueis_por_veiculo.values()
    # tam = len(lista_placas)
    # for i in range(tam-1):
    #     for j in range(i+1,tam):
    #         if lista_alugueis[i]<lista_alugueis[j]:
    #             variavelTemp = lista_alugueis[i]
    #             lista_alugueis[i] = lista_alugueis[j]
    #             lista_alugueis[j] = variavelTemp
                
    #             variavelTemp = lista_placas[i]
    #             lista_placas[i] = lista_placas[j]
    #             lista_placas[j] = variavelTemp

    # print(lista_placas, end='')
    # print(lista_alugueis)

    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|")
    print()
    input("Tecle <ENTER> para continuar...")

def historicoAlugueis():
    interface_historico()
    # placa = input("Informe a placa do veículo: ").upper()
    # aluguel = historicoAlugueis[placa]
    input("Tecle <ENTER> para continuar...")

##############################################
#####         Módulo Informações         #####    
##############################################
def modInfo():
    interface_informacoes()
    input("Tecle <ENTER> para voltar ao menu principal...")
