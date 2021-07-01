# +
import pyodbc
import pandas.io.sql as psql
import pandas as pd

def get_empname(email):
    conn = pyodbc.connect("Driver={SQL Server};Server=LAPTOP-00MU5FI2\SQLEXPRESS;Integrated Security=True;Database=RPA;")
    cursor = conn.cursor()
    
    emp_email = str(email)
    cur = cursor.execute("Select EmpName, EmpEmail FROM [dbo].[Employee] WHERE [EmpEmail]='"+emp_email+"'")
    columns = [column[0] for column in cur.description]
    results=[]
    for row in cur.fetchall():
        results.append(dict(zip(columns, row)))
    
 
    return results[0]['EmpName']
    


# get_empname('jill_j@abc.com')

    

