# num1 = [ 10, 5, 20, 0, 40, 45, 50]
# num2 = [40, 5, 10]

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

flag = 0
for i in range(len(num2)):
	if ( num2[i] in num1 ):
		continue
	else:
		print ("False")
		break
else:
	print ("True")
