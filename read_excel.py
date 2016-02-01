import pandas as pd
#lets take csv files
csv = pd.read_excel("AISS_SAIS_P&L_DEC_2015.xlsx")
#lets extract the data from schools
li = csv['school_id'].values.tolist()
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
csv['school_id'] = li1
csv.columns = ['school_id', 'metric', 'sept', 'oct','nov','dec','jan','feb','march','april','may', 'june', 'july', 'aug','total_year']
##write it back to a csv files
csv.to_excel('AISS_SAIS_P&L_DEC_2015.xlsx',index = False)
print(csv.ix[7:9,'school_id':'dec'])

"""#code to add the two metrics to give a resultant one
li = csv[(csv['SGD'] == 'Gross Fees') & (csv['Currency']=='Total Stamford AIS')] 
li = li.values.tolist()
li1 = csv[(csv['SGD'] == 'Discounts') & (csv['Currency']=='Total Stamford AIS')] 
li1 = li1.values.tolist()
li = li[0]
li = li[2:]
li1 = li1[0]
li1 = li1[2:]
print(li)
print(li1)
li2 = ( np.array(li) + np.array(li1) ).tolist()
print(li2)"""