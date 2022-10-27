VicCoin = float(input())
soma_quantidade = 0

while VicCoin !=-1:
    VicCoin = float(input())
    soma_quantidade += 1
    if VicCoin == -1:
        soma_quantidade += 1
        reais = VicCoin * 2.50
        print(f'VC$ {VicCoin:.2f}')
        print(f'R$ {reais:.2f}')