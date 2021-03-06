import pandas as pd 
import numpy as np
month_list = ['sept', 'oct','nov','dec','jan','feb','march','april','may', 'june', 'july', 'aug']
BS_month_column_list = ['school_id', 'metric', 'remark' , 'note', 'sep2012', 'oct2012', 'nov2012', 'dec2012', 'jan2013' , 'feb2013', 'mar2013', 'apr2013', 'may2013', 'jun2013', 'jul2013', 'aug2013','sep2013', 'oct2013', 'nov2013', 'dec2013', 'jan2014' , 'feb2014', 'mar2014', 'apr2014', 'may2014', 'jun2014', 'jul2014', 'aug2014', 'sep2014', 'oct2014', 'nov2014', 'dec2014', 'jan2015' , 'feb2015', 'mar2015', 'apr2015', 'may2015', 'jun2015', 'jul2015', 'aug2015', 'sep2015', 'oct2015', 'nov2015', 'dec2015', 'jan2016' , 'feb2016']
result = pd.DataFrame()
result2 = pd.DataFrame()
budget = pd.DataFrame()
budget2 = pd.DataFrame()
last_year = pd.DataFrame()
last_year2 = pd.DataFrame()
bs = pd.DataFrame()
bs1 = pd.DataFrame()

def calculate_ytd_enr(input_list):
	divide_by = []
	i = 1
	for item in input_list:
		divide_by = divide_by + [i]
		i+=1
	li = operation_on_list(input_list,divide_by,'/') 
	return li

def calculate_ytd_from_list(input_list):
	fy_ytd=0
	ytd = []
	input_list = np.array(input_list)
	input_list[np.isnan(input_list)] = 0
	input_list = input_list.tolist()
	for item in input_list:
		fy_ytd = fy_ytd + item
		ytd = ytd + [fy_ytd]
	return ytd


def total_teacher_churn_perc(school_name_in_excel_file, month_processed,current_year,result,result2,column_name_in_fact_table,load_fy_ytd_flag):
	'''churn metrics
	Staff- Other Teaching - Leavers
	Staff - Non Teaching - Leavers
	Staff- Teachers - Leavers
	'''
	month = month_index(month_processed)
	year = year_index(current_year, month)
	#extract_metric(metric_name, school_id, month)
	yr1 = extract_metric("Staff- Other Teaching - Leavers", school_name_in_excel_file,month_processed)
	yr2 = extract_metric("Staff - Non Teaching - Leavers", school_name_in_excel_file,month_processed)
	yr3 = extract_metric("Staff- Teachers - Leavers", school_name_in_excel_file,month_processed)
	#convert all to arrays
	yr1 = np.array(yr1)
	yr1[np.isnan(yr1)] = 0
	yr2 = np.array(yr2)
	yr2[np.isnan(yr2)] = 0
	yr3 = np.array(yr3)
	yr3[np.isnan(yr3)] = 0
	#print(nurs0,nurs1,nurs2,nurs3,nurs_other,nurs_etc)
	
	#add to a single res11ult
	res = yr1+yr2+yr3
	##
	metric_values_of_churn = res
	ytd_values_of_churn = calculate_ytd_from_list(metric_values_of_churn)
	
	'''calculate total of all the teachers'''

	'''total teacher metrics
	Staff - Other Teaching - Opening Balance
	Staff - Teachers - Opening Balance
	Staff - Non Teaching - Opening Balance
	'''
	month = month_index(month_processed)
	year = year_index(current_year, month)
	#extract_metric(metric_name, school_id, month)
	yr1 = extract_metric("Staff - Non Teaching - Opening Balance", school_name_in_excel_file,month_processed)
	yr2 = extract_metric("Staff - Teachers - Opening Balance", school_name_in_excel_file,month_processed)
	yr3 = extract_metric("Staff - Other Teaching - Opening Balance", school_name_in_excel_file,month_processed)
	#convert all to arrays
	yr1 = np.array(yr1)
	yr1[np.isnan(yr1)] = 0
	yr2 = np.array(yr2)
	yr2[np.isnan(yr2)] = 0
	yr3 = np.array(yr3)
	yr3[np.isnan(yr3)] = 0
	#print(nurs0,nurs1,nurs2,nurs3,nurs_other,nurs_etc)
	
	#add to a single res11ult
	res = yr1+yr2+yr3
	##
	metric_values_of_total_students = res
	ytd_values_of_total_students = calculate_ytd_from_list(metric_values_of_total_students)


	total_staff_churn_perc = operation_on_list(metric_values_of_churn, metric_values_of_total_students,'/')

	ytd_total_staff_churn_perc = operation_on_list(ytd_values_of_churn, ytd_values_of_total_students, '/')
	school_id = identify_school_name(school_name_in_excel_file)
	
	result2 = assign_to_metric(school_id , month, year ,'total_staff_churn_perc', total_teacher_churn_perc , column_name_in_fact_table,load_fy_ytd_flag,ytd_total_staff_churn_perc)

	result = concat_df(result , result2)
	return result

