# Acess controll with face recognition and card scanner 
![Python](https://img.shields.io/badge/Python-3.8.5-3772A2)  ![Arduino](https://img.shields.io/badge/-Arduino-00989D)


## Setup project

* Keep images in new_faces folder
* Name images with users ID ` 5423.jpg`
* Create a virtual environment : ` virtualenv venv`
* Acrivate virtual environment: ` source venv/bin/activate`
* Install dependencies : ` pip install -r requirements.txt`
* Configure database with config file
* Run main.py : ` python main.py`


## To do 
- [ ] Card scanner module
    - [ ] Generate token
    - [ ] Write token to card
    - [ ] Read card
    - [ ] Reset card 
- [ ] User CRUD
- [ ] Combine front-end with back-end
- [ ] Refactor face recognition module 
- [ ] Camera feed module

### Completed tasks
- [x] Set up SqlAlchemy ORM
- [x] Set up database models  
- [x] Face recognition module 
	- [x] Generate encodes
	- [x] Recognition
- [x] Reset function
	- [x] Backup data 
	- [x] Clear db tables 
- [x] GUI designs (pyqt5 designer)