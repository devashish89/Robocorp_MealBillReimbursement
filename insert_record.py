# +
import pyodbc
import pandas.io.sql as psql
import pandas as pd

def insert_data(name, email, amt, vname, vaddr, vgst, vcat):
    conn = pyodbc.connect("Driver={SQL Server};Server=LAPTOP-00MU5FI2\SQLEXPRESS;Integrated Security=True;Database=RPA;")
    cursor = conn.cursor()
    
#     emp_email = str(email)
    cursor.execute("INSERT INTO [dbo].[Reimburse] VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(name, email, amt, vname, vaddr[:50], vgst, vcat))
    conn.commit()

# insert_data("", "", "v", "", "", "", "")
