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
    encoding = fr.face_encodings(image)[0]
        
    ## moving face images from new_faces to known_faces 
    os.rename(f"new_faces/{id}.jpg",f"known_faces/{id}.jpg")

    return encoding
        

        


def get_knownEncodes():
    ## this function is will be remove when db implemented
    ## Loads encodes saved in encodes.npz into knwown_faceEncodes list  

    known_faceEncodes=[]
    
    for arrays in data:
        for array in arrays:
            known_faceEncodes.append(array)

    return known_faceEncodes




def get_knownNames():
    ## this function is will be remove when db implemented
    ## Loads known names in names.npz into known_names list

    known_names=[]

    ## reading 'names.npz' to load known face encodes
    names_inFile=np.load("names.npz")
    names=[names_inFile[key] for key in names_inFile]

    for arrays in names:
        for array in arrays:
            known_names.append(array)

    return known_names



def recognize_face(id):
    ## Read a video capture and compare encodes with the user encode 

    ## get users face encode
    users = session.query(Users).filter(Users.id==id)

    for user in users:
        userEncode = user.encode

    userEncode = jsonDeserialize(userEncode)

    while (cap.isOpened()):
        ret, frame = cap.read()
    
        ## getting faces encodes from the video frame
        face_locations=fr.face_locations(frame)
        faces_encodings = fr.face_encodings(frame,face_locations)     
        

        ## compare encodes for matches
        for face in faces_encodings:
            result=fr.compare_faces([userEncode],face)
            if True in result:
                return True
                
            
        cv2.imshow('video frame',frame)
        if cv2.waitKey(1)==ord('q'):
            break