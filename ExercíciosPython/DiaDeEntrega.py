compra = input()
prazo = int(input())

if compra == 'domingo':
    dia = 1

if compra == 'segunda':
    dia = 2

if compra == 'terca':
    dia = 3

if compra == 'quarta':
    dia = 4

if compra == 'quinta':
    dia = 5

if compra == 'sexta':
    dia = 6

if compra == 'sabado':
    dia = 7

entrega = prazo +  dia

if entrega > 7:
    entrega = entrega - 7

if entrega == dia:
    print('chega hoje!')

elif entrega == 1:
    print('sera entregue ' + 'domingo')

elif entrega == 2:
    print('sera entregue ' + 'segunda')

elif entrega == 3:
    print('sera entregue ' + 'terca')

elif entrega == 4:
    print('sera entregue ' + 'quarta')

elif entrega == 5:
    print('sera entregue ' + 'quinta')

elif entrega == 6:
    print('sera entregue ' + 'sexta')

elif entrega == 7:
    print('sera entregue ' + 'sabado')
