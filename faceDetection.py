# facedetection module

import face_recognition as fr
import cv2 
import numpy as np
from model import *

class FaceRecognition:

    def __init__(self,camport):
        self.port = camport 
        self.cap = cv2.VideoCapture(f"{self.port}")

    def generate_faceEncode(self,userID,new_dir="new_faces/",known_dir="known_faces/"):
        # read new user images and return encodes

        # encoding images of new user (filetype=jpg)
        try:
            image = fr.load_image_file(f"{new_dir}{userID}.jpg")
            encodes = fr.face_encodings(image)[0]
        except:
            raise Exception("file doesnt exist")

        # moving face images from new_faces to known_faces
        # os.rename(f"{new_dir}{userID}.jpg", f"{known_dir}{userID}.jpg")

        return encodes


    def recognize_face(self,id):
        # Read a video capture and compare encodes with the user encode return true or false

        # get users face encode
        try:
            users = session.query(Users).filter(Users.card_encodes == id)
            for user in users:
                userEncode = user.image_encodes
                userEncode = jsonDeserialize(userEncode)
        except:
            raise Exception("error fetching user data")

        match_count = 0
        frameCount = 0
        
        while (self.cap.isOpened()):
            ret, frame = self.cap.read()
            frameCount += 1

            # getting faces encodes from the video frame
            face_locations = fr.face_locations(frame)
            faces_encodings = fr.face_encodings(frame, face_locations)

            # compare encodes for matches
            for face in faces_encodings:
                result = fr.compare_faces([userEncode], face)
                if True in result:
                    match_count += 1
                else:
                    match_count = 0
            print(f"match count : {match_count}")
            if match_count > 10:
                #cv2.destroyAllWindows()
                return True
            elif frameCount > 1000:
                #cv2.destroyAllWindows()
                return False

           # cv2.imshow('video frame', frame)
           # if cv2.waitKey(1) == ord('q'):
           #     cv2.destroyAllWindows()
           #     break
