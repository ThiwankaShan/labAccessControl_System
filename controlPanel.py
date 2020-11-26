from model import *
from config import *
from faceDetection import *
from cardScanner import CardScanner
from entrance import Entrance
import sys
import threading

class ControlPanel():

    print('control panel : class attributes created')
    entrance = 'hello entrance'

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
    def start(cls):
        print('start method fired')
        th = threading.Thread(target=cls.generalMode,args=())
        th.start()
    
    @classmethod
    def stop(cls):
        print('stop method fired')
        pass

    @classmethod
    def emergencyMode(cls):
        print('emergency method fired')
        pass

    @classmethod
    def lockdownMode(cls):
        print('lockdown method fired')
        pass
    
    @classmethod
    def generalMode(cls):
        print('generalMode method fired')
        pass


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