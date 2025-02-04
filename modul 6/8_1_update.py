import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "",
    database= "db_2210010146"
)

mycursor = mydb.cursor()
sql = "UPDATE kategori set name='Jelly' where id = 4"
mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "record(s) Updated")