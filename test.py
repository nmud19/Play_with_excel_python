import numpy as np
li1 = [10,20,30,40,50]
li2 = [5,4,3,2,1]
li1 = np.array(li1)
li2 = np.array(li2)

li3 =  li1 / li2
li3 = li3.tolist()
print(li3)