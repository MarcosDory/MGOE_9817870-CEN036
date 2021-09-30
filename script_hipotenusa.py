import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
if isinstance(a, int) == True:
 a=int(sys.argv[1])
 if isinstance(b, int) == True:
  b=int(sys.argv[2])
  a=a*a
  b=b*b
  c=a+b
  print(c)
else:
 print('valor atribuido deve ser um número inteiro')

