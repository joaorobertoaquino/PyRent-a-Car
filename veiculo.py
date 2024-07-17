from dicionarios import veiculos
import interfaces as ifc 
from datetime import datetime

#########################
#####   Cadastrar   #####
#########################
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

#########################
#####     Exibir    #####
#########################
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

#########################
#####    Alterar    #####
#########################
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

#########################
#####    Excluir    #####
#########################
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
