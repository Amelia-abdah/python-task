import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "",
    port= "3306",
    database= "db_2210010146"
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM kategori')

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
