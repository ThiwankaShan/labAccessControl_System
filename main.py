from faceDetection import *  

def main():
    
    is_newUsers=str(input("are there any new users? \nEnter y to yes \nEnter n to No\n"))

    if is_newUsers.lower()=='y':

        is_reset=str(input("\ndo you want to reset all the data files and start fresh? \nEnter y to yes \nEnter n to No\n"))
        if is_reset.lower()=='y':
            resetSystem()
        create_user()
        main()
    
    elif is_newUsers.lower()=='n':
        id=int(input('\nEnter your id : ')) ## this will be provided from the cardscanner module as an argument

        if recognize_face(id):        
            users = session.query(Users).filter(Users.id==id)
            for user in users:
                userName = user.name
            print(f"Acesss granted\n Welcome {userName}")
        else :
            print("Access denied")
    
    else:
        print('input not valid')
        main()


def resetSystem():
    ## remove encodes.npz and names.npz data, move known_faces images to new_faces images

    known_directory="known_faces/"
    try:
        Users.__table__.drop(engine)    
        Base.metadata.create_all(engine)    
        for fileName in os.listdir(known_directory):
            os.rename(f"known_faces/{fileName}",f"new_faces/{fileName}")
        print("files reseted successfully")
    except:
        print("something went  wrong when resetting files")

def create_user():
    ## create new user and store user details in db

    userName = str(input('Enter user name : '))
    regID = str(input("Enter registration id : ")) 
    encodes = generate_faceEncode(regID)

    userObj = Users(name=userName, id = regID, encode= jsonSerialize(encodes))
    session.add(userObj)
    session.commit()

main()
