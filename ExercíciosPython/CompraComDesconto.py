compra = float(input())
qntdd = int(input())
if qntdd <= 40:
    
    total = compra * qntdd
    print('{:.2f}'.format(total))
    
    desc = total * 0.1
    
    desc_total = total * qntdd * 0.01
    
    desc_compra = total - desc_total - desc 
    print('{:.2f}'.format(desc_compra))
