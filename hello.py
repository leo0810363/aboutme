def square(y):
	print("{}的平方是{},三次方是{}".format(y, y*y, y**3))




x = int(input("請輸入整數"))

print("python程式測試", x)
if (x<0):
	print("您輸入的值是負數")
elif (x==0):
	print("您輸入值為0")
else:
	for i in range(1,x+1):
		square(i)