## facedetection module

import face_recognition as fr
import cv2
import os 
import time
import numpy as np
from model import *

directory = "new_faces/"
cap = cv2.VideoCapture("video/video.mp4")


def generate_faceEncode(id):
    ## read new user images and return encodes

    ## encoding images of new user (filetype=jpg)
    image = fr.load_image_file(f"new_faces/{id}.jpg")
    encodes = fr.face_encodings(image)[0]
        
    ## moving face images from new_faces to known_faces 
    os.rename(f"new_faces/{id}.jpg",f"known_faces/{id}.jpg")

    return encodes




def recognize_face(id):
    ## Read a video capture and compare encodes with the user encode return true or false

    ## get users face encode
    users = session.query(Users).filter(Users.id==id)
    for user in users:
        userEncode = user.encode
        userEncode = jsonDeserialize(userEncode)


    match_count = 0 
    frameCount = 0 
    while (cap.isOpened()):
        ret, frame = cap.read()
        frameCount+=1

        ## getting faces encodes from the video frame
        face_locations=fr.face_locations(frame)
        faces_encodings = fr.face_encodings(frame,face_locations)     

        ## compare encodes for matches
        for face in faces_encodings:
            result=fr.compare_faces([userEncode],face)
            if True in result:
                match_count += 1
            else:
                match_count = 0

        if match_count>10:
            cv2.destroyAllWindows()
            cap.release() 
            return True
        elif frameCount >1000:
            cv2.destroyAllWindows()
            cap.release()
            return False     
            
        cv2.imshow('video frame',frame)
        if cv2.waitKey(1)==ord('q'):
            cv2.destroyAllWindows()
            cap.release() 
            break