def total_teacher_churn(school_name_in_excel_file, month_processed,current_year,result,result2,column_name_in_fact_table,load_fy_ytd_flag):
	'''churn metrics
	Staff- Other Teaching - Leavers
	Staff - Non Teaching - Leavers
	Staff- Teachers - Leavers
	'''
	month = month_index(month_processed)
	year = year_index(current_year, month)
	#extract_metric(metric_name, school_id, month)
	yr1 = extract_metric("Staff- Other Teaching - Leavers", school_name_in_excel_file,month_processed)
	yr2 = extract_metric("Staff - Non Teaching - Leavers", school_name_in_excel_file,month_processed)
	yr3 = extract_metric("Staff- Teachers - Leavers", school_name_in_excel_file,month_processed)
	#convert all to arrays
	yr1 = np.array(yr1)
	yr1[np.isnan(yr1)] = 0
	yr2 = np.array(yr2)
	yr2[np.isnan(yr2)] = 0
	yr3 = np.array(yr3)
	yr3[np.isnan(yr3)] = 0
	#print(nurs0,nurs1,nurs2,nurs3,nurs_other,nurs_etc)
	
	#add to a single res11ult
	res = yr1+yr2+yr3
	##
	metric_values = res.tolist()
	ytd_metrics = calculate_ytd_from_list(metric_values)
	school_id = identify_school_name(school_name_in_excel_file)
	result2 = assign_to_metric(school_id , month, year ,'total_staff_churn', metric_values,column_name_in_fact_table,load_fy_ytd_flag,ytd_metrics)
	result = concat_df(result , result2)
	return result


def add_multiple_metrics(metric_list,school_name_in_excel_file, month_processed):
	values_list = []
	#metric_name_in_excel_file, school_name_in_excel_file, month_processed
	for item in metric_list:
		values_list = values_list + extract_metric(item, school_name_in_excel_file,month_processed)
	return 

def secondary(school_name_in_excel_file, month_processed,current_year,result,result2,column_name_in_fact_table):
	'''
	Pupils - Yr07-G06
	Pupils - Yr08-G07
	Pupils - Yr09-G08
	Pupils - Yr10-G09
	Pupils - Yr11-G10
	Pupils - Yr12-G11
	Pupils - Yr13-G12
	'''
	month = month_index(month_processed)
	year = year_index(current_year, month)
	#extract_metric(metric_name, school_id, month)
	nurs0 = extract_metric("Pupils - Yr07-G06", school_name_in_excel_file,month_processed)
	nurs1 = extract_metric("Pupils - Yr08-G07", school_name_in_excel_file,month_processed)
	nurs2 = extract_metric("Pupils - Yr09-G08", school_name_in_excel_file,month_processed)
	nurs3 = extract_metric("Pupils - Yr10-G09", school_name_in_excel_file,month_processed)
	nurs_other = extract_metric("Pupils - Yr11-G10", school_name_in_excel_file,month_processed)
	nurs_etc = extract_metric("Pupils - Yr12-G11", school_name_in_excel_file,month_processed)
	last_array = extract_metric("Pupils - Yr13-G12", school_name_in_excel_file,month_processed)
	#convert all to arrays
	nurs0 = np.array(nurs0)
	nurs0[np.isnan(nurs0)] = 0
	nurs1 = np.array(nurs1)
	nurs1[np.isnan(nurs1)] = 0
	nurs2 = np.array(nurs2)
	nurs2[np.isnan(nurs2)] = 0
	
	nurs3 = np.array(nurs3)
	nurs3[np.isnan(nurs3)] = 0
	
	nurs_other = np.array(nurs_other)
	nurs_other[np.isnan(nurs_other)] = 0
	
	nurs_etc = np.array(nurs_etc)
	nurs_etc[np.isnan(nurs_etc)] = 0
	
	last_array = np.array(last_array)
	last_array[np.isnan(last_array)] = 0
	#print(nurs0,nurs1,nurs2,nurs3,nurs_other,nurs_etc)
	
	#add to a single res11ult
	res = nurs0+nurs1+nurs2+nurs3+nurs_other+nurs_etc+last_array
	##
	metric_values = res.tolist()
	
	
	ytd = calculate_ytd_from_list(metric_values)
	ytd = calculate_ytd_enr(ytd)
	school_id = identify_school_name(school_name_in_excel_file)
	result2 = assign_to_metric(school_id , month, year ,'secondary', metric_values,column_name_in_fact_table,1,ytd)
	result = concat_df(result , result2)
	return result


