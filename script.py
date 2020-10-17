import face_recognition as fr
import cv2

known_image = fr.load_image_file("known_faces/face.jpg")
known_encoding = fr.face_encodings(known_image)[0]

cap = cv2.VideoCapture("video/video.mp4")

while (cap.isOpened()):
    ret, frame = cap.read()
    
    face_locations=fr.face_locations(frame)
    unknown_encoding = fr.face_encodings(frame,face_locations)

    for unknown_face in unknown_encoding:
        result=fr.compare_faces([known_encoding],unknown_face)

        if True in result:
            print('keira knightley')
    cv2.imshow('video frame',frame)
    if cv2.waitKey(1)==ord('q'):
        break
