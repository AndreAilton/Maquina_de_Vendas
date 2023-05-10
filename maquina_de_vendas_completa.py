# -*- coding: utf-8 -*-
"""Maquina de vendas completa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SCGil5q__cBXEU8eNwWn2fe2-BnGGaBx
"""

#=============BANCO DE DADOS============================
Lista =  open('Banco de dados.txt','r')
Linhas= Lista.readlines()

for c in Linhas:     
    if c[2] == 'V':
       c = c.replace(' ', '')
       ValorItem = eval(c)
        
    elif c[2] == 'Q':
       c = c.replace(' ', '')
       QItem = eval(c)
    elif c[2] == 'L':
       c = c.replace(' ', '')
       Lucro = eval(c)
    else:
       c = c.replace(' ', '')
       itens = eval(c)
#=============BANCO DE DADOS============================
#VARIAVEIS DECLARADADS
confirmo="S"
confirm ="S"
saldo = 0
Vendas = 0
Dinheiro1 = 0
Nitem = 12345
#-----------------------------
#fUNÇÕES INVOCAVEIS
#-----------------------------

#função para mudar quantidade

#Base Valor Maquina====================
def tabelaitens():
  print("""  =======MAQUINA DE VENDAS=======
  Itens                    | {}
  [1] Chocolate            | {}
  [2] Refrigerante         | {}
  [3] Salgadinho           | {}
  [4] Bolacha              | {}
  [5] Agua                 | {}
  [6] Balas                | {}
  [7] Sorvete              | {}
  [8] Chiclete             | {}
  [9] Caramelo             | {}
  ===============================""".format(ValorItem[0],ValorItem[1],ValorItem[2],ValorItem[3],ValorItem[4],ValorItem[5],ValorItem[6],ValorItem[7],ValorItem[8],ValorItem[9]))

#Base Estoque Maquina=======================
def tabelaitensq():
  print("""  =======MAQUINA DE VENDAS=======
  QUAL ITEM DESEJA ALTERAR QUANTIDADE
  Itens                    | {}
  [1] Chocolate            | {}
  [2] Refrigerante         | {}
  [3] Salgadinho           | {}
  [4] Bolacha              | {}
  [5] Agua                 | {}
  [6] Balas                | {}
  [7] Sorvete              | {}
  [8] Chiclete             | {}
  [9] Caramelo             | {}
  ===============================""".format(QItem[0],QItem[1],QItem[2],QItem[3],QItem[4],QItem[5],QItem[6],QItem[7],QItem[8],QItem[9]))

#Base Controle Mestre================
def tabelaitens0():
  print("""  =======MAQUINA DE VENDAS=======
  ALTERAÇÃO DO VALOR E QUANTIDADE   
  ===============================
  [0] VALOR         
  [1] QUANTIDADE
  [2] Lucro
  [3] Retornar a maquina      
  ===============================""")

#Escolha do estoque==================
def Escolhaestoque():
  confirm = "N"
  while (confirm=="N"):
    Nitem = int(input("Escolha um item -->"))
    confirm = input("Voce escolheu {} que possui {} e custa {}$ reais no estoque Confirma S/N \n---->".format(itens[Nitem], QItem[Nitem],ValorItem[Nitem]))
    confirm = confirm.upper()
  else:
    pass
  return Nitem

#Escolher valores  ===============
def Escolha():
  confirm = "S"
  while confirm == "S":
    Nitem1 = int(input("O item desejado "))
    if Nitem1 <10 :
      Nitem = Nitem1
      if QItem[Nitem] == 0:
        confirm = str(input("Produto indisponivel Quer Escolher outro S/N \n---->" ))
        confirm = confirm.upper()
      else:
        confirm = input("Voce escolheu {} que custa {}$ Confirma S/N \n----> ".format(itens[Nitem], ValorItem[Nitem]))
        confirm = confirm.upper()
        if confirm == "S":
          return Nitem
        else:
          confirm = "S"
    elif Nitem1 >9 and Nitem1<1200 :
        confirm = str(input("Produto Incorreto Quer Escolher outro S/N \n---->" ))
        confirm = confirm.upper()
    else:
      Nitem1 == 123123 #SENHA
      return 123123  #SENHA
  else: 
    pass
  return 0

#DEFINIR SALDO====================
def Saldo():
  global saldo
  print('Seu saldo e de {}'.format(saldo))
  if saldo >= ValorItem[Nitem]:
    saldo += -ValorItem[Nitem]
    return saldo
  else:
    saldo += int(input("Insira o Valor de {}$ reais\n --->".format(ValorItem[Nitem]-saldo)))
    while saldo<ValorItem[Nitem]:
      print("coloque ",ValorItem[Nitem] - saldo,"$ reais")
      saldo += int(input("-->")) 
    saldo += -ValorItem[Nitem]
    return saldo
#=======================================================================
#============================CODIGO PRINCIPAL===========================
while (confirm=="S") or (confirmo1 == "S"):
  tabelaitens()
  Nitem = Escolha()
  if Nitem == 0:
    confirm = "N"
    confirmo1 = "N"
  else:
    if Nitem == 123123: #DEFINIR SENHA
      while (confirmo =="S"):
        tabelaitens0()
        Nitem = int(input("--->"))
        if Nitem == 1:
          tabelaitensq()
          Nitem = Escolhaestoque()
          QItem[Nitem] += int(input("Adicione uma quantidade"))
          print("Valor alterado com sucesso")
          print(itens[Nitem],"possui",QItem[Nitem],"no estoque")
          confirmo = input("Deseja Continuar S/N")
          confirmo = confirmo.upper()
          confirm = confirmo
        elif Nitem == 2:
          print("Foram feitas {} Vendas \nrecebemos {}$ Reais no total".format(Lucro[1],Lucro[2]))
        elif Nitem == 0:
          tabelaitens()
          Nitem = Escolhaestoque()
          ValorItem[Nitem] = int(input("insira novo valor"))
          print("Valor alterado com sucesso")
          print(ValorItem[Nitem])
          confirmo = input("Deseja Continuar S/N")
          confirmo = confirmo.upper()
          confirm = confirmo
  
        elif Nitem == 3:
          confirm = "S"
          confirm = confirm.upper()
          confirmo = "S"
    else:
      if confirmo == "N":
        Lista =  open('Banco de dados.txt','w')
        Lista.write('{}\n{}\n{}\n{}'.format(itens,ValorItem,QItem,Lucro))
        pass
      else:
        saldo = Saldo()
        QItem[Nitem] += -1
        Lucro[1] += 1
        Lucro[2] += ValorItem[Nitem]
        print("Compra feita com sucesso")
        confirmo1 = (input("seu saldo atual e de {} escolher outro produto S/N -->".format(saldo)))
        confirmo1 = confirmo1.upper()
        confirm = "N"
        Lista =  open('Banco de dados.txt','w')
        Lista.write('{}\n{}\n{}\n{}'.format(itens,ValorItem,QItem,Lucro))
  print("seu troco e de",saldo,"$ reais")
  Lista =  open('Banco de dados.txt','w')
  Lista.write('{}\n{}\n{}\n{}'.format(itens,ValorItem,QItem,Lucro))