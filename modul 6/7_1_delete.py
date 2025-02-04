import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "",
    database= "db_2210010146"
)

mycursor = mydb.cursor()
sql = "DELETE FROM kategori where id = 2"
mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "record(s) deleted")