import pandas as pd
#lets take csv files
csv = pd.read_excel("Finance_Metrics.xlsx")
#lets extract the data from schools
li = csv['Currency'].values.tolist()
#make a list from the schools
#print(li)
#edit the list by replacing Nan by the school name
holder = li[0]
import numpy as np
x = np.array(li)
li1=[]
for item in x:
	if item == 'nan':
		item = holder
		li1.append(item)
	else:
		holder = item
		li1.append(item)
#reassign the list
csv['Currency'] = li1

##write it back to a csv files
csv.to_excel('test1.xlsx',index = False)

print(csv['SGD'])


