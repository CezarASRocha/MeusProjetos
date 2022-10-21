a, b, c = map(float, input().split())

tri = (c * a) / 2
print(f'TRIANGULO: {tri:.3f}')

circ = (2 * 3.14159 * c) / 2 * (c)
print(f'CIRCULO: {circ:.3f}')

trap = (a + b) * (c) / 2
print(f'TRAPEZIO: {trap:.3f}')

quad = b ** 2
print(f'QUADRADO: {quad:.3f}')

retan = a * b
print(f'RETANGULO: {retan:.3f}')