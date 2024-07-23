from dicionarios import funcionarios
import interfaces as ifc 
import validacao as val
from datetime import datetime
import funcoes

#########################
#####   Cadastrar   #####
#########################
def cadastrarFunc():
    ifc.cabecalhoModulos("Cadastrar Funcionário")
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
    funcionarios[cpf] = [nome,email,fone,dataNascimento,data.strftime("%x, %X")]
    print("✅ Funcionário cadastrado com sucesso!")
    input("Tecle <ENTER> para continuar...")

#########################
#####     Exibir    #####
#########################
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

#########################
#####    Alterar    #####
#########################
def alterarDadosFunc():
    ifc.cabecalhoModulos("Alterar Dados do Cliente")
    cpf = input('❱ Qual o CPF do Cliente? ').strip()
    cpf = val.formatar_cpf(cpf)
    
    if cpf in funcionarios:
        dadosCliente = funcionarios[cpf]
        print("\n❱ Informe os novos dados ou deixe o campo em branco para não alterar a informação.")
        
        nome = input(f"\n👤 Nome ({dadosCliente[0]}): ").strip()
        if nome:
            nome = funcoes.ler_nome()
            funcionarios[cpf][0] = nome

        email = input(f"📧 Email ({dadosCliente[1]}): ").strip()
        if email:
            email = funcoes.ler_email()
            funcionarios[cpf][1] = email
        
        fone = input(f"📞 Celular ({dadosCliente[2]}): ").strip()
        if fone:
            fone = funcoes.ler_telefone()
            funcionarios[cpf][2] = fone
        
        dataNascimento = input(f"🎂 Data de Nascimento ({dadosCliente[3]}): ").strip()
        if dataNascimento:
            dataNascimento = funcoes.ler_data_nascimento()
            funcionarios[cpf][3] = dataNascimento

        print('\n📋 Dados alterados com sucesso!')
    else:
        print('\n❌ Cliente inexistente!')

    input(" Tecle <ENTER> para continuar...")
    input("Tecle <ENTER> para continuar...")

#########################
#####    Excluir    #####
#########################
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