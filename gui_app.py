import time
import concurrent.futures
from datetime import datetime
from tkinter import *
import pandas as pd
from dateutil import relativedelta
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hagai1234Buachi",
    database="project1"
)


root = Tk()
root.title("Calculator Salary")

def info():

    try:

        mycursor = mydb.cursor()
        sqlformula = ("SELECT FIRST_NAME, LAST_NAME, SALARY, HIRE_DATE FROM workers")
        result_dataFrame = pd.read_sql(sqlformula, mydb)

        df = pd.DataFrame(result_dataFrame)
        print(df)
        mycursor.execute(sqlformula)
        pd.set_option('display.max_columns', None)
        print("The average salary is:",result_dataFrame['SALARY'].mean())





    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()



labell=Label(text="PLAYERS", font=30).grid(row=0)
button = Button(text='PRESS HERE TO CALCULATE!',width=40, height=10, fg='red', command=info).grid(row=4)

root.mainloop()