def upper_elementary(school_name_in_excel_file, month_processed,current_year,result,result2,column_name_in_fact_table):
	'''Lower_elementary
	Pupils - Yr04-G03
	Pupils - Yr05-G04
	Pupils - Yr06-G05
	'''
	month = month_index(month_processed)
	year = year_index(current_year, month)
	#extract_metric(metric_name, school_id, month)
	yr1 = extract_metric("Pupils - Yr04-G03", school_name_in_excel_file,month_processed)
	yr2 = extract_metric("Pupils - Yr05-G04", school_name_in_excel_file,month_processed)
	yr3 = extract_metric("Pupils - Yr06-G05", school_name_in_excel_file,month_processed)
	#convert all to arrays
	yr1 = np.array(yr1)
	yr1[np.isnan(yr1)] = 0
	yr2 = np.array(yr2)
	yr2[np.isnan(yr2)] = 0
	yr3 = np.array(yr3)
	yr3[np.isnan(yr3)] = 0
	#print(nurs0,nurs1,nurs2,nurs3,nurs_other,nurs_etc)
	
	#add to a single res11ult
	res = yr1+yr2+yr3
	##
	metric_values = res.tolist()
	
	ytd = calculate_ytd_from_list(metric_values)
	ytd = calculate_ytd_enr(ytd)
	
	school_id = identify_school_name(school_name_in_excel_file)
	result2 = assign_to_metric(school_id , month, year ,'upper_elementary', metric_values,column_name_in_fact_table,1,ytd)
	result = concat_df(result , result2)
	return result

def lower_elementary(school_name_in_excel_file, month_processed,current_year,result,result2,column_name_in_fact_table):
	'''Lower_elementary
	Pupils - Yr01-KG-KG2
	Pupils - Yr02-G01
	Pupils - Yr03-G02
	'''
	month = month_index(month_processed)
	year = year_index(current_year, month)
	#extract_metric(metric_name, school_id, month)
	yr1 = extract_metric("Pupils - Yr01-KG-KG2", school_name_in_excel_file,month_processed)
	yr2 = extract_metric("Pupils - Yr02-G01", school_name_in_excel_file,month_processed)
	yr3 = extract_metric("Pupils - Yr03-G02", school_name_in_excel_file,month_processed)
	#convert all to arrays
	yr1 = np.array(yr1)
	yr1[np.isnan(yr1)] = 0
	yr2 = np.array(yr2)
	yr2[np.isnan(yr2)] = 0
	yr3 = np.array(yr3)
	yr3[np.isnan(yr3)] = 0
	#print(nurs0,nurs1,nurs2,nurs3,nurs_other,nurs_etc)
	
	#add to a single res11ult
	res = yr1+yr2+yr3
	##
	metric_values = res.tolist()
	ytd = calculate_ytd_from_list(metric_values)
	ytd = calculate_ytd_enr(ytd)
	
	school_id = identify_school_name(school_name_in_excel_file)
	result2 = assign_to_metric(school_id , month, year ,'lower_elementary', metric_values,column_name_in_fact_table,1,ytd)
	result = concat_df(result , result2)
	return result

def nursery(school_name_in_excel_file, month_processed,current_year,result,result2,column_name_in_fact_table,load_fy_ytd_flag):
	'''Pupils - Nursery -0+
	Pupils - Nursery -1+
	Pupils - Nursery -2+
	Pupils - Nursery -3+-EC3-Pre K
	Pupils - Nursery Other
	Pupils - RCN-EC4-KG1
	'''
	month = month_index(month_processed)
	year = year_index(current_year, month)
	#extract_metric(metric_name, school_id, month)
	nurs0 = extract_metric("Pupils - Nursery -0+", school_name_in_excel_file,month_processed)
	nurs1 = extract_metric("Pupils - Nursery -1+", school_name_in_excel_file,month_processed)
	nurs2 = extract_metric("Pupils - Nursery -2+", school_name_in_excel_file,month_processed)
	nurs3 = extract_metric("Pupils - Nursery -3+-EC3-Pre K", school_name_in_excel_file,month_processed)
	nurs_other = extract_metric("Pupils - Nursery Other", school_name_in_excel_file,month_processed)
	nurs_etc = extract_metric("Pupils - RCN-EC4-KG1", school_name_in_excel_file,month_processed)
	#convert all to arrays
	nurs0 = np.array(nurs0)
	nurs0[np.isnan(nurs0)] = 0
	nurs1 = np.array(nurs1)
	nurs1[np.isnan(nurs1)] = 0
	nurs2 = np.array(nurs2)
	nurs2[np.isnan(nurs2)] = 0
	
	nurs3 = np.array(nurs3)
	nurs3[np.isnan(nurs3)] = 0
	
	nurs_other = np.array(nurs_other)
	nurs_other[np.isnan(nurs_other)] = 0
	
	nurs_etc = np.array(nurs_etc)
	nurs_etc[np.isnan(nurs_etc)] = 0
	
	#print(nurs0,nurs1,nurs2,nurs3,nurs_other,nurs_etc)
	
	#add to a single res11ult
	res = nurs0+nurs1+nurs2+nurs3+nurs_other+nurs_etc
	##
	metric_values = res.tolist()
	ytd = calculate_ytd_from_list(metric_values)
	ytd = calculate_ytd_enr(ytd)
	school_id = identify_school_name(school_name_in_excel_file)
	result2 = assign_to_metric(school_id , month, year ,'nursery', metric_values,column_name_in_fact_table,1,ytd)
	result = concat_df(result , result2)
	return result

