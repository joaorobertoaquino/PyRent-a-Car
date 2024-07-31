import os 

#Exibir cabeçalho automático reutilizável
def cabecalhoModulos(titulo):
    os.system('clear' if os.name == 'posix' else 'cls')
    titulo_len = len(titulo)
    total_length = titulo_len + 10
    margem = (total_length - titulo_len - 4) // 2  #4 espaços para "===="
    linha_titulo = "=" * 5 + " " * margem + titulo + " " * margem + "=" * 5
    linha = "=" * total_length + "=" * 6
    print(linha)
    print(linha_titulo)
    print(linha)
    print()
#código feito por Diana com ajuda do chat GPT

def interface_principal():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("================================================")
    print("======  ⋆⁺⋆⁺₊⋆ Locadora de Carros ⋆⁺⋆⁺₊⋆  ======")
    print("================================================")
    print("=====        1 - Módulo Clientes           =====")
    print("=====        2 - Módulo Funcionários       =====")
    print("=====        3 - Módulo Veículos           =====")
    print("=====        4 - Módulo Reserva            =====")
    print("=====        5 - Módulo Relatório          =====")
    print("=====        6 - Módulo Informações        =====")
    print("=====        0 - Sair                      =====")

def interface_clientes():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("=================================================")
    print("=====            Módulo Clientes            =====")
    print("=================================================")
    print("=====     1 - Cadastrar Cliente             =====")
    print("=====     2 - Exibir Dados do Cliente       =====")
    print("=====     3 - Alterar Dados do Cliente      =====")
    print("=====     4 - Excluir Cliente               =====")
    print("=====     0 - Retornar ao Menu Principal    =====")

def interface_funcionarios():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("==================================================")
    print("=====           Módulo Funcionários          =====")
    print("==================================================")
    print("=====     1 - Cadastrar Funcionários         =====")
    print("=====     2 - Exibir Dados do Funcionários   =====")
    print("=====     3 - Alterar Dados do Funcionários  =====")
    print("=====     4 - Excluir Funcionário            =====")
    print("=====     0 - Retornar ao Menu Principal     =====")

def interface_veiculos():
    os.system('clear' if os.name == 'posix' else 'cls')   
    print()
    print("==================================================")
    print("=====            Módulo Veículos             =====")
    print("==================================================")
    print("=====     1 - Cadastrar Veículo              =====")
    print("=====     2 - Exibir Dados do Veículo        =====")
    print("=====     3 - Alterar Dados do Veículo       =====")
    print("=====     4 - Excluir Veículo                =====")
    print("=====     0 - Retornar ao Menu Principal     =====")

def interface_reserva():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("=================================================")
    print("=====             Módulo Reserva            =====")
    print("=================================================")
    print("=====     1 - Reservar Veículo              =====")
    print("=====     2 - Devolver Veículo              =====")
    print("=====     3 - Veículos Disponíveis          =====")
    print("=====     4 - Veículos Alugados             =====")
    print("=====     5 - Política de Combustível       =====")
    print("=====     0 - Retornar ao Menu Principal    =====")


def interface_Veiculosdisponiveis():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("==================================================================================================================================")
    print("=====                                           Lista de Veículos Disponíveis                                                =====")
    print("==================================================================================================================================")
    print("|-----------|-----------------|--------------------|-------|-----------------|-----------|--------------------|------------------|")
    print("|   Placa   |      Marca      |       Modelo       |  Ano  |       Cor       | Categoria |  Data do Cadastro  |      Horário     |")
    print("|-----------|-----------------|--------------------|-------|-----------------|-----------|--------------------|------------------|")

def interface_Veiculosalugados():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("=============================================================================================================================================================================")
    print("=======================                                                  Lista de Veículos Alugados                                                   =======================")
    print("=============================================================================================================================================================================")
    print("|-----------|-----------------|--------------------|-------|-----------------|-----------|---------------------|----------------------|-------------------------------------|")
    print("|   Placa   |      Marca      |       Modelo       |  Ano  |       Cor       | Categoria |   Data do Aluguel   |  Data de Devolução   |       Atualmente Alugado Por:       |")
    print("|-----------|-----------------|--------------------|-------|-----------------|-----------|---------------------|----------------------|-------------------------------------|")

