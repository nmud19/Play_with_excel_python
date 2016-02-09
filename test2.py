import pandas as pd
result = pd.DataFrame()
def add_more(result):
	result1 = pd.DataFrame()
	result1['hello'] = [1,2,3,4,5,6,7,8]
	result1['kajumba'] = [3,4,6,1,3,4,6,1]
	#print(result1)
	result = pd.merge(result,result1,how = 'right', on='hello')
	return result
def extract_metric(metric_name, school_id, month):
	try:
		result = df[(df['metric'] == metric_name) & (df['school_id'] == school_id)]
		result = result.ix[:,'sept':month]
		result = result.values.tolist()
		result = result[0]
	except : 
		'''hardcoded values as budget does not have this '''
		return [0,0,0,0,0,0,0,0,0,0,0,0]
	return result
#main
df = pd.read_excel("AISS_SAIS_P&L_DEC_2015.xlsx")
result2 = extract_metric('Total Revenue', 'Total Stamford AIS','dec')
'''print(result2)
fy_ytd=0
ytd = []
for item in result2:
	fy_ytd = fy_ytd + item
	ytd = ytd + [fy_ytd]

print(ytd)

'''

li = [1,2,3,4,5]
li = li * 12
print(li)