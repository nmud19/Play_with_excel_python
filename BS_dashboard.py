from datetime import datetime
from pprint import pprint
import pandas as pd
import datetime


month_column_list = ['school_id', 'metric', 'remark' , 'note', 'sep2012', 'oct2012', 'nov2012', 'dec2012', 'jan2013' , 'feb2013', 'mar2013', 'apr2013', 'may2013', 'jun2013', 'jul2013', 'aug2013','sep2013', 'oct2013', 'nov2013', 'dec2013', 'jan2014' , 'feb2014', 'mar2014', 'apr2014', 'may2014', 'jun2014', 'jul2014', 'aug2014', 'sep2014', 'oct2014', 'nov2014', 'dec2014', 'jan2015' , 'feb2015', 'mar2015', 'apr2015', 'may2015', 'jun2015', 'jul2015', 'aug2015', 'sep2015', 'oct2015', 'nov2015', 'dec2015', 'jan2016' , 'feb2016']

#future parameters include year and month
def BS_sanitise_file(res):
	for item in month_column_list:
		if(item == 'sep2015' ):
			break
		else:
			if(item == 'school_id' or item == 'metric'):
				pass
			else:
				del df[item]
	return res

#main prog

df = pd.read_excel("AISS_SAIS_DASHBOARD_DEC_2015.xlsx",skiprows = 1)
#print(len(df.columns) , len(month_column_list))
df.columns = month_column_list
df = BS_sanitise_file(df)




print(df['metric'])

