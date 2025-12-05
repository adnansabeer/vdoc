import face_recognition
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.label import Label
from kivymd.uix.screen import Screen
import cv2
import time
import os


class CameraScreen(Screen):
    def __init__(self, nav_bar_2, **kwargs):
        super().__init__(name="Camera", **kwargs)

        self.next_btn = MDRaisedButton(text="Next", disabled=True)
        nav_bar_2.add_widget(BoxLayout()) 
        nav_bar_2.add_widget(self.next_btn)
        self.next_btn.bind(on_release=self.info_screen)
        self.add_widget(nav_bar_2)

        label = Label(
            text='Tap the camera icon to take a picture.',
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=10,
            font_size=24
        )

        self.img_path = ""
        self.captured_frame = None 

        self.img_widget = Image(
            source="",
            allow_stretch=True,
            keep_ratio=True,
            size_hint=(None, None),
            size=(600, 300),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )

        layout = BoxLayout(
            spacing=10,
            padding=10,
        )

        button_layout = BoxLayout(
            orientation='vertical',
            spacing=10,
            padding=10,
            pos_hint={'center_x': 0.0, 'center_y': 0.4},
            size_hint_y=None,
            height=50
        )

        self.btn_capture = MDIconButton(
            icon="camera",
            pos_hint={"center_x": 0.5},
            on_release=self.take_picture
        )

        self.btn_check = MDIconButton(
            icon="check",
            pos_hint={"center_x": 0.5},
            on_release=self.save_picture
        )
        self.btn_check.disabled = True  

        self.main_cam_box = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=20
        )

        self.main_cam_box.add_widget(label)
        layout.add_widget(self.img_widget)

        button_layout.add_widget(self.btn_capture)
        button_layout.add_widget(self.btn_check)

        layout.add_widget(button_layout)
        self.main_cam_box.add_widget(layout)

        self.message_label = Label(
            text="",
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=30,
            font_size=18,
            pos_hint= {'center_x': 0.5,'center_y': 1},

        )
        self.main_cam_box.add_widget(self.message_label)

        self.add_widget(self.main_cam_box)

    def show_message(self, text, color):
        self.message_label.text = text
        self.message_label.color = color

    def save_picture(self, instance):
        if self.captured_frame is None:
            self.show_message("No picture captured to save.", (1, 0, 0, 1))
            return

        rgb_frame = self.captured_frame[:, :, ::-1]  
        face_locations = face_recognition.face_locations(rgb_frame)

        if len(face_locations) == 0:
            self.show_message("No faces detected. Please try again.", (1, 0.5, 0, 1))
            return

        self.img_path = f"captured_{int(time.time())}.jpg"
        cv2.imwrite(self.img_path, self.captured_frame)
        print(f"Image saved to {self.img_path}")

        self.img_widget.source = self.img_path
        self.img_widget.reload()

        self.show_message("Image saved successfully!", (0, 0.6, 0, 1))

        self.btn_capture.disabled = True
        self.btn_check.disabled = True
        self.next_btn.disabled = False
        
    def take_picture(self, instance):
        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            self.show_message("Cannot access camera", (1, 0, 0, 1))
            return

        for _ in range(5):
            cam.read()

        ret, frame = cam.read()
        cam.release()

        if ret:
            self.captured_frame = frame

            temp_path = "temp_preview.jpg"
            cv2.imwrite(temp_path, frame)
            self.img_widget.source = temp_path
            self.img_widget.reload()

            self.show_message("Picture captured (not saved yet).", (0, 0, 0, 1))

            self.btn_check.disabled = False 
            self.btn_capture.disabled = False
            self.next_btn.disabled = True   
        else:
            self.show_message("Failed to capture image.", (1, 0, 0, 1))

    def info_screen(self, instance):
        self.parent.current = 'Info'
