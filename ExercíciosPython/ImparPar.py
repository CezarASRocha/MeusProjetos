num = int(input())
impar = 0
par = num % 2
if par == 0:
	num = num - 1
	impar = num + 3
	print(num, impar)
else:
	num = num + 1
	impar = num - 3
	print (impar, num)