import os #this header required for the file path variable
import re #this import required foir regular expressions module
excel_files = [] # this is the variable holding the file names
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
def sanitise_the_file():

	return
#main program
excel_files = cache_all_file_names()
identify_file('DEC', '2015')
print("end of loop")
