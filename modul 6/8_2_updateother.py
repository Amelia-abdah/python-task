import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "",
    database= "db_2210010146"
)

mycursor = mydb.cursor()
sql = "UPDATE kategori set name= %s where id = %s"
adr = ("Drinks", "4")
mycursor.execute(sql, adr)

mydb.commit()
print(mycursor.rowcount, "record(s) Updated")