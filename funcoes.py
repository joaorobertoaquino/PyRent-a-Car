import os
import pickle
from datetime import datetime, timedelta
from dicionarios import cliente, funcionarios, veiculos_disponiveis, veiculos_alugados, alugueis_por_veiculo, valor_aluguel

########################################################
#####            Escrever Arquivos                 #####
########################################################
def escreverArquivos():
    arq_cliente = open("cliente.dat", "wb")
    pickle.dump(cliente, arq_cliente)
    arq_cliente.close()

    arq_funcionarios = open("funcionarios.dat", "wb")
    pickle.dump(funcionarios, arq_funcionarios)
    arq_funcionarios.close()

    arq_veiculos_disponiveis = open("veiculos_disponiveis.dat", "wb")
    pickle.dump(veiculos_disponiveis, arq_veiculos_disponiveis)
    arq_veiculos_disponiveis.close()

    arq_veiculos_alugados = open("veiculos_alugados.dat", "wb")
    pickle.dump(veiculos_alugados, arq_veiculos_alugados)
    arq_veiculos_alugados.close()

    arq_alugueis_por_veiculo = open("alugueis_por_veiculo.dat", "wb")
    pickle.dump(alugueis_por_veiculo, arq_alugueis_por_veiculo)
    arq_alugueis_por_veiculo.close()

########################################################
#####                Menu Pricipal                 #####
########################################################
def menuPrincipal():
    os.system('clear' if os.name == 'posix' else 'cls')
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
    os.system('clear' if os.name == 'posix' else 'cls')
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
    cliente[cpf] = [nome,email,fone,dataNascimento, data.strftime("%x, %X")]
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
    if cpf in cliente:
        print("##### Nome: ", cliente[cpf][0])
        print("##### CPF: ", cpf)
        print("##### Email: ", cliente[cpf][1])
        print("##### Celular: ", cliente[cpf][2])
        print("##### Data de Nascimento: ", cliente[cpf][3])
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
    if cpf in cliente:
        dadosCliente = cliente[cpf]
        print("Informe os novos dados ou deixe o campo em branco para não alterar a informação.")
        nome = input(f"##### Nome ({dadosCliente[0]}): ").strip()
        email = input(f"##### Email ({dadosCliente[1]}): ").strip()
        fone = input(f"##### Celular ({dadosCliente[2]}): ").strip()
        dataNascimento = input(f"##### Data de Nascimento ({dadosCliente[3]}): ").strip()
        # Atualiza apenas os campos que não estão vazios, permitindo que a informação anterior continue a mesma.
        if nome:
            cliente[cpf][0] = nome
        if email:
            cliente[cpf][1] = email
        if fone:
            cliente[cpf][2] = fone
        if dataNascimento:
            cliente[cpf][3] = dataNascimento

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
    if cpf in cliente:
        print("##### Nome: ", cliente[cpf][0])
        print("##### Email: ", cliente[cpf][1])
        print("##### Celular: ", cliente[cpf][2])
        print("##### Data de Nascimento: ", cliente[cpf][3])
        print()
        resp = input('Tem certeza que deseja excluir este cliente (Sim/Não)?')
        if resp.upper() == 'SIM':
            del cliente[cpf]
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
    os.system('clear' if os.name == 'posix' else 'cls')
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
    os.system('clear' if os.name == 'posix' else 'cls')   
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
    placa = input("##### Número da placa: ")
    print()
    categoria = input("##### Informe a categoria do carro: ")
    print()
    data = datetime.now()
    veiculos_disponiveis[placa] = [marca,modelo,ano,cor,categoria, data.strftime("%d/%m/%Y"), data.strftime("%H:%M:%S")]
    print(f"Veículo {modelo} cadastrado com sucesso!")
    input("Tecle <ENTER> para continuar...")

