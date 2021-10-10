def c(A, D):
    if (A <= D/(2**1/2)):
        return "Да, можно"
    return "Нет, нельзя"
	
while True:
	try:
		D = int(input("Диаметр бревна: "))
		if (D < 0):
		    raise Exception()
		A = int(input("Ширина бруса: "))
		if (A < 0):
		    raise Exception()
		else:
		    print (c(A, D))
	except:
		print("Введите натуральное число.")
		continue
	break