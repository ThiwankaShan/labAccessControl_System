## card scanner module
import serial

ardunioSerial = serial.Serial('/dev/ttyACM0',9600,timeout=5)
id_arr=['71 255 242 50','138 172 106 1']

def readCard():
    while (True):
        value = ardunioSerial.readline()
        value = value.decode('utf-8')[:13]
        print('from arduino '+value)

        if value in id_arr:
            print('from python true')
            ardunioSerial.write('granted\n'.encode())
        elif len(value)!=13:
            print(f"junk value : {value}")
            pass
        else:
            print(f"from python false when value {value}")
            ardunioSerial.write('denied\n'.encode())

def writeCard():
