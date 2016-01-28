import os
path = 'C:/Users/64Squares/Desktop/Nikhil/financials_automated'
excel_files = [f for f in os.listdir(path) if f.endswith('.xlsx')]

print(excel_files)

#lets check for a particular value or file using regex
import re
# iterate the list 
for item in excel_files:
	p = re.compile('.*SAIS.*',item)
	print(p)
	#if(re.compile('.*SAIS.*',item)):

		#print("Found a match for SAIS")
# if the item matches then out put the school id or something like that
