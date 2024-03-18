import mysql.connector

mydb = mysql.connector.connect(host="sql6.freesqldatabase.com",
                               user="sql6692017",
                               password="2DcjLXDFwG",
                               database="sql6692017")

print(mydb)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM accounts")
myresult = cursor.fetchall()
print(myresult)
# cursor = mydb.cursor()
cursor.execute("SELECT * FROM accounts")
myresult = cursor.fetchall()
print(myresult)