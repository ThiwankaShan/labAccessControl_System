## facedetection module

import face_recognition as fr
import cv2
import os 
import time
import numpy as np
from model import *

directory = "new_faces/"
cap = cv2.VideoCapture("video/video.mp4")



def store_newFaces():
    ## read new user images and store encodes in database

    known_faces=[]
    known_names=[]
    for fileName in os.listdir(directory):

        ## encoding images of new faces (filetype=jpg)
        known_image = fr.load_image_file(f"new_faces/{fileName}")
        known_encoding = fr.face_encodings(known_image)[0]
        
        ## moving face images from new_faces to known_faces 
        os.rename(f"new_faces/{fileName}",f"known_faces/{fileName}")

        known_faces.append(known_encoding)
        known_names.append(fileName[:-4])

        insertData('users',name=fileName[:-4],encode=known_encoding)




def get_knownEncodes():
    ## this function is will be remove when db implemented
    ## Loads encodes saved in encodes.npz into knwown_faceEncodes list  

    known_faceEncodes=[]
    
    for arrays in data:
        for array in arrays:
            known_faceEncodes.append(array)

    return known_faceEncodes




def get_knownNames():
    ## Loads known names in names.npz into known_names list

    known_names=[]

    ## reading 'names.npz' to load known face encodes
    names_inFile=np.load("names.npz")
    names=[names_inFile[key] for key in names_inFile]

    for arrays in names:
        for array in arrays:
            known_names.append(array)

    return known_names



def recognize_face():
    ## Read a video capture and compare encodes with the user encode 

    id=int(input('\nEnter your id : ')) ## this will be provided from the cardscanner module as an argument 

    ## get users face encode
    known_faceEncode = extractData('users','encode','ID',id) 

    while (cap.isOpened()):
        ret, frame = cap.read()
    
        ## getting faces encodes from the video frame
        face_locations=fr.face_locations(frame)
        faces_encodings = fr.face_encodings(frame,face_locations)     
        
        

        ## compare encodes for matches
        for face in faces_encodings:
            result=fr.compare_faces(known_faceEncode,face)
        
            if True in result:
                print('Hello welcome to dr sobeck\'s lab')
                return True
            

        cv2.imshow('video frame',frame)
        if cv2.waitKey(1)==ord('q'):
            break