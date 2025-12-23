## Demo

<img width="996" height="784" alt="image" src="https://github.com/user-attachments/assets/64c10776-74cc-4135-b345-f427c4399fd5" />
<img width="997" height="789" alt="image" src="https://github.com/user-attachments/assets/da9a701a-d125-45b4-8ff5-ea82b1ad2561" />
<img width="999" height="786" alt="image" src="https://github.com/user-attachments/assets/99fae415-3317-4f14-baa8-f064382e6d47" />
<img width="997" height="780" alt="image" src="https://github.com/user-attachments/assets/11473195-73e8-4efe-9501-5286ddc92dbe" />



## Requirements

| Component              | Version |
|------------------------|---------|
| Python                 | 3.10    |
| Kivy                   | 2.3.1   |
| KivyMD                 | 1.2.0   |
| OpenCV                 | 4.12.0.88 |
| face-recognition       | 1.3.0   |
| mysql-connector-python | 9.5.0   |
---

## Setup & Run

Install dependencies:

```bash
pip install kivy==2.3.1 kivymd==1.2.0 opencv-python face-recognition mysql-connector-python
```

## System Requirements

- Camera  
- MySQL server  

## Features (Completed)

- Camera-based face capture  
- Basic face recognition  
- Patient information input  
- Guided medical checkup workflow  
- Individual and full checkup modes  
- Step-by-step on-screen instructions  
- Display of sample medical readings  
- MySQL database storage  

---

## Features (In Progress)

- Microphone input for voice-based patient identification  
- Automatic update of patient medical records upon recognition  

---

## Features (To Do)

- Role-based access control (patients, nurses, admins)  
- Patient list management and editing for nurses and admins  
- On-screen virtual keyboard  


## Notes

- Medical values are sample readings  
- Face recognition uses local camera input and image files  
- Database tables initialize automatically on first run  

## Project Structure

VDOC
  - vdoc.py        # Main application entry point
  - vdoc.kv        # UI layout
  - video.py       # Camera handling
  - face.py        # Face recognition logic
  - info.py        # Patient info screen
  - database.py    # Database operations


