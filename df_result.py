import pandas as pd 
month_list = ['sept', 'oct','nov','dec','jan','feb','march','april','may', 'june', 'july', 'aug']
result = pd.DataFrame()
result2 = pd.DataFrame()

def identify_school_name(school_name_in_excel_file):
	if(school_name_in_excel_file =='Total Stamford AIS'):
		school_id = 'sais'
	return school_id

def map_school_name_by_excel(school_name_in_excel_file):
	if(school_name_in_excel_file == 'sais'):
		school_id = 'Total Stamford AIS'
	return school_id

def load_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed,current_year, metric_name_in_fact_table,result,result2 ):
	month = month_index(month_processed)
	year = year_index(current_year, month)
	metric_values = extract_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed)
	school_id = identify_school_name(school_name_in_excel_file)
	result2 = assign_to_metric(school_id , month, year ,metric_name_in_fact_table, metric_values)
	result = concat_df(result , result2)
	return result

def concat_df(res, res1):
	frames = [res,res1]
	res = pd.concat(frames)
	return res

def assign_to_metric(school_id,month,year,metric,monthly_actuals):
	res = pd.DataFrame()
	res['school_id'] = [school_id] * len(month)
	res['year'] = year
	res['month'] = month
	res['metric'] = [metric] *len(monty)
	res['Monthly_actuals'] = monthly_actuals
	return res

def extract_metric(metric_name, school_id, month):
	result = df[(df['metric'] == metric_name) & (df['school_id'] == school_id)]
	result = result.ix[:,'sept':month]
	result = result.values.tolist()
	result = result[0]
	return result

def year_index(year, monty):
	y = year
	yeary = []
	for item in monty:
		if(item ==1):
			y+=1
		yeary = yeary + [y]
	return yeary

def month_index(month):
	i = 9
	li = []
	for item in month_list:
		if month == item:
			li = li + [i]
			break
		else:
			li = li + [i]
			i+=1
			if(i ==13):
				i=1
	return li

#main program
df = pd.read_excel("AISS_SAIS_P&L_DEC_2015.xlsx")
Revenue = extract_metric('Total Revenue', 'Total Stamford AIS', 'dec')
monty = month_index('dec')
year = year_index(2015, monty)

#load revenue data into dataframe
result2 = assign_to_metric('sais',monty,year,'Revenue',Revenue)
result = concat_df(result,result2)
#print(result)

#load fees into file
tuitionfees = extract_metric('Net Fees', 'Total Stamford AIS', 'dec')
result2 = assign_to_metric('sais',monty,year,'Tution_Fees',tuitionfees)
result = concat_df(result,result2)


#load other income
other_income = extract_metric('Other Income', 'Total Stamford AIS', 'dec')
result2 = assign_to_metric('sais',monty,year,'other_income',other_income)
result = concat_df(result,result2)

#load Avg Discount (%)
Avg_Discount = extract_metric("Discount % Gross Fees", 'Total Stamford AIS', 'dec')
result2 = assign_to_metric('sais',monty,year,'Avg_Discount',Avg_Discount)
result = concat_df(result,result2)

#loading gross margin
gm = extract_metric("Gross Margin", 'Total Stamford AIS', 'dec')
result2 = assign_to_metric('sais',monty,year,'Gross_Margin',gm)
result = concat_df(result,result2)

#loading GM Total % Income
gmperc = extract_metric("GM Total % Income", 'Total Stamford AIS', 'dec')
result2 = assign_to_metric('sais',monty,year,'Gross_Margin_perc',gmperc)
result = concat_df(result,result2)

#Total Operating Costs
opex = extract_metric("Total Operating Costs", 'Total Stamford AIS', 'dec')
result2 = assign_to_metric('sais',monty,year,'opex',opex)
result = concat_df(result,result2)

#Total Opex % Income
opexperc = extract_metric("Total Opex % Income", 'Total Stamford AIS', 'dec')
result2 = assign_to_metric('sais',monty,year,'opex_perc',opexperc)
result = concat_df(result,result2)

#Underlying EBITDA
ebitda = extract_metric("Underlying EBITDA", 'Total Stamford AIS', 'dec')
result2 = assign_to_metric('sais',monty,year,'ebitda',ebitda)
result = concat_df(result,result2)

#ebitda%
result = load_metric("Underlying EBITDA % Income", 'Total Stamford AIS', 'dec', 2015, 'ebitda_perc', result,result2 )

#staff metrics

#1.total staff fte
result = load_metric("Staff FTEs", 'Total Stamford AIS', 'dec', 2015, 'Staff_FTE', result,result2 )
#2.avg staff cost per fte
	# we need to multiply the revenue index by 12
#3.Staff Costs % Revenue
#4.Pupil Teacher Ratio (PTR)
#5. Pupil Total Teaching Staff Ratio (PTTRS)

# 6.Total Staff Churn
	#sumn of all leavers
#7.Total Staff Churn (%)
	#perc of all leavers

#8. Teacher Churn
result = load_metric("Staff- Teachers - Leavers", 'Total Stamford AIS', 'dec', 2015, 'teacher_churn', result,result2 )

#9.Teacher Churn (%)
result = load_metric("Staff - Teachers - Churn", 'Total Stamford AIS', 'dec', 2015, 'teacher_churn_perc', result,result2 )

#10. Other Teaching Staff Churn
result = load_metric("Staff- Other Teaching - Leavers", 'Total Stamford AIS', 'dec', 2015, 'other_staff_churn', result,result2 )

#11. Other Teaching Staff Churn (%)
result = load_metric("Staff - Other Teaching - Churn", 'Total Stamford AIS', 'dec', 2015, 'other_staff_churn_perc', result,result2 )

#12. Non-Academic Staff Churn
result = load_metric("Staff - Non Teaching - Leavers", 'Total Stamford AIS', 'dec', 2015, 'non_teaching_staff_churn', result,result2 )

#13. Non-Academic Staff Churn (%)
result = load_metric("Staff - Non Teaching - Churn", 'Total Stamford AIS', 'dec', 2015, 'non_teaching_staff_churn_perc', result,result2 )



'''ebitdaperc = extract_metric("Underlying EBITDA % Income", 'Total Stamford AIS', 'dec')
result2 = assign_to_metric('sais',monty,year,'ebitda_perc',ebitdaperc)
result = concat_df(result,result2)
'''
print(result)

#writing file to excel
#result.to_excel('fact_table.xlsx',index = False)

'''
#this is for revenue
result['school_id'] = ['sais'] * len(monty)
result['year'] = len(monty)*[2015]
result['month'] = monty
result['metric'] = ['Revenue'] *len(monty)
result['Monthly_actuals'] = Revenue
print(result)
'''
'''
#for fees
tuitionfees = extract_metric('Net Fees', 'Total Stamford AIS', 'dec')
result2 = pd.DataFrame()
result2['school_id'] = ['sais'] * len(monty)
result2['year'] = len(monty)*[2015]
result2['month'] = monty
result2['metric'] = ['Tution_Fees'] *len(monty)
result2['Monthly_actuals'] = tuitionfees
print(result2)
frames = [result,result2]
result = pd.concat(frames)

print("The moment we have been waiting for")
print(result)
result2 = pd.DataFrame()
print(result2)
'''