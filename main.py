import os
from funcoes import (
    alterarDadosFunc,
    cadastrarFunc,
    cadastrarVeic,
    excluirFunc,
    excluirVeic,
    exibirDadosFunc,
    exibirDadosVeic,
    menuPrincipal,
    modCliente,
    cadastrarCliente,
    excluirCliente,
    exibirDadosCliente,
    alterarDadosCliente,
    modFunc,
    modInfo,
    modRelatorio,
    modReserva,
    modVeic,
    alterarDadosVeic
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
        op_cliente = cadastrarCliente()

      elif op_cliente == '2':
        op_cliente = exibirDadosCliente()

      elif op_cliente == '3':
        op_cliente = alterarDadosCliente()
  
      elif op_cliente == '4':
        op_cliente = excluirCliente()
   
  elif op_pric == '2':
    op_func = ''
    while op_func != '0':
      op_func = modFunc()
           
      if op_func == '1':
        op_func = cadastrarFunc()

      elif op_func == '2':
        op_func = exibirDadosFunc()

      elif op_func == '3':
        op_func = alterarDadosFunc()

      elif op_func == '4':
        op_func = excluirFunc()

  elif op_pric == '3':
    op_veic = ''
    while op_veic != '0':
      op_veic = modVeic()

      if op_veic == '1':
        op_veic = cadastrarVeic()

      elif op_veic == '2':
        op_veic = exibirDadosVeic()

      elif op_veic == '3':
        op_veic = alterarDadosVeic()

      elif op_veic == '4':
        op_veic = excluirVeic()
    
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
