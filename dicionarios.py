import pickle

clientes = {
  '22233344455': ['João Roberto', 'joaoroberto@gmail.com', '(84) 998011505', '07/10/2005', '00:00:00']
}
funcionarios = {
  '22233344455': ['Alberto', 'albertoroberto@gmail.com', '(84) 998011506', '02/04/2000', '00:00:00']
}

veiculos = {
  'BEE5T23': {
        'marca': 'Chevrolet',
        'modelo': 'Onix',
        'ano': '2023',
        'cor': 'Preto',
        'categoria': 'B',
        'data_cadastro': '06/26/24',
        'hora_cadastro': '00:00:00',
        'alugado': True,
        'data_inicio': '06/10/2024',
        'data_fim': '06/10/2024',
    }
}

historico_aluguel = {
    "ABC1234": {
        'cpf_cliente': '123.456.789-00',
        'nome_cliente': 'João Roberto Galvão Aquino',
        'data_fim': '06/12/2024',
        'status': True  
    }
}


alugueis_por_veiculo = {
  "FGH4D29": 5,
}  # Dicionário para contar o número de alugueis de cada veículo. 

valor_aluguel = {
  "A" : 120.00,
  "B" : 150.00
} #Dicionário para contar os números de vezes que os veículos fora, alugados.

#########################################################
#####            Carregar Dados                     #####
#########################################################

historico_aluguel = {}
try:
  arq_historico_aluguel = open("historico_aluguel.dat", "rb")
  historico_aluguel = pickle.load(arq_historico_aluguel)
except:
  arq_historico_aluguel = open("historico_aluguel.dat", "wb")
  arq_historico_aluguel.close()

clientes = {}
try:
  arq_clientes = open("clientes.dat", "rb")
  clientes = pickle.load(arq_clientes)
except:
  arq_clientes = open("clientes.dat", "wb")
  arq_clientes.close()

funcionarios = {}
try:
  arq_funcionarios = open("funcionarios.dat", "rb")
  funcionarios = pickle.load(arq_funcionarios)
except:
  arq_funcionarios = open("funcionarios.dat", "wb")
arq_funcionarios.close()

veiculos ={}
try:
  arq_veiculos = open("veiculos.dat", "rb")
  veiculos = pickle.load(arq_veiculos)
except:
  arq_veiculos= open("veiculos_.dat", "wb")
arq_veiculos.close()

alugueis_por_veiculo={}
try:
  arq_alugueis_por_veiculo = open("alugueis_por_veiculo.dat", "rb")
  alugueis_por_veiculo = pickle.load(arq_alugueis_por_veiculo)
except:
  arq_alugueis_por_veiculo = open("alugeuis_por_veiculo.dat", "wb")
arq_alugueis_por_veiculo.close()

