## facedetection module

import face_recognition as fr
import cv2
import os 
import time
import numpy as np

directory = "new_faces/"
cap = cv2.VideoCapture("video/video.mp4")

def load_newFaces():
    ## read new user images and store encodes in the encodes.npz file and user names in names.npz file
    known_faces=[]
    known_names=[]
    for fileName in os.listdir(directory):

        ## encoding images of new faces (filetype=jpg)
        known_image = fr.load_image_file(f"new_faces/{fileName}")
        known_encoding = fr.face_encodings(known_image)[0]
        ##print(f'known_encoding : \n {known_encoding}')
        
        
        ## moving face images from new_faces to known_faces 
        os.rename(f"new_faces/{fileName}",f"known_faces/{fileName}")

        known_faces.append(known_encoding)
        known_names.append(fileName[:-4])

    ## storing encoded data to the "encoding.npz" file
    np.savez('encodes.npz',known_faces)

    ## storing names to the "names.npz" file
    np.savez('names.npz',known_names)

def get_knownFaces():
    ## Loads encodes saved in encodes.npz into knwown_faceEncodes list  

    known_faceEncodes=[]

    ## reading 'encodes.npz' to load known face encodes
    data_inFile=np.load("encodes.npz")
    data=[data_inFile[key] for key in data_inFile]
    for arrays in data:
        for array in arrays:
            known_faceEncodes.append(array)
    ##print(f"known faces encodes from file : \n{known_faceEncodes}")

    return known_faceEncodes

def get_knownNames():
    ## Loads known names in names.npz into known_namaes list

    known_names=[]

    ## reading 'names.npz' to load known face encodes
    names_inFile=np.load("names.npz")
    names=[names_inFile[key] for key in names_inFile]
    for arrays in names:
        for array in arrays:
            known_names.append(array)
    ##print(f"known names from file : \n{known_names}")

    return known_names


def recognize_faces():
    ## Read a video capture and compare encodes with the known encodes for a match 


    ## getting known face encodes
    known_faceEncodes = get_knownFaces() 
    known_names = get_knownNames()

    while (cap.isOpened()):
        ret, frame = cap.read()
    
        ## getting faces encodes from the video
        face_locations=fr.face_locations(frame)
        faces_encoding = fr.face_encodings(frame,face_locations)     
        
        

        ## compare encodes for matches
        for face in faces_encoding:
            result=fr.compare_faces(known_faceEncodes,face)
        
            if True in result:
                index=result.index(True)
                ##print(known_names[index])
                return True
            

        cv2.imshow('video frame',frame)
        if cv2.waitKey(1)==ord('q'):
            break