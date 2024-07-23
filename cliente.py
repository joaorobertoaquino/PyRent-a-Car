from dicionarios import clientes
import interfaces as ifc 
import validacao as val
from datetime import datetime
import funcoes

#########################
#####   Cadastrar   #####
#########################
def cadastrarCliente():
    ifc.cabecalhoModulos("Cadastrar Cliente")
    nome = funcoes.ler_nome()
    print()
    cpf = funcoes.ler_cpf()
    print()
    email = funcoes.ler_email()
    print()
    fone = funcoes.ler_telefone()
    print()
    dataNascimento = funcoes.ler_data_nascimento()
    print()
    data = datetime.now()
    clientes[cpf] = [nome,email,fone,dataNascimento, data.strftime("%x, %X")]
    print("✅ Cliente cadastrado com sucesso!")
    input("Tecle <ENTER> para continuar...")

#########################
#####     Exibir    #####
#########################
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

#########################
#####    Alterar    #####
#########################
def alterarDadosCliente():
    ifc.cabecalhoModulos("Alterar Dados do Cliente")
    cpf = input('❱ Qual o CPF do Cliente? ').strip()
    cpf = val.formatar_cpf(cpf)
    
    if cpf in clientes:
        dadosCliente = clientes[cpf]
        print("\n❱ Informe os novos dados ou deixe o campo em branco para não alterar a informação.")
        
        nome = input(f"\n👤 Nome ({dadosCliente[0]}): ").strip()
        if nome:
            nome = funcoes.ler_nome()
            clientes[cpf][0] = nome
        
        email = input(f"📧 Email ({dadosCliente[1]}): ").strip()
        if email:
            email = funcoes.ler_email()
            clientes[cpf][1] = email
        
        fone = input(f"📞 Celular ({dadosCliente[2]}): ").strip()
        if fone:
            fone = funcoes.ler_telefone()
            clientes[cpf][2] = fone
        
        dataNascimento = input(f"🎂 Data de Nascimento ({dadosCliente[3]}): ").strip()
        if dataNascimento:
            dataNascimento = funcoes.ler_data_nascimento()
            clientes[cpf][3] = dataNascimento

        print('\n📋 Dados alterados com sucesso!')
    else:
        print('\n❌ Cliente inexistente!')

    input(" Tecle <ENTER> para continuar...")

#########################
#####    Excluir    #####
#########################
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