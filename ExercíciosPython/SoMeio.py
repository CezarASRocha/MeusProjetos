nota_1 = float(input())
nota_2 = float(input())

media = (nota_1 + nota_2) / 2
if media >= 6.00:
    print('aprovado' )
elif media >= 2.00 and nota_1 > 1.99:
    print('talvez com a sub')
else:
   print ('reprovado')