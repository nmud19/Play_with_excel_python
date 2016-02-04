import pandas as pd
#lets take csv files
csv = pd.read_csv("Finance_Metrics.csv")
#lets extract the data from schools
li = csv['Currency'].values.tolist()
#make a list from the schools
#print(li)
#edit the list by replacing Nan by the school name
holder = li[0]
import numpy as np
x = np.array(li)
#print(x)
#print(x)
li1=[]
print(x[0],type(x[0]),x[1],type(x[1]) )
for item in x:
	print(item, type(item))
	if item == 'nan':
		item = holder
		li1.append(item)
	else:
		holder = item
		li1.append(item)
#reassign the list
csv['Currency'] = li1

csv.columns = ['school_id', 'metric', 'sept', 'oct','nov','dec','jan','feb','march','april','may', 'june', 'july']
##write it back to a csv files
#csv.to_csv('test1.csv',index = False)
print(csv)