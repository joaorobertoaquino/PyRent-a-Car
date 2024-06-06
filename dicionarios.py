import pickle
from collections import Counter

cliente = {
  '22233344455': ['João Roberto', 'joaoroberto@gmail.com', '(84) 998011505', '00:00:00']
}
funcionarios = {
  '22233344455': ['Alberto', 'albertoroberto@gmail.com', '(84) 998011506', '00:00:00']
}
veiculos_disponiveis = {
  'BEE4R22': ['Chevrolet', 'Onix', '2020', 'Branco', '00:00:00']
}
veiculos_alugados = {
  'BEE5T23': ['Chevrolet', 'Onix', '2023', 'Preto', '00:00:00']
}
alugueis_por_veiculo = {
  "FGH4D29": 5,
}  # Dicionário para contar o número de alugueis de cada veículo


#########################################################
#####            Carregar Dados                     #####
#########################################################
cliente = {}
try:
  arq_cliente = open("cliente.dat", "rb")
  cliente = pickle.load(arq_cliente)
except:
  arq_cliente = open("cliente.dat", "wb")
  arq_cliente.close()

funcionarios = {}
try:
  arq_funcionarios = open("funcionarios.dat", "rb")
  funcionarios = pickle.load(arq_funcionarios)
except:
  arq_funcionarios = open("funcionarios.dat", "wb")
arq_funcionarios.close()

veiculos_disponiveis ={}
try:
  arq_veiculos_disponiveis = open("veiculos_disponiveis.dat", "rb")
  veiculos_disponiveis = pickle.load(arq_veiculos_disponiveis)
except:
  arq_veiculos_disponiveis = open("veiculos_disponiveis.dat", "wb")
arq_veiculos_disponiveis.close()

veiculos_alugados={}
try:
  arq_veiculos_alugados = open("veiculos_alugados.dat", "rb")
  veiculos_alugados = pickle.load(arq_veiculos_alugados)
except:
  arq_veiculos_alugados = open("veiculos_alugados.dat", "wb")
arq_veiculos_alugados.close()

alugueis_por_veiculo={}
try:
  arq_alugueis_por_veiculo = open("alugueis_por_veiculo.dat", "rb")
  alugueis_por_veiculo = pickle.load(arq_alugueis_por_veiculo)
except:
  arq_alugueis_por_veiculo = open("alugeuis_por_veiculo.dat", "wb")
arq_alugueis_por_veiculo.close()
