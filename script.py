import face_recognition as fr
import cv2
import os 

directory="known_faces/"
known_faces=[]
known_names=[]
for fileName in os.listdir(directory):
    known_image = fr.load_image_file(f"known_faces/{fileName}")
    known_encoding = fr.face_encodings(known_image)[0]
    known_faces.append(known_encoding)
    known_names.append(fileName[:-4])


cap = cv2.VideoCapture("video/video.mp4")

while (cap.isOpened()):
    ret, frame = cap.read()
    
    face_locations=fr.face_locations(frame)
    faces_encoding = fr.face_encodings(frame,face_locations)

    for face in faces_encoding:
        result=fr.compare_faces(known_faces,face)
        
        if True in result:
            index=result.index(True)
            print(known_names[index])

    cv2.imshow('video frame',frame)
    if cv2.waitKey(1)==ord('q'):
        break

