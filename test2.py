def return_list():
	li = [1,2,3,4,5]
	return li

li1 = [11,22,33,44,55]
li2 = li1 + return_list()
print(li2)
li2 = [0:]