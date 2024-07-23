
import pickle
import interfaces as ifc 
from dicionarios import clientes, veiculos, historico_aluguel, funcionarios
import validacao as val
import validacao as val

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

##################################### 
#####       Verificação         #####  
#####################################

def ler_nome():
    nome = input("👤 Nome: ")
    while not val.validar_nome(nome):
        print("==⊳ Ops! O nome informado é inválido!")
        print("==⊳ Tente novamente...")
        print()
        nome = input("👤 Nome: ")
    return nome

def ler_email():
    email = input("📧 Email: ")
    while not val.validar_email(email):
        print("==⊳ Ops! O email informado é inválido!")
        print("==⊳ Tente novamente...")
        print()
        email = input("📧 Email: ")
    return email

def ler_data_nascimento():
    data_nascimento = input("🎂 Data de nascimento (00/00/0000): ")
    is_valid, message = val.validar_Datanascimento(data_nascimento)
    while not is_valid:
        print(f"==⊳ Ops! {message}")
        print("==⊳ Tente novamente...")
        print()
        data_nascimento = input("🎂 Data de nascimento (00/00/0000): ")
        is_valid, message = val.validar_Datanascimento(data_nascimento)
    return data_nascimento

def ler_placa_veiculo():
    placa = input("⊳ Placa do Veículo: ")
    while not val.validar_placa(placa):
        print("==⊳ Ops! A placa do veículo informada é inválida!")
        print("==⊳ Tente novamente...")
        print()
        placa = input("⊳ Placa do Veículo: ")
    return placa

def ler_cpf():
    cpf = input("🆔 CPF: ")
    cpf = val.formatar_cpf(cpf)
    while not val.validar_cpf(cpf):
        print("==⊳ Ops! CPF inválido!")
        print("==⊳ Tente novamente...")
        print()
        cpf = input("🆔 CPF: ")
    return cpf

def ler_telefone():
    fone = input("📞 Celular: ")
    fone = val.formatar_telefone(fone)
    while not val.validar_telefone(fone):
        print("==⊳ Ops! O telefone informado é inválido!")
        print("Utilize o modelo a seguir como exemplo: '+55 12 34567-8901' ou '12 3456-7890'")
        print("==⊳ Tente novamente...")
        print()
        fone = input("📞 Celular: ")
    return fone

def ler_ano_veiculo():
    ano = input("⊳ Ano de lançamento: ")
    while not val.validar_ano_veiculo(ano):
        print("==⊳ Ops! Ano inválido!")
        print("==⊳ O ano deve ser um número de quatro dígitos entre 1886 e o ano atual.")
        print()
        ano = input("⊳ Ano de lançamento: ")
    return ano