import face_recognition
import os

image_folder = os.path.dirname(__file__)

img5_filename = None
for file in os.listdir(image_folder):
    if file.lower().startswith("img5.") and file.lower().endswith(('.jpg', '.jpeg', '.png')):
        img5_filename = file
        break

if not img5_filename:
    print("img5 image file not found!")
    exit()

img5_path = os.path.join(image_folder, img5_filename)

img5_encoding = face_recognition.face_encodings(face_recognition.load_image_file(img5_path))
if not img5_encoding:
    print(f"No face found in {img5_filename}")
    exit()
img5_encoding = img5_encoding[0]

matched = False
for file in os.listdir(image_folder):
    if file == img5_filename:
        continue
    if not file.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    file_path = os.path.join(image_folder, file)
    image = face_recognition.load_image_file(file_path)
    encodings = face_recognition.face_encodings(image)

    if not encodings:
        print(f"No face found in {file}")
        continue

    result = face_recognition.compare_faces([img5_encoding], encodings[0])[0]
    if result:
        print(f"Match found: {file}")
        matched = True
        break

if not matched:
    print("No matching image found.")
