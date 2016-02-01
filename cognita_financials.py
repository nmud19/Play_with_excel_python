import pandas as pd
from functools import reduce
import itertools
nf=[]
# import the xlsx file 
xlsx = pd.read_excel("SAIS AIS P&L - Dec'15.xlsx", skiprows = 6)
print("This is the line")
# accessing the rows in the dataframe
col = 2 #initial to 15
#gross fees
gross_fees_df = xlsx[xlsx.columns[2:]][1:2]
#this gives a 2d list
gross_fees_2dlist = gross_fees_df.values.tolist()
# flattenning out the list
gross_fees_2dlist = list(itertools.chain(*gross_fees_2dlist))
gross_fees = gross_fees_2dlist #gross fees holds the gross_fees of sais school

# discount
damm = xlsx[xlsx.columns[2:3]][2:3]
damm = damm.values.tolist()
discount = 0.34
for item in damm:
	print(item[0])
	print(type(item))
	discount = item[0]

#net fees
net_fees = gross_fees + discount
nf.append(net_fees)
print(net_fees)