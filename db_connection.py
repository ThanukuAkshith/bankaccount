import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="akshith@12345",
        database="HDFCBank"
    )
print("db connected successfully")



