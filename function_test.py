import numpy as np #numpy library
import pandas as pd # the pandas used for dataframe
import os #this header required for the file path variable
import re #this import required foir regular expressions module
excel_files = [] # this is the variable holding the file names
#these two variables are required for us to write in the file
month = 0
year = 0

#this function takes in the predefined path name for the directory and then returnsd the file names in the excel_files varuiable
def cache_all_file_names():
	#the path to the directory and sub directory
	rootdir = 'C:/Users/64Squares/Desktop/Nikhil/financials'
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			excel_files.append(os.path.join(subdir, file))
	return excel_files


#this program will define the regex for the particular files
def identify_file(month,year):
	#lets try some regex first
	#regex_aiss = re.compile(r".*ais+.*", re.I)
	regex = '.*sais+.*P&L.*' + re.escape(month) + '.*' + re.escape(year) + '.*'
	# re.escape elimintes the need for special characters
	regex_sais = re.compile(regex, re.I)
	for file_name in excel_files:
	    #for sasi
	    if (regex_sais.match(file_name)):
	    	print("Found sais: ", file_name)
	return

#this function will be called if the input file type is P&L	
def sanitise_the_file_PnL():
	li = csv['Currency'].values.tolist()
	holder = li[0]
	import numpy as np
	x = np.array(li)
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
	return csv

#this function will add two metrics to give out a resultant metric 
#input will be the the column name1 and 2(for added security), the global dataframe, the row name ,ie, school name and the metric to be added's name.
#resultant metric will be in form of a list
def add_two_metrics(column_name1, column_name2, metric1, metric2, school_name_as_in_xlfile,month):
	li = csv[(csv[column_name1] == metric1) & (csv[column_name2]==school_name_as_in_xlfile)] 
	li = li.values.tolist()
	li1 = csv[(csv[column_name1] == metric2) & (csv[column_name2]==school_name_as_in_xlfile)] 
	li1 = li1.values.tolist()
	li = li[0]
	li = li[2:]
	li1 = li1[0]
	li1 = li1[2:]
	li2 = ( np.array(li) + np.array(li1) ).tolist()
	print(li)
	print(li1)
	print(li2)
	return li2


#main program

#CODE to extract all excel file names into the variable
excel_files = cache_all_file_names()
#print(excel_files)
#this identifys the file type like PnL or capex or etc.
identify_file('DEC', '2015')
#reading the file --function not yet ready
csv = pd.read_excel("AISS_SAIS_P&L_DEC_2015.xlsx")
#sanitise_the_file_PnL()
add_two_metrics('metric','school_id','Gross Fees','Discounts','Total Stamford AIS','dec')
print("end of loop")