def interface_Politicacombustivel():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("====================================================================================")
    print("=====                         Política de Combustível                          =====")
    print("====================================================================================")
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

def interface_relatorio():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("=================================================")
    print("=====            Módulo Relatório           =====")
    print("=================================================")
    print("=====     1 - Lista Geral de Clientes       =====")
    print("=====     2 - Lista Geral de Funcionários   =====")
    print("=====     3 - Lista Geral de Veículos       =====")
    print("=====     4 - Veículos mais Procurados      =====")
    print("=====     5 - Histórico de Alugueis         =====")
    print("=====     0 - Retornar ao Menu Principal    =====")

def interface_listaclientes():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("==================================================================================================================================================================")
    print("=======================                                              Lista Geral de Clientes                                               =======================")
    print("==================================================================================================================================================================")
    print("|-----------------|-------------------------------------|----------------------------------------|-----------------|----------------------|----------------------|")
    print("|       CPF       |            Nome Completo            |                 E-mail                 |     Celular     |  Data de Nascimento  |   Data do Cadastro   |")
    print("|-----------------|-------------------------------------|----------------------------------------|-----------------|----------------------|----------------------|")

def interface_listfucionarios():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("==============================================================================================================================================================")
    print("=======================                                          Lista Geral de Funcionários                                           =======================")
    print("==============================================================================================================================================================")
    print("|-----------------|-------------------------------------|------------------------------------|-----------------|----------------------|----------------------|")
    print("|       CPF       |            Nome Completo            |               E-mail               |     Celular     |  Data de Nascimento  |   Data do Cadastro   |")
    print("|-----------------|-------------------------------------|------------------------------------|-----------------|----------------------|----------------------|")

def interface_listaveiculos():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("=======================================================================================================================================")
    print("=======================                                Lista Geral de Veículos                                  =======================")
    print("=======================================================================================================================================")
    print("|-----------|-----------------------------|--------------------|---------|-----------------|-----------|------------------|-----------|")
    print("|   Placa   |            Marca            |       Modelo       |   Ano   |       Cor       | Categoria | Data do Cadastro |  Horário  |")
    print("|-----------|-----------------------------|--------------------|---------|-----------------|-----------|------------------|-----------|")

def interface_maisprocurados():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("=======================================================================================================")
    print("=======================                Veículos Mais Procurados                 =======================")
    print("=======================================================================================================")
    print("|-----------|-----------------------------|----------|-------|---------------|-----------|------------|")
    print("|   Placa   |            Marca            |  Modelo  |  Ano  |      Cor      | Categoria |  Contagem  |")
    print("|-----------|-----------------------------|----------|-------|---------------|-----------|------------|")

def interface_historico():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("================================================================================================================================================")
    print("=====                                                    Histórico de Aluguel do Veículo                                                   =====")
    print("================================================================================================================================================")
    print("|---------|-------------------------------------|-----------------|--------------|--------------|----------------|----------------|------------|")
    print("|  Placa  |            Alugado por:             |       CPF       | Data Inicial | Hora Aluguel | Data Devolução | Hora Devoluçao |   Status   |")
    print("|---------|-------------------------------------|-----------------|--------------|--------------|----------------|----------------|------------|")
    
def interface_informacoes():
    os.system('clear' if os.name == 'posix' else 'cls')
    print()
    print("========================================================")
    print("=====           📋 Módulo Informações 📋           =====")
    print("========================================================")
    print("=====                                              =====")
    print("=====   🚗 Projeto: Locadora de Veículos Crystal   =====")
    print("=====                                              =====")
    print("=====   🛠️  Desenvolvimento:                        =====")
    print("=====   João Roberto Galvão Aquino                 =====")
    print("=====                                              =====")
    print("=====   📧 E-mail para comunicação:                =====")
    print("=====   joao.roberto.galvao.017@gmail.com          =====")
    print("=====                                              =====")
    print("========================================================")
    print()
    