def exibirDadosVeic():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####    Exibir Dados do Veículo       #####")
    print("############################################")
    print()
    placa = input("Digite a placa do veículo: ")
    if placa in veiculos_disponiveis:
        dados = veiculos_disponiveis[placa]
        print(f"##### Marca: {dados[0]}")
        print(f"##### Modelo: {dados[1]}")
        print(f"##### Ano: {dados[2]}")
        print(f"##### Cor: {dados[3]}")
        print(f"##### Categoria: {dados[4]}")
        print(f"##### Cadastro: {dados[5]} às {dados[6]}")
        
    elif placa in veiculos_alugados:
        dados = veiculos_alugados[placa]
        print(f"##### Marca: {dados[0]}")
        print(f"##### Modelo: {dados[1]}")
        print(f"##### Ano: {dados[2]}")
        print(f"##### Cor: {dados[3]}")
        print(f"##### Categoria: {dados[4]}")
        print(f"##### Cadastro: {dados[5]} às {dados[6]}")
        
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
    placa = input('Informe a placa do veículo: ')
    respExcluirDados = input("Deseja mesmo continuar com essa ação (Sim / Não)? ")
    if respExcluirDados.upper() == 'SIM':
        if (placa in veiculos_disponiveis) or (placa in veiculos_alugados):
            if placa in veiculos_disponiveis:
                veiculo = veiculos_disponiveis[placa]
            else:
                veiculo = veiculos_alugados[placa][:5]
            
            print("Deixe o campo em branco para não alterar a informação.")
            marca = input(f"Marca ({veiculo[0]}): ") or veiculo[0]
            modelo = input(f"Modelo ({veiculo[1]}): ") or veiculo[1]
            ano = input(f"Ano ({veiculo[2]}): ") or veiculo[2]
            cor = input(f"Cor ({veiculo[3]}): ") or veiculo[3]
            categoria = input(f"Categoria ({veiculo[4]}): ") or veiculo[4]

            if placa in veiculos_disponiveis:
                veiculos_disponiveis[placa] = [marca, modelo, ano, cor, categoria, veiculo[5]]
            else:
                veiculos_alugados[placa][:6] = [marca, modelo, ano, cor, categoria, veiculo[5]]
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
    placa = input('Informe a placa do veículo: ')
    respExcluir = input("Deseja mesmo completar essa ação (Sim / Não)? ")
    if respExcluir.upper() == 'SIM':
        if placa in veiculos_disponiveis:
            del veiculos_disponiveis[placa]
            print(f"Veículo com placa {placa} excluído com sucesso!")
        elif placa in veiculos_alugados:
            del veiculos_alugados[placa]
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
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("#############################################")
    print("#####   Você está no Módulo Reserva     #####")
    print("#############################################")
    print("##### 1 - Reservar Veículo              #####")
    print("##### 2 - Devolver Veículo              #####")
    print("##### 3 - Veículos Disponíveis          #####")
    print("##### 4 - Veículos Alugados             #####")
    print("##### 5 - Política de Combustível       #####")
    print("##### 0 - Retornar ao Menu Principal    #####")
    op_reserva = input("##### Escolha sua opção: ")
    return op_reserva

def reservarVeiculo():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("############################################")
    print("#####        Reservar Veículo          #####")
    print("############################################")
    print()
    placa = input("Digite a placa do veículo a ser alugado: ")
    if placa in veiculos_disponiveis:
        dias = int(input("Por quantos dias o veículo será alugado? "))
        data_inicio = datetime.now().strftime("%d/%m/%Y")
        data_fim = (datetime.now() + timedelta(days=dias)).strftime("%d/%m/%Y")
        veiculo = veiculos_disponiveis.pop(placa)
        preco = valor_aluguel[veiculo[4]]
        veiculo.extend([data_inicio, data_fim])
        veiculos_alugados[placa] = veiculo

        print("Preço da diária: R$ ", preco)

        if placa in alugueis_por_veiculo:
            alugueis_por_veiculo[placa] += 1
        else:
            alugueis_por_veiculo[placa] = 1

        print(f"\nVeículo {veiculo[1]} alugado com sucesso até {data_fim}!")
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
    placa = input("Digite a placa do veículo a ser devolvido: ")
    respDevolver = input("Deseja mesmo continuar (Sim/Não)? ")
    if placa in veiculos_alugados:
        veiculo = veiculos_alugados.pop(placa)
        veiculo = veiculo[:7]  # Remove as informações de aluguel
        veiculos_disponiveis[placa] = veiculo
        print(f"Veículo {veiculo[1]} devolvido com sucesso!")
    else:
        print("Veículo não encontrado ou não está alugado.")
    
    input("Tecle <ENTER> para continuar...")


def veiculosDisponiveis():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("########################################################################################################################################################")
    print("#####                                                      Lista de Veículos Disponíveis                                                           #####")
    print("########################################################################################################################################################")
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|-----------|--------------------|------------------|")
    print("|   Placa   |            Marca            |       Modelo       |       Ano       |       Cor       | Categoria |  Data do Cadastro  |      Horário     |")
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|-----------|--------------------|------------------|")
    for placa, dados in veiculos_disponiveis.items():
        print("| %-9s "%placa, end='')
        print("| %-27s "%dados[0], end='')
        print("| %-18s "%dados[1], end='')
        print("| %-15s "%dados[2], end='')
        print("| %-15s "%dados[3], end='')
        print("| %-9s "%dados[4], end='')
        print("| %-18s "%dados[5], end='')
        print("| %-16s |"%dados[6])
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|-----------|--------------------|------------------|")
    print()
    input("Tecle <ENTER> para continuar...")

def veiculosAlugados():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("#############################################################################################################################################################")
    print("#######################                                           Lista de Veículos Alugados                                          #######################")
    print("#############################################################################################################################################################")
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|-----------|---------------------|----------------------|")
    print("|   Placa   |            Marca            |       Modelo       |       Ano       |       Cor       | Categoria |   Data do Aluguel   |  Data de Devolução   |")
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|-----------|---------------------|----------------------|")
    for placa, dados in veiculos_alugados.items():
        print("| %-9s "%placa, end='')
        print("| %-27s "%dados[0], end='')
        print("| %-18s "%dados[1], end='')
        print("| %-15s "%dados[2], end='')
        print("| %-15s "%dados[3], end='')
        print("| %-9s "%dados[4], end='')
        print("| %-19s "%dados[7], end='')
        print("| %-20s |"%dados[8])
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|-----------|---------------------|----------------------|")
    print()
    input("Tecle <ENTER> para continuar...")

