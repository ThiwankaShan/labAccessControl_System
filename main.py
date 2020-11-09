from faceDetection import *  
import sys

def main():
    
    is_newUsers=str(input("\nare there any new users? \nEnter y to yes \nEnter n to No\nEnter q to exit\n"))

    if is_newUsers.lower()=='y':

        is_reset=str(input("\ndo you want to reset all the data files and start fresh? \nEnter y to yes \nEnter n to No\n"))
        if is_reset.lower()=='y':
            resetSystem()
        create_user()
    
    elif is_newUsers.lower()=='n':
        id=int(input('\nEnter your id : ')) ## this will be provided from the cardscanner module as an argument

        if recognize_face(id):        
            users = session.query(Users).filter(Users.id==id)
            for user in users:
                userName = user.name
            print('\n****************************************\n')
            print(f"\nAcesss granted\nWelcome {userName}\n")
            print('\n****************************************\n')
        else :
            print("Access denied")
    elif is_newUsers.lower()=='q':
        sys.exit()

    else:
        print('input not valid')
    



def resetSystem():
    ## (deletes users table), move known_faces images to new_faces images
    ## reset db will be implement instead of delete only users table 


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

    userName = str(input('\nEnter user name : '))
    regID = str(input("Enter registration id : ")) 
    encodes = generate_faceEncode(regID)

    userObj = Users(name=userName, id = regID, encode= jsonSerialize(encodes))
    session.add(userObj)
    session.commit()

while True:
    main()
