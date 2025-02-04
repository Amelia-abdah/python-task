import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "",
    database= "db_2210010146"
)

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM kategori')

myresult = mycursor.fetchone()

for x in myresult:
    print(x)