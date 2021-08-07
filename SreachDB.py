import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ganji2130",
  database="mydatabase"
)


mycursor = mydb.cursor()

search_keyword = 'JavaScript'


mycursor.execute("SELECT * FROM urls WHERE title LIKE '%" + search_keyword + "%'")

myresult = mycursor.fetchall()

for x in myresult:
  print('\n')
  print(x)
  