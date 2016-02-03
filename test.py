import pymysql
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='192.168.100.31',
                             user='cognita_u',
                             password='cognita_p@$sw0rD',
                             db='cognita',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
  
    with connection.cursor() as cursor:
        # Read a single record
        sql = " SELECT * FROM `xw_financial_fact` WHERE `school`= 'aiss' and `month` = %s and `year` = '2015' "
        cursor.execute(sql,'12')
        result = cursor.fetchone()
        print(result)
        print(result['month_ly'])
finally:
    connection.close()