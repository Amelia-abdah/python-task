import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "",
    database= "db_2210010146"
)

mycursor = mydb.cursor()
sql = "DELETE FROM kategori where id = %s"
adr = ("3",)
mycursor.execute(sql,adr)

mydb.commit()
print(mycursor.rowcount, "record(s) deleted")