def politicaCombustivel():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("####################################################################################")
    print("#####                         Política de Combustível                          #####")
    print("####################################################################################")
    print("""
        Prezado Cliente,

        Gostaríamos de informar que, de acordo com nossas políticas de 
        aluguel de carros, é obrigatório que os veículos alugados sejam
        devolvidos com o tanque de combustível cheio. Este procedimento 
        é essencial para garantir a melhor experiência de locação para
        todos os nossos clientes.

        Agradecemos antecipadamente pela sua cooperação e compreensão.
        Se você tiver alguma dúvida ou precisar de assistência adicional,
        não hesite em entrar em contato conosco. Estamos aqui para ajudar!
        
        Atenciosamente,
        [João Roberto Galvão Aquino]
        [Locadora de Carros - Crystal]""")
    print()
    input("\nTecle <ENTER> para continuar...")


#############################################
#####         Módulo Relatório          #####   
#############################################
def modRelatorio():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("#############################################")
    print("#####   Você está no Módulo Relatório   #####")
    print("#############################################")
    print("##### 1 - Lista Geral de Clientes       #####")
    print("##### 2 - Lista Geral de Funcionários   #####")
    print("##### 3 - Lista Geral de Veículos       #####")
    print("##### 4 - Veículos mais Procurados      #####")
    print("##### 0 - Retornar ao Menu Principal    #####")
    op_relatorio = input("##### Escolha sua opção: ")
    return op_relatorio 

def lista_geral_clientes():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("##########################################################################################################################################################")
    print("#######################                                          Lista Geral de Clientes                                           #######################")
    print("##########################################################################################################################################################")
    print("|-------------|-------------------------------------|------------------------------------|-----------------|----------------------|----------------------|")
    print("|     CPF     |            Nome Completo            |               E-mail               |     Celular     |  Data de Nascimento  |   Data do Cadastro   |")
    print("|-------------|-------------------------------------|------------------------------------|-----------------|----------------------|----------------------|")
    for cpf in cliente:
        print("| %-9s "%(cpf), end='')
        print("| %-35s "%(cliente[cpf][0]), end='')
        print("| %-34s "%(cliente[cpf][1]), end='')
        print("| %-15s "%(cliente[cpf][2]), end='')
        print("| %-20s "%(cliente[cpf][3]), end='')
        print("| %-20s |"%(cliente[cpf][4]))
    print("|-------------|-------------------------------------|------------------------------------|-----------------|----------------------|----------------------|")
    print()
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
    print("#########################################################################################################################")
    print("#######################                          Lista Geral de Veículos                          #######################")
    print("#########################################################################################################################")
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|--------------------|")
    print("|   Placa   |            Marca            |       Modelo       |       Ano       |       Cor       |  Data do Cadastro  |")
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|--------------------|")
    #veículos disponíveis
    for placa, dados in veiculos_disponiveis.items():
        print("| %-9s "%placa, end='')
        print("| %-27s "%dados[0], end='')
        print("| %-18s "%dados[1], end='')
        print("| %-15s "%dados[2], end='')
        print("| %-15s "%dados[3], end='')
        print("| %-9s "%dados[4], end='')
        print("| %-15s |"%dados[5])
    #veículos alugados
    for placa, dados in veiculos_alugados.items():
        print("| %-9s "%placa, end='')
        print("| %-27s "%dados[0], end='')
        print("| %-18s "%dados[1], end='')
        print("| %-15s "%dados[2], end='')
        print("| %-15s "%dados[3], end='')
        print("| %-9s "%dados[4], end='')
        print("| %-15s |"%dados[5])
    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|--------------------|")
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
    lista_placas = alugueis_por_veiculo.keys()
    lista_alugueis = alugueis_por_veiculo.values()
    tam = len(lista_placas)
    for i in range(tam-1):
        for j in range(i+1,tam):
            if lista_alugueis[i]<lista_alugueis[j]:
                variavelTemp = lista_alugueis[i]
                lista_alugueis[i] = lista_alugueis[j]
                lista_alugueis[j] = variavelTemp
                
                variavelTemp = lista_placas[i]
                lista_placas[i] = lista_placas[j]
                lista_placas[j] = variavelTemp

    print(lista_placas, end='')
    print(lista_alugueis)

    print("|-----------|-----------------------------|--------------------|-----------------|-----------------|")
    print()
    input("Tecle <ENTER> para continuar...")

##############################################
#####         Módulo Informações         #####    
##############################################
def modInfo():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("###################################################")
    print("#####     Você está no Módulo Informações     #####")
    print("###################################################")
    print("#####                                         #####")
    print("#####  Projeto: Locadora de Veículos          #####")
    print("#####  Desenvolvimento:                       #####")
    print("#####  João Roberto Galvão Aquino             #####")
    print("#####                                         #####")
    print("#####  E-mail para comunicação:               #####")
    print("#####  joao.roberto.galvao.017@gmail.com      #####")
    print("#####                                         #####")
    print("###################################################")
    print()
    input("Tecle <ENTER> para voltar ao menu principal...")
