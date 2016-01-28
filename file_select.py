import os
path = 'C:/Users/64Squares/Desktop/Nikhil/financials_automated'
excel_files = [f for f in os.listdir(path) if f.endswith('.xlsx')]
print(excel_files)

#lets check for a particular value of the excel_files

#lets try some regex first
import re
regex_sais = re.compile(r".*sais+.*", re.I)
regex_aiss = re.compile(r".*ais+.*", re.I)

#lets check into the list of excel files we have
for file_name in excel_files:
	#for sasi
	if (regex_sais.match(file_name)):
		print("Found sais: ", file_name)
	#for aiss
	if (regex_aiss.match(file_name)):
		print("Found aiss: ", file_name)
	

print("end of loop")
