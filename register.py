#!C:\python\python.exe

import cgi
import mysql.connector

print("Content-Type:text/html\r\n\r\n")
print("<html>")
print("<body>")
print("<h1>welcome to my page</h1>")

Form=cgi.FieldStorage()
FName=Form.getvalue("name")
FPassword=Form.getvalue("password")
print("record stored....thank you for registers mr/ms",FName)
#print("<h1>",FName,FPassword,"</h1>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="amazon"
    )
mycursor=mydb.cursor()
sql="INSERT INTO users(name,password)VALUES(%s,%s)"
val=(FName,FPassword);
mycursor.execute(sql,val)
mydb.commit()


print("</body>")
print("</html>")
