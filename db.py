import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", password="", database="test")

if connection.is_connected():
    print("Conectado")
else:
    print("Errou")

connection.close()