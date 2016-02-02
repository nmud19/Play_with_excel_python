import pandas as pd 
import numpy as np
month_list = ['sept', 'oct','nov','dec','jan','feb','march','april','may', 'june', 'july', 'aug']
BS_month_column_list = ['school_id', 'metric', 'remark' , 'note', 'sep2012', 'oct2012', 'nov2012', 'dec2012', 'jan2013' , 'feb2013', 'mar2013', 'apr2013', 'may2013', 'jun2013', 'jul2013', 'aug2013','sep2013', 'oct2013', 'nov2013', 'dec2013', 'jan2014' , 'feb2014', 'mar2014', 'apr2014', 'may2014', 'jun2014', 'jul2014', 'aug2014', 'sep2014', 'oct2014', 'nov2014', 'dec2014', 'jan2015' , 'feb2015', 'mar2015', 'apr2015', 'may2015', 'jun2015', 'jul2015', 'aug2015', 'sep2015', 'oct2015', 'nov2015', 'dec2015', 'jan2016' , 'feb2016']
result = pd.DataFrame()
result2 = pd.DataFrame()


def load_dual_metric(metric1 , metric2 , school_name_in_excel_file, month_processed,current_year, metric_name_in_fact_table,result,result2, op ):
	
	month = month_index(month_processed)
	year = year_index(current_year, month)
	#metric_values = extract_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed)
	#here we can assign a single value to it
	metric_values  = operations_on_two_metrics(metric1, metric2, school_name_in_excel_file, month_processed, op)
	school_id = identify_school_name(school_name_in_excel_file)
	result2 = assign_to_metric(school_id , month, year ,metric_name_in_fact_table, metric_values)
	result = concat_df(result , result2)
	return result

def operations_on_two_metrics(metric1, metric2, school_id, month, op):
	m1 = extract_metric(metric1, school_id, month)
	m2 = extract_metric(metric2, school_id, month)
	if(op == '/'):
		li1 = np.array(m1)
		li2 = np.array(m2)
		li3 =  li1 / li2
		li3 = li3.tolist()
	return li3

def BS_cash_convent_metrics(month, year, school_id, result):
	result = BS_load_metric('Covenant interest', school_id, month,year, 'Covenant_interest',result,result2)
	result = BS_load_metric('Covenant leverage', school_id, month,year, ' Covenant_leverage',result,result2)
	result = BS_load_metric('Interest / Debt Service cover', school_id, month,year, 'Intrest_debt_service_cover',result,result2)
	result = BS_load_metric('Liquidity / Cash position', school_id, month,year, 'Liquidity_cash_position',result,result2)
	result = BS_load_metric('Total Cash balance', school_id, month,year, 'total_cash_balance',result,result2)
	return result

def BS_extract_metric(metric_name, school_id, month,year):
	#we have starting and ending columns of the indexes
	column_name_end = month+year
	column_name_start = "sep"+year
	#since all the school_ids are in upper case in this file
	school_id = school_id.upper()
	result2 = df[(df['metric'] == metric_name) & (df['school_id'] == school_id)]
	result2 = result2.ix[:,column_name_start:column_name_end]
	result2 = result2.values.tolist()
	print(result2)
	result2 = result2[0]
	return result2

def BS_load_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed,current_year, metric_name_in_fact_table,result,result2 ):
	
	BS_month_column_current = month_processed+current_year
	BS_month_start_fy = 'sep'+current_year 
	no_of_months = (BS_month_column_list.index(BS_month_column_current) - BS_month_column_list.index(BS_month_start_fy) + 1)

	#month index
	month = BS_month_index(no_of_months)
	year = year_index(current_year, month)
	
	metric_values = BS_extract_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed, current_year)
	#only lower case from the file
	school_id = school_name_in_excel_file.lower()

	#convert that year string to float for insertion into fact table
	yeary = []
	for item in year:
		x = float(item)
		yeary = yeary +[x]

	result2 = assign_to_metric(school_id , month, yeary ,metric_name_in_fact_table, metric_values)
	result = concat_df(result , result2)
	return result

def BS_sanitise_file(res):
	for item in BS_month_column_list:
		if(item == 'sep2015' ):
			break
		else:
			if(item == 'school_id' or item == 'metric'):
				pass
			else:
				del df[item]
	return res

def BS_month_index(month):
	i = 9
	li = []
	x = month
	start = 0
	while(start < x):
		if(i > 12 ):
			i = 1
		li = li + [i]
		i+=1
		start+=1
	return li

