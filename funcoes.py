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

###############################################  
#####          Módulo Clientes            #####  
############################################### 
def modCliente():
    ifc.interface_clientes()
    op_cliente = input("=====❱ Escolha sua opção: ") 
    return op_cliente

def cadastrarCliente():
    ifc.cabecalhoModulos("Cadastrar Cliente")
    nome = input("👤 Nome: ")
    print()
    cpf = input("🆔 CPF: ")
    cpf = val.formatar_cpf(cpf)
    print()
    email = input("📧 Email: ")
    print()
    fone = input("📞 Celular: ")
    fone = val.formatar_telefone(fone)
    print()
    dataNascimento = input("🎂 Data de nascimento (00/00/0000): ")
    dataNascimento = val.formatar_data(dataNascimento)
    print()
    data = datetime.now()
    clientes[cpf] = [nome,email,fone,dataNascimento, data.strftime("%x, %X")]
    print("✅ Cliente cadastrado com sucesso!")
    input("Tecle <ENTER> para continuar...")

def exibirDadosCliente():
    ifc.cabecalhoModulos("Exibir Dados do Cliente")
    cpf = input('❱ Qual o CPF do cliente? ')
    cpf = val.formatar_cpf(cpf)
    print()
    if cpf in clientes:
        print("👤 Nome: ", clientes[cpf][0])
        print("🆔 CPF: ", cpf)
        print("📧 Email: ", clientes[cpf][1])
        print("📞 Celular: ", clientes[cpf][2])
        print("🎂 Data de Nascimento: ", clientes[cpf][3])
    else:
        print('❌ Cliente inexistente!')
    print()
    input("Tecle <ENTER> para continuar...")

def alterarDadosCliente():
    ifc.cabecalhoModulos("Alterar Dados do Cliente")
    cpf = input('❱ Qual o CPF do Cliente? ')
    cpf = val.formatar_cpf(cpf)
    if cpf in clientes:
        dadosCliente = clientes[cpf]
        print("\n❱ Informe os novos dados ou deixe o campo em branco para não alterar a informação.")
        nome = input(f"\n👤 Nome ({dadosCliente[0]}): ").strip()
        email = input(f"📧 Email ({dadosCliente[1]}): ").strip()
        fone = input(f"📞 Celular ({dadosCliente[2]}): ").strip()
        dataNascimento = input(f"🎂 Data de Nascimento ({dadosCliente[3]}): ").strip()
        # Atualiza apenas os campos que não estão vazios, permitindo que a informação anterior continue a mesma.
        if nome:
            clientes[cpf][0] = nome
        if email:
            clientes[cpf][1] = email
        if fone:
            fone = val.formatar_telefone(fone)
            clientes[cpf][2] = fone
        if dataNascimento:
            dataNascimento = val.formatar_data(dataNascimento)
            clientes[cpf][3] = dataNascimento

        print('\n📋 Dados alterados com sucesso!')
    else:
        print('\n❌ Cliente inexistente!')
    
    input(" Tecle <ENTER> para continuar...")

def excluirCliente():
    ifc.cabecalhoModulos("Excluir Cliente")
    cpf = input('_ Informe o CPF do cliente: ')
    cpf = val.formatar_cpf(cpf)
    if cpf in clientes:
        print("👤 Nome: ", clientes[cpf][0])
        print("📧 Email: ", clientes[cpf][1])
        print("📞 Celular: ", clientes[cpf][2])
        print("🎂 Data de Nascimento: ", clientes[cpf][3])
        print()
        resp = input('❱ Tem certeza que deseja excluir este cliente (Sim/Não)?')
        if resp.upper() == 'SIM':
            del clientes[cpf]
            print("✅ Aluno excluído com sucesso!")
        else:
            print('🚫 Exclusão não realizada!')
    else:
        print('❌ Cliente inexistente!')
    input("Tecle <ENTER> para continuar...")
    

############################################### 
#####          Módulo Funcionários        #####        
###############################################    
def modFunc():
    ifc.interface_funcionarios()
    op_func = input("=====❱ Escolha sua opção: ")
    return op_func

def cadastrarFunc():
    ifc.cabecalhoModulos("Cadastrar Funcionário")
    nome = input("👤 Nome: ")
    print()
    cpf = input("🆔 CPF: ")
    cpf = val.formatar_cpf(cpf)
    print()
    email = input("📧 Email: ")
    print()
    fone = input("📞 Celular: ")
    print()
    dataNascimento = input("🎂 Data de Nascimento (00/00/0000): ")
    dataNascimento = val.formatar_data(dataNascimento)
    print()
    data = datetime.now()
    funcionarios[cpf] = [nome,email,fone,dataNascimento,data.strftime("%x, %X")]
    print("✅ Funcionário cadastrado com sucesso!")
    input("Tecle <ENTER> para continuar...")

def exibirDadosFunc():
    ifc.cabecalhoModulos("Exibir Dados do Funcionário")
    cpf = input('❱ Qual o CPF do funcionário(a)? ')
    cpf = val.formatar_cpf(cpf)
    print()
    if cpf in funcionarios:
        print("👤 Nome: ", funcionarios[cpf][0])
        print("🆔 CPF: ", cpf)
        print("📧 Email: ", funcionarios[cpf][1])
        print("📞 Celular: ", funcionarios[cpf][2])
        print("🎂 Data de Nascimento: ", funcionarios[cpf][3])
    else:
        print('❌ Funcionário(a) inexistente!')
    print()
    input("Tecle <ENTER> para continuar...")

