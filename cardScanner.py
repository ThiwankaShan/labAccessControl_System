# card scanner module
import serial
from model import *

ardunioSerial = serial.Serial(serial_port, 9600, timeout=5)


def readCard():
    # genereator returns recognized user card encode or message

    # querry all user id as a list
    querry_result = session.query(Users.card_encodes).all()
    id_arr = []
    for user in querry_result:
        id_arr.append(user[0])

    # read scanner and yield matching id
    while (True):
        value = ardunioSerial.readline()
        value = value.decode('utf-8')[:13]
        print('arduino output'+value)

        if value in id_arr:
            print('from python true')
            ardunioSerial.write('granted\n'.encode())
            result = value
        elif len(value) != 13:
            #print(f"junk value : {value}")
            result = 'waiting'
            pass
        else:
            print(f"from python false when value {value}")
            ardunioSerial.write('denied\n'.encode())
            result = 'denied'

        yield result
