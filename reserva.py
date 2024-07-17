from datetime import datetime, timedelta
from dicionarios import clientes, veiculos, valor_aluguel, historico_aluguel
import validacao as val
import interfaces as ifc

def reservarVeiculo():
  ifc.cabecalhoModulos("Reservar Veículo")
  placa = input("❱ Informe a placa do veículo a ser alugado: ").upper()
  if placa in veiculos and not veiculos[placa]['alugado']:
      dias = int(input("\n❱ Por quantos dias o veículo será alugado? "))
      data_inicio = datetime.now().strftime("%d/%m/%Y")
      hora_inicio = datetime.now().strftime("%H:%M:%S")
      data_fim = (datetime.now() + timedelta(days=dias)).strftime("%d/%m/%Y")
      preco = valor_aluguel[veiculos[placa]['categoria']]

      nome_cliente = input("\n❱ 👤 Informe o nome do cliente: ")
      cpf_cliente = input("\n❱ 🆔 CPF do cliente: ")
      cpf_cliente = val.formatar_cpf(cpf_cliente)

      if cpf_cliente in clientes:
          if clientes[cpf_cliente][0] == nome_cliente:
              veiculos[placa]['alugado'] = True
              veiculos[placa]['data_inicio'] = data_inicio
              veiculos[placa]['data_fim'] = data_fim

              if placa not in historico_aluguel:
                  historico_aluguel[placa] = []
              historico_aluguel[placa].append({
                  'cpf_cliente': cpf_cliente,
                  'nome_cliente': nome_cliente,
                  'data_inicio': data_inicio,
                  'hora_inicio': hora_inicio,
                  'data_fim': data_fim,
                  'hora_fim': None,
                  'status': True
              })
              print("\nPreço da diária: R$ ", preco)
              print(f"\n✅ Veículo {veiculos[placa]['modelo']} alugado com sucesso até {data_fim}!")
          else:
              print("🚫 Nome do cliente não corresponde ao CPF informado.")
      else:
          print("🚫 Cliente não cadastrado.")
  else:
      print("🚫 Veículo não encontrado ou já está alugado.")
  input("\nTecle <ENTER> para continuar...")


def devolverVeiculo():
  ifc.cabecalhoModulos("Devolver Veículo")
  placa = input("❱ Digite a placa do veículo a ser devolvido: ").upper()

  if placa in veiculos and veiculos[placa]['alugado']:
      cpf_cliente = input("❱ CPF do cliente: ")
      cpf_cliente = val.formatar_cpf(cpf_cliente)
      data_fim = datetime.now().strftime("%d/%m/%Y")
      hora_fim = datetime.now().strftime("%H:%M:%S")

      devolucao_valida = False
      for aluguel in historico_aluguel[placa]:
          if aluguel['cpf_cliente'] == cpf_cliente and aluguel['status']:
              devolucao_valida = True
              aluguel['data_fim'] = data_fim
              aluguel['hora_fim'] = hora_fim
              aluguel['status'] = False
              veiculos[placa]['alugado'] = False
              break

      if devolucao_valida:
          print(f"\n✅ Veículo {veiculos[placa]['modelo']} devolvido com sucesso!")
      else:
          print("\n🚫 CPF não corresponde ao cliente que alugou o veículo.")
  else:
      print("\n🚫 Veículo não encontrado ou não está alugado.")
  input("\nTecle <ENTER> para continuar...")


def veiculosDisponiveis():
  ifc.interface_Veiculosdisponiveis()
  for placa, dados in veiculos.items():
      if not dados ['alugado']:
          print("| %-9s "%placa, end='')
          print("| %-15s "%dados['marca'], end='')
          print("| %-18s "%dados['modelo'], end='')
          print("| %-5s "%dados['ano'], end='')
          print("| %-15s "%dados['cor'], end='')
          print("| %-9s "%dados['categoria'], end='')
          print("| %-18s "%dados['data_cadastro'], end='')
          print("| %-16s |"%dados['hora_cadastro'])
  print("|-----------|-----------------|--------------------|-------|-----------------|-----------|--------------------|------------------|")
  print()
  input("Tecle <ENTER> para continuar...")

def veiculosAlugados():
  ifc.interface_Veiculosalugados()
  for placa, dados in veiculos.items():
      if dados['alugado']:
          print("| %-9s "%placa, end='')
          print("| %-15s "%dados['marca'], end='')
          print("| %-18s "%dados['modelo'], end='')
          print("| %-5s "%dados['ano'], end='')
          print("| %-15s "%dados['cor'], end='')
          print("| %-9s "%dados['categoria'], end='')
          print("| %-19s "%dados['data_inicio'], end='')
          print("| %-20s "%dados['data_fim'], end='')
          if placa in historico_aluguel:
              # Encontrar o registro ativo (status True)
              for aluguel in historico_aluguel[placa]:
                  if aluguel['status']:
                      print("| %-35s |" % aluguel['nome_cliente'])
                      break
              else:
                  print("| %-35s |" % "Nome não encontrado")
          else:
              print("| %-35s |" % "Não Informado")

  print("|-----------|-----------------|--------------------|-------|-----------------|-----------|---------------------|----------------------|-------------------------------------|")
  input("Tecle <ENTER> para continuar...")


def politicaCombustivel():
  ifc.interface_Politicacombustivel()
  input("\nTecle <ENTER> para continuar...")