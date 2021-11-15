import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="DATABASE_USER",
    password="DATABASE_PASS ",
    database="DATABASE_NAME"
)


mycursor = mydb.cursor()
sqlformula = "INSERT INTO workers (EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE , JOB_ID, SALARY, MANAGER_ID, DEPARTMENT_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
employed = [(7,"Cristiano","Ronaldo","CRIS","312-456-7832","1990-05-02","CR_K",30000.00,10,60),
            (10,"Luka","Modric","LUKITA","265-875-2352","1990-06-03","LM_K",29000.00,7,60),
            (8,"Ricardo","Kaka","RICKY","186-245-6239","1991-07-12","RK_V",27000.00,7,60),
            (4,"Sergio","Ramos","SERGI","578-219-9248","1991-07-14","SR_P",28000.00,8,60),
            (14,"Guti","Hernanzdez","GUTI","325-930-3267","1990-07-08","GH_V",26000.00,4,50),
            (1,"Iker","Casillas","SAN","247-947-3487","1989-02-12","SI_P",26000.00,4,50),
            (11,"Gareth","Bale","GABI","287-246-1235","1992-03-05","GB_V",25000.00,17,70),
            (17,"Raul","Gonzales","BLANCO","135-199-8465","1990-05-03","RG_K",29000.00,11,70),
            (3,"Kaper","Pepe","PEP","464-132-7894","1992-05-04","KP_V",26000.00,17,70),
            (9,"Karim","Benzema","BENZ","298-1326-8904","1990-03-12","KB_K",27000.00,7,60)]
mycursor.executemany(sqlformula , employed)
mydb.commit()