def useless_function():
	print("This contains all the comments which need to be saved")
	'''
	#this is for revenue
	result['school_id'] = ['sais'] * len(monty)
	result['year'] = len(monty)*[2015]
	result['month'] = monty
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
	'''ebitdaperc = extract_metric("Underlying EBITDA % Income", 'Total Stamford AIS', 'dec')
	result2 = assign_to_metric('sais',monty,year,'ebitda_perc',ebitdaperc)
	result = concat_df(result,result2)
	'''
	return

def finance_metrics(year_of_file, month_of_file, school_id, result, result2):
	#temporary assignment
	school_name_in_excel_file = map_school_name_by_excel(school_id)
	#load_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed,current_year, metric_name_in_fact_table,result,result2) 
	#revenue
	result = load_metric('Total Revenue', school_name_in_excel_file, month_of_file, year_of_file, 'Revenue', result,result2)
	# fees 
	result = load_metric('Net Fees', school_name_in_excel_file, month_of_file, year_of_file, 'Tution_Fees', result,result2)
	#load other income
	result = load_metric('Other Income', school_name_in_excel_file, month_of_file, year_of_file, 'other_income', result,result2)
	#load Avg Discount (%)
	result = load_metric('Discount % Gross Fees', school_name_in_excel_file, month_of_file, year_of_file, 'Avg_Discount', result,result2)
	#loading gross margin
	result = load_metric('Gross Margin', school_name_in_excel_file, month_of_file, year_of_file, 'Gross_Margin', result,result2)
	#loading GM Total % Income
	result = load_metric('GM Total % Income', school_name_in_excel_file, month_of_file, year_of_file, 'Gross_Margin_perc', result,result2)
	#Total Operating Costs
	result = load_metric('Total Operating Costs', school_name_in_excel_file, month_of_file, year_of_file, 'opex', result,result2)
	#Total Opex % Income
	result = load_metric('Total Opex % Income', school_name_in_excel_file, month_of_file, year_of_file, 'opex_perc', result,result2)
	#Underlying EBITDA
	result = load_metric('Underlying EBITDA', school_name_in_excel_file, month_of_file, year_of_file, 'ebitda', result,result2)
	#ebitda perc
	result = load_metric("Underlying EBITDA % Income", school_name_in_excel_file, month_of_file, year_of_file, 'ebitda_perc', result,result2)
	return result

def staff_metrics(year_of_file, month_of_file, school_id, result, result2):
	#temporary assignment
	school_name_in_excel_file = map_school_name_by_excel(school_id)
	#1.total staff fte
	result = load_metric("Staff FTEs", school_name_in_excel_file, month_of_file, year_of_file, 'Staff_FTE', result , result2 )
	#2.avg staff cost per fte
		# we need to multiply the revenue index by 12
	result = load_metric_multiply_by_12("Avg Total Staff Cost Per FTE", school_name_in_excel_file, month_of_file, year_of_file, 'avg_staff_cost_per_fte', result , result2 )

	#3.Staff Costs % Revenue
	result = load_dual_metric('Staff Costs' , 'Total Revenue', school_name_in_excel_file, month_of_file, year_of_file, 'staff_costs_by_revenue',result,result2, '/' )
	#4.Pupil Teacher Ratio (PTR)
	#5. Pupil Total Teaching Staff Ratio (PTTRS)

	# 6.Total Staff Churn
		#sumn of all leavers
	#7.Total Staff Churn (%)
		#perc of all leavers

	#8. Teacher Churn
	result = load_metric("Staff- Teachers - Leavers", school_name_in_excel_file, month_of_file, year_of_file, 'teacher_churn', result,result2 )
	#9.Teacher Churn (%)
	result = load_metric("Staff - Teachers - Churn", school_name_in_excel_file, month_of_file, year_of_file, 'teacher_churn_perc', result,result2 )
	#10. Other Teaching Staff Churn
	result = load_metric("Staff- Other Teaching - Leavers", school_name_in_excel_file, month_of_file, year_of_file, 'other_staff_churn', result,result2 )
	#11. Other Teaching Staff Churn (%)
	result = load_metric("Staff - Other Teaching - Churn", school_name_in_excel_file, month_of_file, year_of_file, 'other_staff_churn_perc', result,result2 )
	#12. Non-Academic Staff Churn
	result = load_metric("Staff - Non Teaching - Leavers", school_name_in_excel_file, month_of_file, year_of_file, 'non_teaching_staff_churn', result,result2 )
	#13. Non-Academic Staff Churn (%)
	result = load_metric("Staff - Non Teaching - Churn", school_name_in_excel_file, month_of_file, year_of_file, 'non_teaching_staff_churn_perc', result,result2 )
	return result

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


def load_metric_multiply_by_12(metric_name_in_excel_file, school_name_in_excel_file, month_processed,current_year, metric_name_in_fact_table,result,result2 ):
	month = month_index(month_processed)
	year = year_index(current_year, month)
	metric_values = extract_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed)
	school_id = identify_school_name(school_name_in_excel_file)
	result2 = assign_to_metric(school_id , month, year ,metric_name_in_fact_table, metric_values)
	result2['Monthly_actuals'] = result2['Monthly_actuals']*12
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

'''Read the PnL file'''
df = pd.read_excel("AISS_SAIS_P&L_DEC_2015.xlsx")
monty = month_index('dec')
year = year_index(2015, monty)
#finance metrics
result = finance_metrics(2015,'dec','sais',result,result2)
#staff metrics
result = staff_metrics(2015,'dec','sais',result,result2)


'''Read the Dashboard file'''
df = pd.read_excel("AISS_SAIS_DASHBOARD_DEC_2015.xlsx",skiprows = 1)
#print(len(df.columns) , len(month_column_list))
df.columns = BS_month_column_list
df = BS_sanitise_file(df)
# The function to pull out 5 metrics
result = BS_cash_convent_metrics('dec', '2015', 'SAIS', result)
print(result) 


#writing file to excel
result.to_excel('fact_table.xlsx',index = False)
