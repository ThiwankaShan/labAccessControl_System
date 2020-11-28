from model import *
from config import *
from faceDetection import *
from cardScanner import CardScanner
from entrance import Entrance
import sys
import threading
import multiprocessing

class ControlPanel():
    #mode = 'deactive'
    entrance = Entrance(1,serial_port,camera_port)

    @classmethod
    def resetSystem(cls):
        # (deletes users table), move known_faces images to new_faces images
        # reset db will be implement instead of delete only users table

        known_directory = "known_faces/"

        try:
            Users.__table__.drop(engine)
            Base.metadata.create_all(engine)
            for fileName in os.listdir(known_directory):
                os.rename(f"known_faces/{fileName}", f"new_faces/{fileName}")
            print("files reseted successfully")

        except:
            print("something went  wrong when resetting files")


    @classmethod
    def create_user(cls,name,id):
        # create new user and store user details in db

        card_encode = ' '
        image_encodes = FaceRecognition(camera_port).generate_faceEncode(regID)

        userObj = Users(name=userName, id=regID, image_encodes=jsonSerialize(
            image_encodes), card_encodes=card_encode)
        session.add(userObj)
        session.commit()


    @classmethod
    def start(cls,mode):
        ## start geral mode process or break other mode 
        print('start method fired')
        if mode == 'DeActive':
            cls.p = multiprocessing.Process(target=cls.generalMode,args=(cls.entrance,))
            cls.p.start()

        else:
            cls.entrance.cardScanner.ardunioSerial.write('break'.encode())
    
    @classmethod
    def stop(cls):
        ## stop general mode
        print('stop method fired')
        cls.p.terminate()
        
        
    @classmethod
    def emergencyMode(cls):
        ## start emergency mode and haults
        print('emergency method fired')
        cls.entrance.cardScanner.ardunioSerial.write('open'.encode())
        

    @classmethod
    def lockdownMode(cls):
        ## start lockdown mode and haults
        print('lockdown method fired')
        cls.entrance.cardScanner.ardunioSerial.write('close'.encode())
    
    
    @classmethod
    def generalMode(cls,entrance):
        ## start general mode 
        print('generalMode method fired')
        entrance.generalMode()
    

    @classmethod    
    def manualOpen(cls):
        ## manually open door
        print('manual open method fired')
        cls.entrance.cardScanner.ardunioSerial.write('open'.encode())

    @classmethod
    def manualClose(cls):
        ## manually close door
        print('manual close method fired')
        cls.entrance.cardScanner.ardunioSerial.write('close'.encode())

        
            
        

'''
def main():

    is_newUsers = str(input(
        "\nare there any new users? \nEnter y to yes \nEnter n to No\nEnter q to exit\n"))

    if is_newUsers.lower() == 'y':

        is_reset = str(input(
            "\ndo you want to reset all the data files and start fresh? \nEnter y to yes \nEnter n to No\n"))
        if is_reset.lower() == 'y':
            resetSystem()
        create_user()

    elif is_newUsers.lower() == 'n':

    entrance_1 = Entrance(1,serial_port,camera_port)
    def general_mode(entrance):
        entrance.generalMode()
    
    th = threading.Thread(target=general_mode,args=(entrance_1,))
    th.start()

    while True:
        action = input("change action : ")
        th.join()
        if action == "q":
            break
        else:
            entrance_1.cardScanner.ardunioSerial.write(action.encode())

    elif is_newUsers.lower() == 'q':
        sys.exit()

    else:
        print('input not valid')

'''