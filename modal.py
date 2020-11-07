## modal for database handling
import mysql.connector
import json
import numpy as np

##configuration of Db

try:
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = '',
    database = "lab_acess"
    )
    print('connection sucessfull')
except:
    print("Error: couldn't connect to database")

connection = mydb.cursor()
    



def insertData(table : str ,**kwargs):
    ## take table, attribute and value names as arguments and store values in DB

    attrs=""
    values=""

    for attr,value in kwargs.items():
        if type(value)==str:
            value=f"'{value}'"
        elif type(value)==np.ndarray:
            value= value.tolist()
            value=json.dumps(value)
            value=f"'{value}'"
         
        attrs = attrs + attr + ","
        values = values + str(value) + "," 

    attrs=attrs[:-1]
    values=values[:-1]
    sql=f"INSERT INTO {table} ({attrs}) VALUES ({values})"
    connection.execute(sql)
    mydb.commit()
    print('inserted succesfully')



def extractData(table : str,extractAtrr : str ,whereAttr='' ,value=''):
    ## take table name, what value to extract, condition to find the value and return a single value
    
    if whereAttr == '' or value == '':
        sql=f"SELECT {extractAtrr} FROM {table}"
        flag=True
    else:
        sql=f"SELECT {extractAtrr} FROM {table} WHERE {whereAttr}={value}"
        flag=False
    try:
        connection.execute(sql)
        result = connection.fetchall() if flag else connection.fetchone()
        if result == None:
            print("result not found")
        else:
            if type(result[0])==list:
                np.array(result[0])
                return result
            else:
                return result
        
    except:
        print('something went wrong when fetching results')

extractData('users','name','ID',8)
 