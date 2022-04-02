import mysql.connector
import datetime

db = mysql.connector.connect(
    host="eee4022sdatabase-do-user-9871310-0.b.db.ondigitalocean.com",
    user="admin",
    passwd="aGAPX1Hn5TdTE-4I",
    database="lab_system",
    port = "25060"
)

# Creating curser
cursor = db.cursor()

cursor.execute("SHOW TABLES")

for table_name in cursor:
   print(table_name)



# def createTable(name, attributes,primaryKey=None,foreignKeys=None):
#     """Creates a table in the database with the given attributes and keys

#     :param attributes: List of attributes to be added in the table
#     :type attributes: list
#     :param primaryKey: Primary key attribute
#     :type primaryKey: string
#     :param foreignKeys: Foreign key attribute
#     :type foreignKeys: string
#     """
#     query = "CREATE TABLE {}( \n".format(name)
    
#     # Adds the attributes to the queries
#     for attribute in attributes:
#         query = query + "{} {} NOT NULL, \n".format(attribute,attributes[attribute])

#     # Adding the primaryKey to the query
#     if primaryKey !=None:
#         query = query + "PRIMARY KEY ({}), \n".format(primaryKey)
    
#     # Adding the foreignKeys to the query
#     if foreignKeys != None:
#         for key in foreignKeys:
#             reference = foreignKeys[key]
#             query = query + "FOREIGN KEY ({}) REFERENCES {}({}), \n".format(key,reference,key)
        
    
#     query = query[:-3] +"\n);"
#     return query


# start_time = datetime.datetime(2021,5,17,11,00,00)
# end_time = datetime.datetime(2021,5,17,13,00,00)

# # name = "lab_schedule"
# # attributes = {"schedule_id":"VARCHAR(50)", "start_time":"DATETIME", "end_time":"DATETIME", "code":"VARCHAR(50)"}
# # primary_key = "schedule_id"
# # foreignKeys = {"code":"course"}

# # name = "activity"
# # attributes = {"activity_id":"VARCHAR(50)", 
# #     "status":"VARCHAR(50)", 
# #     "activity":"VARCHAR(50)", 
# #     "schedule_id":"VARCHAR(50)",
# #     "code":"VARCHAR(50)"}

# # primary_key = "activity_id"
# # foreignKeys = {"schedule_id":"lab_schedule",
# #     "code":"course"}

# ## Enrolls table
# # name = "enrolls"
# # attributes = {"student_no":"VARCHAR(50)", 
# #     "code":"VARCHAR(50)"}

# # primary_key = None
# # foreignKeys = {"student_no":"student",
# #     "code":"course"}

# ## student table
# # name = "student"
# # attributes = {"student_no":"VARCHAR(50)", 
# #     "student_name":"VARCHAR(50)",
# #     "student_surname":"VARCHAR(50)"}

# # primary_key = "student_no"
# # foreignKeys = None


# ## temp log
# name = "temperature_log"
# attributes = {"temp_id":"VARCHAR(50)", 
#     "Date":"DATETIME",
#     "Temp":"VARCHAR(50)",
#     "student_no":"VARCHAR(50)"}

# primary_key = "temp_id"
# foreignKeys = {"student_no":"student"}

# output = createTable(name,attributes,primary_key,foreignKeys)
# print(output)

# def enterTableInfo():
#     # table name
#     table_name = input("Enter the table: \n")
 
#     # attributes
#     attribute_dict = {}
#     quit = False
#     while(not quit):

#         attribute_name = input("\nEnter attribute name: \n")
#         attribute_type = input("\nEnter attribute type: \n")
#         attribute_dict[attribute_name] = attribute_type

#         quit = input("\nPress \"q\" to if there are no more attributes or \"c\" to continue adding attributes: \n")
#         print(quit)
#         if quit == "q":
#             print(quit)
#             quit = True
    
#     # Primary key
#     primary_key = input("\nEnter the primary key, if \"none\" exist type none: \n")
#     primary_key = primary_key.lower()
#     if primary_key == "none":
#         primary_key = None

#     # Foreign key
#     foreign_key_dict = {}
#     quit = False
#     while(not quit):

#         quit = input("\nPress \"q\" to if there are no foreign keys to add or \"c\" to continue adding foreign keys: \n")
#         if quit == "q":
#             quit = True
        
#         foreign_key = input("\nEnter foreign name: \n")
#         foreign_key_type = input("\nEnter table reference of foreign key: \n")
#         foreign_key_dict[foreign_key] = foreign_key_type

#         if len(foreign_key_dict) == 0:
#             foreign_key_dict = None

#     output = createTable(name,attribute_dict,primary_key,foreign_key_dict)   
#     return output


# # Continuous
# quit = False
# while(not quit):
#     input_value = input("\nOptions: \nPress 1: For adding table \nPress 2:To drop table \nor q to quit: \n")

#     if input_value == "q":
#         quit = True
        
#     # Table informtio1
#     if input_value == "1":
#         output = enterTableInfo()
#         print(output)



        





# query = '''CREATE TABLE contains(
#         code VARCHAR(50) NOT NULL,
#         name VARCHAR(50) NOT NULL,
#         FOREIGN KEY (code) REFERENCES Course(code),
#         FOREIGN KEY (name) REFERENCES lab(name)
#         );'''
# cursor.execute(output)