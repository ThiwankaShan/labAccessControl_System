from faceDetection import *  

def main():
    
    is_newUsers=str(input("are there any new users? \nEnter y to yes \nEnter n to No\n"))

    if is_newUsers.lower()=='y':
        is_reset=str(input("do you want to reset all the data files and start fresh? \nEnter y to yes \nEnter n to No\n"))

        if is_reset.lower()=='y':
            resetSystem()
        load_newFaces()
        recognize_faces()
    
    elif is_newUsers.lower()=='n':
        recognize_faces()
    



def resetSystem():
    ## remove encodes.npz and names.npz data, move known_faces images to new_faces images

    known_directory="known_faces/"
    try:
        os.remove("encodes.npz")
        os.remove("names.npz")
        for fileName in os.listdir(known_directory):
            os.rename(f"known_faces/{fileName}",f"new_faces/{fileName}")
        print("files reseted successfully")
    except:
        print("something went  wrong when resetting files")

main()
