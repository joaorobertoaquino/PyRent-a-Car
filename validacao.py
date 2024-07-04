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
