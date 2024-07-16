from dicionarios import funcionarios
import interfaces as ifc 
import validacao as val
from datetime import datetime

#########################
#####   Cadastrar   #####
#########################
def cadastrarFunc():
  ifc.cabecalhoModulos("Cadastrar Funcionário")
  nome = input("👤 Nome: ")
  print()
  cpf = input("🆔 CPF: ")
  cpf = val.formatar_cpf(cpf)
  print()
  email = input("📧 Email: ")
  print()
  fone = input("📞 Celular: ")
  print()
  dataNascimento = input("🎂 Data de Nascimento (00/00/0000): ")
  dataNascimento = val.formatar_data(dataNascimento)
  print()
  data = datetime.now()
  funcionarios[cpf] = [nome,email,fone,dataNascimento,data.strftime("%x, %X")]
  print("✅ Funcionário cadastrado com sucesso!")
  input("Tecle <ENTER> para continuar...")

#########################
#####     Exibir    #####
#########################
def exibirDadosFunc():
  ifc.cabecalhoModulos("Exibir Dados do Funcionário")
  cpf = input('❱ Qual o CPF do funcionário(a)? ')
  cpf = val.formatar_cpf(cpf)
  print()
  if cpf in funcionarios:
      print("👤 Nome: ", funcionarios[cpf][0])
      print("🆔 CPF: ", cpf)
      print("📧 Email: ", funcionarios[cpf][1])
      print("📞 Celular: ", funcionarios[cpf][2])
      print("🎂 Data de Nascimento: ", funcionarios[cpf][3])
  else:
      print('❌ Funcionário(a) inexistente!')
  print()
  input("Tecle <ENTER> para continuar...")

#########################
#####    Alterar    #####
#########################
def alterarDadosFunc():
  ifc.cabecalhoModulos("Alterar Dados do Funcionário")
  cpf = input('❱ Qual o CPF do funcionário(a)? ')
  cpf = val.formatar_cpf(cpf)
  if cpf in funcionarios:
      dadosFuncionarios = funcionarios[cpf]
      print("❱ Informe os novos dados ou deixe o campo em branco para não alterar a informação.")
      nome = input(f"👤 Nome ({dadosFuncionarios[0]}: )").strip()
      email = input(f"📧 Email ({dadosFuncionarios[1]}): ").strip()
      fone = input(f"📞 Celular ({dadosFuncionarios[2]}): ").strip()
      dataNascimento = input(f"🎂 Data de Nascimento ({dadosFuncionarios[3]}): ").strip()
      # Atualiza apenas os campos que não estão vazios, permitindo que a informação anterior continue a mesma.
      if nome:
          funcionarios[cpf][0] = nome
      if email:
          funcionarios[cpf][1] = email
      if fone:
          funcionarios[cpf][2] = fone
      if dataNascimento:
          funcionarios[cpf][3] = dataNascimento

      print('\n✅ Dados alterados com sucesso!')
  else:
      print('\n❌ Funcionário(a) inexistente!')

  input("Tecle <ENTER> para continuar...")

#########################
#####    Excluir    #####
#########################
def excluirFunc():
  ifc.cabecalhoModulos("Excluir Funcionário")
  cpf = input('❱ Informe o CPF do funcionário(a): ')
  cpf = val.formatar_cpf(cpf)
  if cpf in funcionarios:
      print("👤 Nome: ", funcionarios[cpf][0])
      print("📧 Email: ", funcionarios[cpf][1])
      print("📞 Celular: ", funcionarios[cpf][2])
      print("🎂 Data de Nascimento: ", funcionarios[cpf][3])
      print()
      resp = input('❱ Tem certeza que deseja excluir este funcionário(a)? (Sim/Não)').upper()
      if resp == 'SIM':
          del funcionarios[cpf]
          print("✅ Funcionário(a) excluído com sucesso!")
      else:
          print('🚫 Exclusão não realizada!')
  else:
      print("❌ Funcionário inexistente!")
  input("Tecle <ENTER> para continuar...") 