def alterarDadosFunc():
    ifc.cabecalhoModulos("Alterar Dados do Funcionário")
    cpf = input('❱ Qual o CPF do funcionário(a)? ')
    cpf = val.formatar_cpf(cpf)
    if cpf in funcionarios:
        dadosFuncionarios = funcionarios[cpf]
        print("❱ Informe os novos dados ou deixe o campo em branco para não alterar a informação.")
        nome = input(f"👤 Nome ({dadosFuncionarios[0]}: )").strip()
        email = input(f"📧 Email ({dadosFuncionarios[1]}): ").strip()
        fone = input(f"📞 Celular ({dadosFuncionarios[2]}): ").strip()
        dataNascimento = input(f"🎂 Data de Nascimento ({dadosFuncionarios[3]}): ").strip()
        # Atualiza apenas os campos que não estão vazios, permitindo que a informação anterior continue a mesma.
        if nome:
            funcionarios[cpf][0] = nome
        if email:
            funcionarios[cpf][1] = email
        if fone:
            funcionarios[cpf][2] = fone
        if dataNascimento:
            funcionarios[cpf][3] = dataNascimento
        
        print('\n✅ Dados alterados com sucesso!')
    else:
        print('\n❌ Funcionário(a) inexistente!')

    input("Tecle <ENTER> para continuar...")

def excluirFunc():
    ifc.cabecalhoModulos("Excluir Funcionário")
    cpf = input('❱ Informe o CPF do funcionário(a): ')
    cpf = val.formatar_cpf(cpf)
    if cpf in funcionarios:
        print("👤 Nome: ", funcionarios[cpf][0])
        print("📧 Email: ", funcionarios[cpf][1])
        print("📞 Celular: ", funcionarios[cpf][2])
        print("🎂 Data de Nascimento: ", funcionarios[cpf][3])
        print()
        resp = input('❱ Tem certeza que deseja excluir este funcionário(a)? (Sim/Não)').upper()
        if resp == 'SIM':
            del funcionarios[cpf]
            print("✅ Funcionário(a) excluído com sucesso!")
        else:
            print('🚫 Exclusão não realizada!')
    else:
        print("❌ Funcionário inexistente!")
    input("Tecle <ENTER> para continuar...") 


###########################################
#####         Módulo Veículos         #####         
###########################################
def modVeic():
    ifc.interface_veiculos()
    op_veic = input("=====❱ Escolha sua opção: ")
    return op_veic

def cadastrarVeic():
    ifc.cabecalhoModulos("Cadastrar Veículo")
    marca = input("⊳ Marca: ")
    print()
    modelo = input("⊳ Modelo: ")
    print()
    ano = input("⊳ Ano de lançamento: ")
    print()
    cor = input("⊳ Cor: ")
    print()
    placa = input("⊳ Número da placa: ").upper()
    print()
    categoria = input("⊳ Informe a categoria do carro: ")
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
    print(f"✅ Veículo {modelo} cadastrado com sucesso!")
    input("Tecle <ENTER> para continuar...")

def exibirDadosVeic():
    ifc.cabecalhoModulos("Exibir Dados do Veículo")
    placa = input("❱ Digite a placa do veículo: ").upper()
    print()
    if placa in veiculos:
        dados = veiculos[placa]
        print(f"⊳ Marca: {dados['marca']}")
        print(f"⊳ Modelo: {dados['modelo']}")
        print(f"⊳ Ano: {dados['ano']}")
        print(f"⊳ Cor: {dados['cor']}")
        print(f"⊳ Categoria: {dados['categoria']}")
        print(f"⊳ Cadastro: {dados['data_cadastro']} às {dados['hora_cadastro']}")
        print(f"⊳ Alugado: {'Sim' if dados['alugado'] else 'Não'}")
        if dados['alugado']:
            print(f"⊳ Data de Início: {dados['data_inicio']}")
            print(f"⊳ Data de Fim: {dados['data_fim']}")
    else:
        print("❌ Veículo não encontrado.")
    input("\nPressione Enter para voltar ao menu...")


def alterarDadosVeic():
    ifc.cabecalhoModulos("Alterar Dados do Veículo")
    placa = input('❱ Informe a placa do veículo: ').upper()
    respExcluirDados = input("⊳ Deseja mesmo continuar com essa ação (Sim / Não)? ")
    if respExcluirDados.upper() == 'SIM':
        if placa in veiculos:
            veiculo = veiculos[placa]
            print("\n❱ Deixe o campo em branco para não alterar a informação.")
            marca = input(f"⊳ Marca ({veiculo['marca']}): ") or veiculo['marca']
            modelo = input(f"⊳ Modelo ({veiculo['modelo']}): ") or veiculo['modelo']
            ano = input(f"⊳ Ano ({veiculo['ano']}): ") or veiculo['ano']
            cor = input(f"⊳ Cor ({veiculo['cor']}): ") or veiculo['cor']
            categoria = input(f"⊳ Categoria ({veiculo['categoria']}): ") or veiculo['categoria']

            veiculos[placa].update({
                'marca': marca,
                'modelo': modelo,
                'ano': ano,
                'cor': cor,
                'categoria': categoria
            })
            print(f"\n📋 Dados do veículo {modelo} atualizados com sucesso!")
        else:
            print("\n❌ Veículo não encontrado!")
    else:
        print("\n🚫 Ação não concluída!")

    input("\nTecle <ENTER> para continuar...")


def excluirVeic():
    ifc.cabecalhoModulos("Excluir Veículo")
    placa = input('❱ Informe a placa do veículo: ').upper()
    respExcluir = input("Deseja mesmo completar essa ação (Sim / Não)? ")
    if respExcluir.upper() == 'SIM':
        if placa in veiculos:
            del veiculos[placa]
            print(f"Veículo com placa {placa} excluído com sucesso!")
        else:
            print("❌ Veículo não encontrado.")
    else:
        print("🚫 Ação não concluída!")
    input("Tecle <ENTER> para continuar...")


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