def load_dual_metric(metric1 , metric2 , school_name_in_excel_file, month_processed,current_year, metric_name_in_fact_table,result,result2,op,column_name_in_fact_table,load_fy_ytd_flag):
	# load_fy_ytd_flag 0 indiacates none
	# 1 indicates both metrics
	# 2 indicates calculate only the ytd
	month = month_index(month_processed)
	year = year_index(current_year, month)
	#metric_values = extract_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed)
	#here we can assign a single value to it
	metric_values  = operations_on_two_metrics(metric1, metric2, school_name_in_excel_file, month_processed, op,load_fy_ytd_flag)
	actuals = metric_values[0]
	ytd = metric_values[1]
	school_id = identify_school_name(school_name_in_excel_file)
	if(load_fy_ytd_flag == 0):
		result2 = assign_to_metric(school_id , month, year ,metric_name_in_fact_table, actuals,column_name_in_fact_table, 0, [])
	if(load_fy_ytd_flag == 1):
		result2 = assign_to_metric(school_id , month, year ,metric_name_in_fact_table, actuals,column_name_in_fact_table, 1, ytd)
	if(load_fy_ytd_flag == 2):
		result2 = assign_to_metric(school_id , month, year ,metric_name_in_fact_table, actuals,column_name_in_fact_table,2,ytd)
	
	result = concat_df(result , result2)
	return result

def operation_on_list(m1,m2,op):
	li1 = np.array(m1)
	li2 = np.array(m2)
	li1[np.isnan(li1)] = 0
	li2[np.isnan(li2)] = 0
	
	if(op == '/'):
		li3 =  li1 / li2
		li3[np.isnan(li3)] = 0
		li3 = li3.tolist()
	return li3
	

def operations_on_two_metrics(metric1, metric2, school_id, month, op,load_fy_ytd_flag):
	m1 = extract_metric(metric1, school_id, month)
	m2 = extract_metric(metric2, school_id, month)
	if (load_fy_ytd_flag == 0):
		actuals = operation_on_list(m1,m2,'/')
		return [actuals,[]]

	elif(load_fy_ytd_flag == 2):
		ytd_m1 = calculate_ytd_from_list(m1)
		ytd_m2 = calculate_ytd_from_list(m2)
		ytd = operation_on_list(ytd_m1, ytd_m2, '/')
		return [[],ytd]

	elif(load_fy_ytd_flag == 1):	
		actuals = operation_on_list(m1,m2,'/')
		ytd_m1 = calculate_ytd_from_list(m1)
		ytd_m2 = calculate_ytd_from_list(m2)
		ytd = operation_on_list(ytd_m1, ytd_m2, '/')
		return [actuals,ytd]		

