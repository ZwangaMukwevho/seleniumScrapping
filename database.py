
import mysql.connector


# Function for connecting to mysql
def mysqlConnect(Host,User,Password,database):
    mysqlObject = mysql.connector.connect(
    host = Host,
    user = User,
    password = Password,
    database = database,
    )
    return mysqlObject


#mysql = mysql.connector.connect(
#   host = "localhost",
#    user = "root",
#    password = 'v4469ZWA5569MUK#',
#    database = "test",   
#)


sql = mysqlConnect("localhost","root",'v4469ZWA5569MUK#',"test",)

mycursor = sql.cursor()

# SQL insert query
query  = "insert into student(name,surname) values(%s, %s)"
val = ("Timmy","Turner")

mycursor.execute(query,val)

sql.commit()
print("data saved")