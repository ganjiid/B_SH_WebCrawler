import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ganji2130",
  database="mydatabase"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE urls (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), title VARCHAR(255))")

#mycursor.execute("DROP TABLE urls")

"""mycursor.execute("SELECT * FROM urls")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
"""