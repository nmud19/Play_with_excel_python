import pandas as pd
def add_more(result):
	result1 = pd.DataFrame()
	result1['hello'] = [1,2,3,4,5,6,7,8]
	result1['kajumba'] = [3,4,6,1,3,4,6,1]
	#print(result1)
	result = pd.merge(result,result1,how = 'right', on='hello')
	return result

#main
df = pd.read_excel("AISS_SAIS_P&L_DEC_2015.xlsx")
result = pd.DataFrame()
result['hello'] = [1,2,3,4]
name = 'world'
result[name] = [11,22,33,44]
result = add_more(result)
print(result)
