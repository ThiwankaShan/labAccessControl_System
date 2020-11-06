## modal for database handling
import mysql.connector
import json
import numpy as np
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = '',
    database = "lab_acess"
)

connection = mydb.cursor()

print('connection sucessfull')

def insertData(table : str ,**kwargs):
    attrs=""
    values=""

    for attr,value in kwargs.items():
        if type(value)==str:
            value=f"'{value}'"
        elif type(value)==list:
            value=json.dumps(value)
            value=f"'{value}'"
         
        attrs = attrs + attr + ","
        values = values + str(value) + "," 

    attrs=attrs[:-1]
    values=values[:-1]
    sql=f"INSERT INTO {table} ({attrs}) VALUES ({values})"
    print(sql+'\n')
    connection.execute(sql)
    mydb.commit()
    print('inserted succesfully')

def extractData(table : str,extractAtrr : str ,whereAttr : str ,value):

    sql=f"SELECT {extractAtrr} FROM {table} WHERE {whereAttr}={value}"
    try:
        connection.execute(sql)
        result = connection.fetchone()
        if result == None:
            print("result not found")
        else:
            print(result[0])
    except:
        print('something went wrong')
##insertData('users',name='shan',id=1,encode=[1,2,3,4,5,6,7,8,89,56])

extractData('users','name','ID',1) 