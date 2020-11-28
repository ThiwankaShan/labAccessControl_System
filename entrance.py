from cardScanner import CardScanner
from faceDetection import FaceRecognition
from model import *
import time

class Entrance:

    def __init__(self,id,scanner_port,cam_port):

        self.id = id
        self.cardScanner = CardScanner(scanner_port)
        self.camScanner = FaceRecognition(camera_port)
    
    def generalMode(self):

        while True:
            ## card scanner
            self.cardScanner.readCard()
            result = 'waiting'
            while (result == 'denied' or result == 'waiting'):
                result = self.cardScanner.readCard().__next__()
            card_encodes = result
            print(f"card encodes confirmed for: {card_encodes}")

            ## camera face recognition 
            if True: #self.camScanner.recognize_face(card_encodes):
                users = session.query(Users).filter(Users.card_encodes == card_encodes)
                for user in users:
                    userName = user.name

                print('\n****************************************\n')
                print(f"\nAcesss granted\nWelcome {userName}\n")
                print('\n****************************************\n')

            else:
                print("Access denied")
      

            