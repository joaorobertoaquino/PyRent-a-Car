import re
from datetime import datetime

##################################### 
#####         Formatar          #####  
#####################################
def formatar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = cpf.replace(".", "").replace("-", "")
    # Adiciona a formatação
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def formatar_telefone(telefone):
    # Remove caracteres não numéricos
    telefone = telefone.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
    # Adiciona a formatação
    return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"


##################################### 
#####         Validar           #####  
#####################################
def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    # Verifica o primeiro dígito verificador
    if int(cpf[9]) != digito1:
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    # Verifica o segundo dígito verificador
    if int(cpf[10]) != digito2:
        return False

    # Se passar por todas as verificações, o CPF é válido
    return True


def validar_email(email):
    regex_email = r"([a-zA-Z0-9\.\-\_]{2,})@([a-zA-Z0-9]{2,})(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?(\.[a-z]{2,})?"
    if not re.match(regex_email, email):
        return False
    return True


def validar_nome(nome):
    # Expressão regular para nomes
    regex_nome = (
        r"^["
        r"A-Za-zÀ-ÖØ-öø-ÿ"  # Letras maiúsculas e minúsculas, incluindo caracteres acentuados
        r"'\- "             # Apóstrofos, hífens e espaços
        r"]+$"
    )
    
    # Verifica se o nome corresponde ao padrão
    if re.fullmatch(regex_nome, nome):
        return True
    return False


def validar_Datanascimento(dataNascimento):
    try:
        # Converte a string para um objeto datetime
        birthdate = datetime.strptime(dataNascimento, '%d/%m/%Y')
    except ValueError:
        # Retorna falso se a data estiver em formato inválido
        return False, "Data inválida. Utlize o caractere '/' idêntico ao formato a seguir: (00/00/0000)"

    # Obtém a data atual
    today = datetime.today()

    # Verifica se a data de nascimento não é no futuro ou no presente
    if birthdate >= today:
        return False, "Data de nascimento não pode ser no presente ou no futuro."

    # Calcula a idade da pessoa
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    # Verifica se a pessoa tem pelo menos 18 anos
    if age < 18:
        return False, "A pessoa deve ter pelo menos 18 anos."

    return True, "Data de nascimento válida."


def validar_placa(placa):
    # Expressão regular para os dois formatos de placas no Brasil
    placa_antiga_regex = r'^[A-Z]{3}-[0-9]{4}$'    # Formato antigo: ABC-1234
    placa_atual_regex = r'^[A-Z]{3}[0-9][A-Z][0-9]{2}$'  # Formato novo: ABC1D23
    
    return re.match(placa_antiga_regex, placa) is not None or re.match(placa_atual_regex, placa) is not None


def validar_telefone(fone):
    fone = ''.join(filter(str.isdigit, fone))
    regex_tel = r'([0-9]{11}\b)'
    if not re.match(regex_tel, fone):
        return False
    return True

def validar_ano_veiculo(ano):
    # Remove caracteres não numéricos
    ano = ''.join(filter(str.isdigit, ano))
    
    # Verifica se o ano tem exatamente 4 dígitos e está no intervalo válido
    if len(ano) == 4 and ano.isdigit():
        ano_int = int(ano)
        # Define um intervalo razoável para o ano do veículo
        ano_atual = datetime.now().year
        if 1886 <= ano_int <= ano_atual:
            return True
    return False

#1886 marca o início da produção de automóveis, tornando-o um ano lógico para definir o início da era automotiva.