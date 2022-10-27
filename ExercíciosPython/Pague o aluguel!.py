Total_da_Divida = int(input())
Valor_da_Parcela = int(input())
pagamento = 0

while Total_da_Divida > 0:
    pagamento+=1
    print('pagamento:', pagamento)
    print('antes =',  Total_da_Divida )
    Total_da_Divida = Total_da_Divida - Valor_da_Parcela
    if Total_da_Divida <= 0:
        print('depois = 0')
        print('-----')
    else:
        print('depois =', Total_da_Divida)
        print('-----')
