import pickle

cliente = {
  '22233344455': ['Taciano Silva', 'taciano@ufrn.br', '(83) 99900-0111','01/01/01, 00:00:00'], 
  '33344455566': ['Karliane Vale', 'karliane@ufrn.br', '(84) 99999-8888','01/01/01, 00:00:00'],
  '44455566677': ['João Roberto', 'joao@ufrn.br', '(84) 99801-1505','01/01/01, 00:00:00']
}

funcionarios = {
  '11122233344': ['Flavius Gorgônio', 'flavius@ufrn.br', '(84) 99988-8777','01/01/01, 00:00:00'], 
  '22233344455': ['Taciano Silva', 'taciano@ufrn.br', '(83) 99900-0111','01/01/01, 00:00:00'], 
  '33344455566': ['Karliane Vale', 'karliane@ufrn.br', '(84) 99999-8888','01/01/01, 00:00:00']
}

veiculos = {
    'BEE4R22': ['Chevrolet', 'Onix', '2020', 'Branco'],
    'AAA2T33': ['Chevrolet', 'Onix Plus', '2020', 'Vermelho'],
    'BBB3E44': ['Ferrari', 'Ferrari 488 GTB', '2022', 'Branco']
}

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

veiculos ={}
try:
  arq_veiculos = open("veiculos.dat", "rb")
  veiculos = pickle.load(arq_veiculos)
except:
  arq_veiculos = open("veiculos.dat", "wb")
arq_veiculos.close()

