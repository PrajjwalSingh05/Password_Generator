import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", password="admin", database="password_recorder")
cur = mydb.cursor()
cur.execute("select pin from pin")
querry=cur.fetchall()
print(querry)
if(querry[0]==123):
    print("hello")
else:
    print("byee")