def BS_cash_convent_metrics(month, year, school_id, result,column_name_in_fact_table,load_fy_ytd_flag):

	result = BS_load_metric('Covenant interest', school_id, month,year, 'Covenant_interest',result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	result = BS_load_metric('Covenant leverage', school_id, month,year, ' Covenant_leverage',result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	result = BS_load_metric('Interest / Debt Service cover', school_id, month,year, 'Intrest_debt_service_cover',result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	result = BS_load_metric('Liquidity / Cash position', school_id, month,year, 'Liquidity_cash_position',result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	result = BS_load_metric('Total Cash balance', school_id, month,year, 'total_cash_balance',result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	return result

def BS_extract_metric(metric_name, school_id, month,year):

	print("in extract metric we have the values", metric_name, school_id, month,year)
	#we have starting and ending columns of the indexes
	column_name_start = "sep"+year
	if(month in ['jan','feb','march','april','may', 'june', 'july', 'aug']):
		year = int(year)
		year+=1
		year = str(year)

	column_name_end = month+year
	#since all the school_ids are in upper case in this file
	result2 = df[(df['metric'] == metric_name) & (df['school_id'] == school_id)]
	result2 = result2.ix[:,column_name_start:column_name_end]
	
	result2 = result2.values.tolist()
	result2 = result2[0]
	return result2

def BS_load_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed,current_year, metric_name_in_fact_table,result,result2,column_name_in_fact_table ,load_fy_ytd_flag):
	
	BS_month_start_fy = 'sep'+current_year 

	if(month_processed in ['jan','feb','march','april','may', 'june', 'july', 'aug']):
		current_year = int(current_year)
		current_year += 1
		current_year = str(current_year)

	BS_month_column_current = month_processed + current_year
	if(month_processed in ['jan','feb','march','april','may', 'june', 'july', 'aug']):
		current_year = int(current_year)
		current_year -= 1
		current_year = str(current_year)

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
		if(column_name_in_fact_table == 'Month_ly'):
			#incr yeary here
			x= x+ 1
		yeary = yeary +[x]

	print("The values passed to assign_metric",school_id , month, yeary ,metric_name_in_fact_table, metric_values, column_name_in_fact_table)
	result2 = assign_to_metric(school_id , month, yeary ,metric_name_in_fact_table, metric_values, column_name_in_fact_table,0,[])
	result = concat_df(result , result2)
	return result

def BS_sanitise_file(res,starting_column_month_year,ending_column_month_year):
	flag = 0
	for item in BS_month_column_list:
		if(item == starting_column_month_year ):
			flag = 1
			pass
		else:
			if(item == 'school_id' or item == 'metric'):
				pass
			else:
				if(flag == 1):
					if(item == ending_column_month_year):
						flag = 0
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

def finance_metrics(year_of_file, month_of_file, school_id, result, result2,column_name_in_fact_table, load_fy_ytd_flag):
	#temporary assignment
	school_name_in_excel_file = map_school_name_by_excel(school_id)
	#load_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed,current_year, metric_name_in_fact_table,result,result2) 
	
	#enrollment 
	
	result = load_metric('Total Pupils', school_name_in_excel_file, month_of_file, year_of_file, 'total_pupils', result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	
	
	result = nursery(school_name_in_excel_file, month_of_file,year_of_file,result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	
	result = lower_elementary(school_name_in_excel_file, month_of_file,year_of_file,result,result2,column_name_in_fact_table)
	result = upper_elementary(school_name_in_excel_file, month_of_file,year_of_file,result,result2,column_name_in_fact_table)
	result = secondary(school_name_in_excel_file, month_of_file,year_of_file,result,result2,column_name_in_fact_table)
	
	#revenue
	result = load_metric('Total Revenue', school_name_in_excel_file, month_of_file, year_of_file, 'Revenue', result,result2,column_name_in_fact_table,1)
	# fees 
	result = load_metric('Net Fees', school_name_in_excel_file, month_of_file, year_of_file, 'Tution_Fees', result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	#load other income
	result = load_metric('Other Income', school_name_in_excel_file, month_of_file, year_of_file, 'other_income', result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	#load Avg Discount (%)
	result = load_metric('Discount % Gross Fees', school_name_in_excel_file, month_of_file, year_of_file, 'Avg_Discount', result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	#loading gross margin
	result = load_metric('Gross Margin', school_name_in_excel_file, month_of_file, year_of_file, 'Gross_Margin', result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	#loading GM Total % Income
	result = load_dual_metric('Gross Margin','Total Revenue', school_name_in_excel_file, month_of_file,year_of_file,'Gross_Margin_perc', result, result2, '/', column_name_in_fact_table,1)
	
	#Total Operating Costs
	result = load_metric('Total Operating Costs', school_name_in_excel_file, month_of_file, year_of_file, 'opex', result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	#Total Opex % Income
	
	result = load_dual_metric('Total Operating Costs','Total Revenue', school_name_in_excel_file, month_of_file,year_of_file,'opex_perc', result, result2, '/', column_name_in_fact_table,1)
	
	#Underlying EBITDA
	result = load_metric('Underlying EBITDA', school_name_in_excel_file, month_of_file, year_of_file, 'ebitda', result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	#ebitda perc
	result = load_dual_metric('Underlying EBITDA','Total Revenue', school_name_in_excel_file, month_of_file,year_of_file,'ebitda_perc', result, result2, '/', column_name_in_fact_table,1)
	#total a/r
	'''
	30 Days + Debtors
	60 Days + Debtors
	90 Days + Debtors
	120 Days + Debtors
	1 Year + Debtors
	Total Debtors
	'''
	result = load_metric("Total Debtors", school_name_in_excel_file, month_of_file, year_of_file, 'total_ar', result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	result = load_metric("30 Days + Debtors", school_name_in_excel_file, month_of_file, year_of_file, 'ar_30', result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	result = load_metric("60 Days + Debtors", school_name_in_excel_file, month_of_file, year_of_file, 'ar_60', result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	result = load_metric("90 Days + Debtors", school_name_in_excel_file, month_of_file, year_of_file, 'ar_90', result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	
	return result

def staff_metrics(year_of_file, month_of_file, school_id, result, result2,column_name_in_fact_table,load_fy_ytd_flag):
	#temporary assignment
	school_name_in_excel_file = map_school_name_by_excel(school_id)
	#1.total staff fte
	result = load_metric("Staff FTEs", school_name_in_excel_file, month_of_file, year_of_file, 'Staff_FTE', result , result2 ,column_name_in_fact_table,load_fy_ytd_flag)

	#2.avg staff cost per fte
		# we need to multiply the revenue index by 12
	result =load_single_metric_operation_factor("Avg Total Staff Cost Per FTE", school_name_in_excel_file, month_of_file, year_of_file, 'avg_staff_cost_per_fte', result , result2 ,column_name_in_fact_table,load_fy_ytd_flag,'*',12)
	
	
	#3.Staff Costs % Revenue
	'''Not matching '''
	result = load_dual_metric('Staff Costs' , 'Total Revenue', school_name_in_excel_file, month_of_file, year_of_file, 'staff_costs_by_revenue',result,result2, '/' ,column_name_in_fact_table,1)
	#4.Pupil Teacher Ratio (PTR)
	#Total School PTR
	result = load_metric("Total School PTR", school_name_in_excel_file, month_of_file, year_of_file, 'Total_School_PTR', result , result2,column_name_in_fact_table,load_fy_ytd_flag )

	#5. Pupil Total Teaching Staff Ratio (PTTRS)
	result = load_metric("Total School PTTSR", school_name_in_excel_file, month_of_file, year_of_file, 'Total_School_PTTSR', result , result2 ,column_name_in_fact_table,load_fy_ytd_flag)
	
	# 6.Total Staff Churn
	result = total_teacher_churn(school_name_in_excel_file, month_of_file, year_of_file , result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	#7.Total Staff Churn (%)
	#result = total_teacher_churn_perc(school_name_in_excel_file, month_of_file, year_of_file , result,result2,column_name_in_fact_table,load_fy_ytd_flag)
	
	#8. Teacher Churn
	result = load_metric("Staff- Teachers - Leavers", school_name_in_excel_file, month_of_file, year_of_file, 'teacher_churn', result,result2 ,column_name_in_fact_table,load_fy_ytd_flag)
	#9.Teacher Churn (%)
	result = load_dual_metric('Staff- Teachers - Leavers' , 'Staff - Teachers - Opening Balance', school_name_in_excel_file, month_of_file, year_of_file, 'teacher_churn_perc',result,result2, '/' ,column_name_in_fact_table,1)
	#10. Other Teaching Staff Churn
	result = load_metric("Staff- Other Teaching - Leavers", school_name_in_excel_file, month_of_file, year_of_file, 'other_staff_churn', result,result2,column_name_in_fact_table ,load_fy_ytd_flag)
	#11. Other Teaching Staff Churn (%)
	result = load_dual_metric('Staff- Other Teaching - Leavers' , 'Staff - Other Teaching - Opening Balance', school_name_in_excel_file, month_of_file, year_of_file, 'other_teaching_churn_perc',result,result2, '/' ,column_name_in_fact_table,1)
	#12. Non-Academic Staff Churn
	result = load_metric("Staff - Non Teaching - Leavers", school_name_in_excel_file, month_of_file, year_of_file, 'non_teaching_staff_churn', result,result2 ,column_name_in_fact_table,load_fy_ytd_flag)
	#13. Non-Academic Staff Churn (%)
	result = load_dual_metric('Staff - Non Teaching - Leavers' , 'Staff - Non Teaching - Opening Balance', school_name_in_excel_file, month_of_file, year_of_file, 'non_teaching_churn_perc',result,result2, '/' ,column_name_in_fact_table,1)
	#result = load_metric("Staff - Non Teaching - Churn", school_name_in_excel_file, month_of_file, year_of_file, 'non_teaching_staff_churn_perc', result,result2 ,column_name_in_fact_table,load_fy_ytd_flag)
	return result

def identify_school_name(school_name_in_excel_file):
	if(school_name_in_excel_file =='Total Stamford AIS'):
		school_id = 'sais'
	elif(school_name_in_excel_file =='AISS $'):
		school_id = 'aiss'
	else:
		pass
	return school_id

def map_school_name_by_excel(school_name_in_excel_file):
	if(school_name_in_excel_file == 'sais'):
		school_id = 'Total Stamford AIS'
	elif(school_name_in_excel_file == 'aiss'):
		school_id = 'AISS $'
	else:
		pass
	return school_id

def load_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed,current_year, metric_name_in_fact_table,result,result2,column_name_in_fact_table, load_fy_ytd_flag ):
	month = month_index(month_processed)
	year = year_index(current_year, month)
	metric_values = extract_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed)

	if(load_fy_ytd_flag ==1):
		fy_ytd_values_metric = calculate_ytd_from_list(metric_values)
	else:
		fy_ytd_values_metric = []

	school_id = identify_school_name(school_name_in_excel_file)
	result2 = assign_to_metric(school_id , month, year ,metric_name_in_fact_table, metric_values,column_name_in_fact_table, load_fy_ytd_flag, fy_ytd_values_metric)
	
	result = concat_df(result , result2)
	return result


def load_single_metric_operation_factor(metric_name_in_excel_file, school_name_in_excel_file, month_processed,current_year, metric_name_in_fact_table,result,result2,column_name_in_fact_table,load_fy_ytd_flag,op,factor):
	month = month_index(month_processed)
	year = year_index(current_year, month)
	metric_values = extract_metric(metric_name_in_excel_file, school_name_in_excel_file, month_processed)
	school_id = identify_school_name(school_name_in_excel_file)
	if(load_fy_ytd_flag ==1):
		fy_ytd_values_metric = calculate_ytd_from_list(metric_values)
	else:
		fy_ytd_values_metric = []
	
	result2 = assign_to_metric(school_id , month, year ,metric_name_in_fact_table, metric_values,column_name_in_fact_table,load_fy_ytd_flag,fy_ytd_values_metric)
	#operate
	if(op == '*'):
		result2[column_name_in_fact_table] = result2[column_name_in_fact_table]* factor
	elif(op == '/'):
		result2[column_name_in_fact_table] = result2[column_name_in_fact_table]/ factor
	elif(op == '+'):
		result2[column_name_in_fact_table] = result2[column_name_in_fact_table]+ factor
	elif(op == '-'):
		result2[column_name_in_fact_table] = result2[column_name_in_fact_table]- factor
	else:
		pass
	
	result = concat_df(result , result2)
	return result

def concat_df(res, res1):
	frames = [res,res1]
	res = pd.concat(frames)
	return res

def assign_to_metric(school_id,month,year,metric,column_name_in_fact_table_metric_values,column_name_in_fact_table, load_fy_ytd_flag, fy_ytd_values_metric):
	#check for the fy_ytd flag
	if(load_fy_ytd_flag == 1):
		res = pd.DataFrame()
		res['school_id'] = [school_id] * len(month)
		res['year'] = year
		res['month'] = month
		res['metric'] = [metric] *len(monty)

		res[column_name_in_fact_table] = column_name_in_fact_table_metric_values
		if(column_name_in_fact_table == 'Month_ly'):
			print(school_id, column_name_in_fact_table,column_name_in_fact_table_metric_values )
		if(column_name_in_fact_table == 'Monthly_actuals'):
			res["fy_ytd_actuals"] = fy_ytd_values_metric
		elif(column_name_in_fact_table == 'Monthly_budget'):
			res["fy_ytd_budget"] = fy_ytd_values_metric
		elif(column_name_in_fact_table == 'Month_ly'):
			res["fy_ytd_month_ly_budget"] = fy_ytd_values_metric
		else:
			print("Something's wrong!!!!!!!!")
			pass
		
	elif(load_fy_ytd_flag == 0):
		res = pd.DataFrame()
		res['school_id'] = [school_id] * len(month)
		res['year'] = year
		res['month'] = month
		print("The length of the month is",len(monty), len(month))
		res['metric'] = [metric] *len(month)
		res[column_name_in_fact_table] = column_name_in_fact_table_metric_values
		print("--------------------->",school_id, year, month)
	elif(load_fy_ytd_flag == 2):
		#only ytd
		res = pd.DataFrame()
		res['school_id'] = [school_id] * len(month)
		res['year'] = year
		res['month'] = month
		res['metric'] = [metric] *len(monty)
		if(column_name_in_fact_table == 'Monthly_actuals'):
			res["fy_ytd_actuals"] = fy_ytd_values_metric
		elif(column_name_in_fact_table == 'Monthly_budget'):
			res["fy_ytd_budget"] = fy_ytd_values_metric
		else:
			print("Something's wrong!!!!!!!!")
	return res

def extract_metric(metric_name, school_id, month):
	try:

		result = df[(df['metric'] == metric_name) & (df['school_id'] == school_id)]
		result = result.ix[:,'sept':month]
		result = result.values.tolist()
		result = result[0]
		print(metric_name, school_id, month, result)
	except : 
		'''hardcoded values as budget does not have this '''
		return [0,0,0,0,0,0,0,0,0,0,0,0]
	return result

def year_index(year, monty):
	year = int(year)
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
result = finance_metrics(2015,'dec','sais',result,result2,'Monthly_actuals',1)
#staff metrics
result = staff_metrics(2015,'dec','sais',result,result2,'Monthly_actuals',1)


#for aiss
result = finance_metrics(2015,'dec','aiss',result,result2,'Monthly_actuals',1)
#staff metrics
result = staff_metrics(2015,'dec','aiss',result,result2,'Monthly_actuals',1)
#Lets make a function which takes in file_name, month, currentyear,result,result2,df

'''--------------------------------------------------
---------		Convenant	Metrics		---------------
-----------------------------------------------------'''
df = pd.read_excel("AISS_SAIS_DASHBOARD_DEC_2015.xlsx",skiprows = 1)
#print(len(df.columns) , len(month_column_list))
df.columns = BS_month_column_list
df = BS_sanitise_file(df,'sep2015', 'dec2015')
# The function to pull out 5 metrics
bs1 = BS_cash_convent_metrics('dec', '2015', 'SAIS', bs1, 'Monthly_actuals',0)

#for aiss
df = pd.read_excel("AISS_SAIS_DASHBOARD_DEC_2015.xlsx",skiprows = 1)
#print(len(df.columns) , len(month_column_list))
df.columns = BS_month_column_list
df = BS_sanitise_file(df,'sep2015', 'dec2015')
# The function to pull out 5 metrics(give school_id in CAPITALS)
bs1 = BS_cash_convent_metrics('dec', '2015', 'AISS', bs1,'Monthly_actuals',0)

'''Last year cash metrics'''
'''----------------------------------------------------------'''
df = pd.read_excel("AISS_SAIS_DASHBOARD_DEC_2015.xlsx",skiprows = 1)

#print(len(df.columns) , len(month_column_list))
df.columns = BS_month_column_list
df = BS_sanitise_file(df,'sep2014', 'aug2015')
print(df)
# The function to pull out 5 metrics
# the function takes input of the year as 
# for example the fy is 2015-2016, we give the input as 2015
#important
bs = BS_cash_convent_metrics('aug', '2014', 'SAIS', bs, 'Month_ly',0)

#for aiss
df = pd.read_excel("AISS_SAIS_DASHBOARD_DEC_2015.xlsx",skiprows = 1)
#print(len(df.columns) , len(month_column_list))
df.columns = BS_month_column_list
df = BS_sanitise_file(df,'sep2014', 'aug2015')
# The function to pull out 5 metrics(give school_id in CAPITALS)
bs = BS_cash_convent_metrics('aug', '2014', 'AISS', bs,'Month_ly',0)

cash_metrics = pd.DataFrame()
cash_metrics = pd.merge(bs1, bs, how = 'outer', on = ['school_id','year','month','metric'])
print(cash_metrics)
cash_metrics.to_excel("cash_combined.xlsx", index = False)
#print(result) 

#to load the budget files we do not need any month date, we just load the files as it is
df = pd.read_excel("Budget FY1516 for Dashboard - SAIS AIS (including BSP).xlsx")
monty = month_index('aug')
year = year_index(2015, monty)
#finance metrics
budget = finance_metrics(2015,'aug','sais',budget,budget2,'Monthly_budget',1)
#staff metrics
budget = staff_metrics(2015,'aug','sais',budget,budget2,'Monthly_budget',1)

#for aiss
budget = finance_metrics(2015,'aug','aiss',budget,budget2, 'Monthly_budget',1)
#staff metrics
budget = staff_metrics(2015,'aug','aiss',budget,budget2,'Monthly_budget',1)

combined = pd.DataFrame()
combined = pd.merge(result, budget, how = 'outer', on = ['school_id','year','month','metric'])


'''--------------------------------------------------
---------The LY monthwise and ytd trick---------------
-----------------------------------------------------'''
df = pd.read_excel("SAIS & AISS P&L - Aug 2015.xlsx")
print(df)
monty = month_index('aug')
year = year_index(2015, monty)
#finance metrics
last_year = finance_metrics(2015,'aug','sais',last_year,last_year2,'Month_ly',1)
#staff metrics
last_year = staff_metrics(2015,'aug','sais',last_year,last_year2,'Month_ly',1)

#for aiss
last_year = finance_metrics(2015,'aug','aiss',last_year,last_year2, 'Month_ly',1)
#staff metrics
last_year = staff_metrics(2015,'aug','aiss',last_year,last_year2,'Month_ly',1)



'''the final step of writiing inthe file'''
combined1 = pd.DataFrame()

combined1 = pd.merge(combined, last_year, how = 'outer', on = ['school_id','year','month','metric'])
#combined2 = pd.merge(combined1, bs, how = 'outer', on = ['school_id','year','month','metric'])

print("the columns for combined file1", combined1.columns)

combined2 = pd.merge(combined1, cash_metrics, how = 'outer', on = ['school_id','year','month','metric','Monthly_actuals', 'Month_ly'])
combined2.to_excel('combined_table.xlsx', index = False)
print("the columns for cash metrics", cash_metrics.columns)
print("the columns for combined file2", combined2.columns)

#writing file to excel
#result.to_excel('fact_table.xlsx',index = False)
