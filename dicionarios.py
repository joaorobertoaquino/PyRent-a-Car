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
    "BEE5T23": [
        {
          'cpf_cliente': '123.456.789-00',
          'nome_cliente': 'João Roberto Galvão Aquino',
          'data_inicio': '06/10/2024',
          'hora_inicio': '08:00:00',
          'data_fim': '06/12/2024',
          'hora_fim': '12:00:00',
          'status': False  
        }
    ]
}

valor_aluguel = {
  "seda": 120.00,
  "suv": 150.00,
  "hatch": 100.00,
  "pickup": 200.00,
  "crossover": 140.00,
  "perua": 130.00,
  "conversivel": 250.00,
  "coupe": 180.00,
  "minivan": 160.00,
  "van": 180.00,
  "esportivo": 300.00,
  "eletrico": 220.00,
  "hibrido": 200.00
}

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

