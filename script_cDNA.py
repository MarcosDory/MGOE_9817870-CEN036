import sys
#Atribuindo valores importados para as variáveis
DNA=sys.argv[1]
n1=int(sys.argv[2])
n2=int(sys.argv[3])
n3=int(sys.argv[4])
n4=int(sys.argv[5])
#Fazendo a correção numerica para os valores do index Python
n1=n1-1
n2=n2-1
n3=n3-1
n4=n4-1
#Verificando se os numeros inseridos são menores que a sequência de DNA
#A variável Y será 2 se os números estiverem corretamente inserido e 4 se forem maiores, assim poderá ser criada uma lógica para realizar a concatenação 
k=len(DNA)
Y=2
if n1 < k:
 print('Valor aceitável para n1')
else:
 print('Valor de n1 superior ao tamanho da sequência de DNA')
 Y=4
if n2 < k:
 print('Valor aceitável para n2')
else:
 print('Valor de n2 superior ao tamanho da sequência de DNA')
 Y=4
if n3 < k:
 print('Valor aceitável para n3')
else:
 print('Valor de n3 superior ao tamanho da sequência de DNA')
 Y=4
if n4 < k:
 print('Valor aceitável para n4')
else:
 print('Valor de n4 superior ao tamanho da sequencia de DNA')
 Y=4
#Colocando em maiúsculo as bases nitrogenadas para evitar erro
DNA.upper()
#Cortando as áreas específicas
CDS1=DNA[n1:n2]
CDS2=DNA[n3:n4]
#testando se DNA é uma string:
if isinstance(DNA, str) == True:
 print('DNA inserido corretamente')
else:
 print('DNA inserido incorretamente')
#testando a presença de ATG e dos códons de parada TAG,TAA,TGA:
n01=n1+3
n04=n4-3
n04=int(n04)
if DNA[n1:n01] == 'ATG':
 print('ATG encontrado corretamente em n1')
 Éxon=CDS1+CDS2
 if Y < 3:
  if DNA[n04:n4] == 'TAG':
   print('Códon de parada TAG encontrado na região n4 em CDS 2')
   print('CDS1+CDS2=',Éxon)
  elif DNA[n04:n4] == 'TAA':
   print('Códon de parada TAA encontrado na região n4 em CDS 2')
   print('CDS1+CDS2=',Éxon)
  elif DNA[n04:n4] == 'TGA':
   print('Códon de parada TGA encontrado na região n4 em CDS 2')
   Éxon=CDS1+CDS2
   print('CDS1+CDS2=',Éxon)
  else:
   print('Não foi ncontrado nenhum códon de parada na regíão n4 de CDS 2')
 else:
  print('Valores inseridos para recortar o DNA são  maiores que a sequencia do DNA assim a operação não será realizada')
else:
 print('ATG não encontrado em CDS 1')



