import os
from funcoes import (
    alterarDadosFunc,
    cadastrarFunc,
    cadastrarVeic,
    excluirVeic,
    excluirFunc,
    exibirDadosFunc,
    exibirDadosVeic,
    menuPrincipal,
    modCliente,
    cadastrarCliente,
    excluirCliente,
    modFunc,
    modInfo,
    modRelatorio,
    modReserva,
    modVeic,
    alterarDadosVeic,
    alterarDadosCliente,
    exibirDadosCliente,
    escreverArquivos       
)

###################################################
##### Projeto - Locadora de Carros - Versão 4 #####
###################################################
op_pric = ''
while op_pric != '0':
  op_pric = menuPrincipal()
  
  if op_pric == '1':
    op_cliente = ''
    while op_cliente != '0':
      op_cliente = modCliente()
      
      if op_cliente == '1':
        cadastrarCliente()

      elif op_cliente == '2':
        exibirDadosCliente()

      elif op_cliente == '3':
        alterarDadosCliente()
  
      elif op_cliente == '4':
        excluirCliente()
   
  elif op_pric == '2':
    op_func = ''
    while op_func != '0':
      op_func = modFunc()
           
      if op_func == '1':
        cadastrarFunc()

      elif op_func == '2':
        exibirDadosFunc()

      elif op_func == '3':
        alterarDadosFunc()

      elif op_func == '4':
        excluirFunc()

  elif op_pric == '3':
    op_veic = ''
    while op_veic != '0':
      op_veic = modVeic()

      if op_veic == '1':
        cadastrarVeic()

      elif op_veic == '2':
        exibirDadosVeic()

      elif op_veic == '3':
        alterarDadosVeic()

      elif op_veic == '4':
        excluirVeic()
    
  elif op_pric == '4':
   op_reserva = ''
   while op_reserva != '0':
     op_reserva = modReserva()

  elif op_pric == '5':
    op_relatorio = ''
    while op_relatorio != '0':
      op_relatorio = modRelatorio()
     

  elif op_pric == '6':
    op_pric = modInfo()

print("Você encerrou o programa!")
print("Até logo!")
escreverArquivos()