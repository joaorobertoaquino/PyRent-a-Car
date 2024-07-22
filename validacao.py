import re
from datetime import datetime

def formatar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = cpf.replace(".", "").replace("-", "")
    # Adiciona a formatação
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def formatar_data(data):
    # Remove caracteres não numéricos
    data = data.replace("/", "")
    # Adiciona a formatação
    return f"{data[:2]}/{data[2:4]}/{data[4:]}"

def formatar_telefone(telefone):
    # Remove caracteres não numéricos
    telefone = telefone.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")
    # Adiciona a formatação
    return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"


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
    # Expressão regular para validar um nome abrangente
    name_regex = (
        r"^["
        r"\p{L}"        # Qualquer letra unicode
        r"\p{M}"        # Marcas de acentuação
        r"'\- "         # Apóstrofos, hífens e espaços
        r"]+$"
    )
    return re.match(name_regex, nome, re.UNICODE) is not None

#     "João da Silva",
#     "Marie Curie",
#     "Anne-Marie",
#     "O'Connor",
#     "Lucas123",        # Inválido (contém números)
#     "Maria Clara!",    # Inválido (contém caractere especial)
#     "José",
#     "Ñandú",
#     "李四",            # Nome em caracteres chineses
#     "Иван Иванович",   # Nome em caracteres cirílicos
#     "Ólafur Ragnar",   # Nome com acentuação islandesa
#     "D'Angelo",        # Nome com apóstrofo
#     "Jean-Luc",        # Nome com hífen
#     "Renée",           # Nome com acento
#     "Søren Kierkegaard", # Nome com caracteres escandinavos
#     "El Niño",         # Nome com espaço e tilde


def validar_Datanascimento(dataNascimento):
    try:
        # Converte a string para um objeto datetime
        birthdate = datetime.strptime(dataNascimento, '%d/%m/%Y')
    except ValueError:
        # Retorna falso se a data estiver em formato inválido
        return False, "Data inválida."

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

def is_valid_license_plate(plate):
    # Expressão regular para os dois formatos de placas no Brasil
    old_plate_regex = r'^[A-Z]{3}-[0-9]{4}$'    # Formato antigo: ABC-1234
    new_plate_regex = r'^[A-Z]{3}[0-9][A-Z][0-9]{2}$'  # Formato novo: ABC1D23
    
    return r