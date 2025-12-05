from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton, MDRectangleFlatButton, MDRaisedButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from datetime import datetime
from kivy.uix.widget import Widget
import mysql.connector as mysql
import cv2
import time
import os
import face_recognition

dob_var = ""
gender_var = ""
first_name_var = ""
last_name_var = ""

class InfoScreen(Screen):
    def __init__(self,nav_bar, **kwargs):
        super().__init__(name="Info", **kwargs)

        next_btn = MDRaisedButton(text="Next")
        nav_bar.add_widget(Widget())
        nav_bar.add_widget(next_btn)
        next_btn.bind(on_release=self.med_screen)

        self.add_widget(nav_bar)


        grid = GridLayout(
            cols = 2,
            padding = 35,
            spacing = 50
        )
        info_box = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=20
        )
        self.info_box = info_box

        f_label = Label(
            text='First Name:',
            color=(0, 0, 0, 1),
            size_hint=(None, None),
            size=(30, 50),  
            font_size=20,
            halign='right',
            valign='center',
        )
        self.f_label = f_label
        

        first_name = MDTextField(
            mode = 'rectangle',
            size_hint= (None, None),
            size = (450, 50),
        )
        self.first_name = first_name
        first_name.bind(focus  = self.f_label_1)

        f_button = MDIconButton(
            icon = 'microphone'
        )
        self.f_button = f_button

        f_box = BoxLayout(
            spacing = 10
        )
        self.f_box = f_box
        f_box.add_widget(first_name)
        f_box.add_widget(f_button)

        l_label = Label(
            text = 'Last Name:',
            color=(0, 0, 0, 1),
            size_hint=(None, None),
            size=(30, 50),  
            font_size=20,
            halign='right',
            valign='center',
        )
        self.l_label = l_label

        last_name = MDTextField(
            mode = 'rectangle',
            size_hint= (None, None),
            size = (450, 50),
        )
        self.last_name = last_name
        last_name.bind(focus  = self.l_label_1)

        l_button = MDIconButton(
            icon = 'microphone',
            size_hint= (None, None),
            size = (20,20)
        )
        self.l_button = l_button

        l_box = BoxLayout(spacing = 10)
        self.l_box = l_box
        l_box.add_widget(last_name)
        l_box.add_widget(l_button)

        grid.add_widget(f_label)
        grid.add_widget(f_box)

        grid.add_widget(l_label)
        grid.add_widget(l_box)

        info_box.add_widget(grid)

        sec_box = BoxLayout(
            spacing =20,
            padding = 20,
            pos_hint = {'center_x': 0.5,'center_y': 1}
        )
        dob = BoxLayout(
            orientation= 'vertical',
            spacing = 20,
            padding = 20
        )
        self.dob = dob

        d_label = Label(
            text = 'Date of Birth',
            color = (0,0,0,1),
            pos_hint = {'center_x': 0.45}
        )
        self.d_label = d_label

        dmy = BoxLayout(
            spacing = 5
        )
        self.dmy = dmy

        day = MDRectangleFlatButton(
            text = 'DD'
        )
        self.day = day

        day_menu_items = [
            {"text": str(i), "on_release": lambda x=str(i): self.set_day(x)} for i in range(1, 32)
        ]

        day_menu = MDDropdownMenu(
            caller=day,
            items=day_menu_items,
            width_mult=4,
        )
        self.day_menu = day_menu

        day.bind(on_release=lambda *args: day_menu.open())

        month = MDRectangleFlatButton(
            text = 'MM'
        )
        self.month = month

        month_menu_items = [
            {"text": month, "on_release": lambda x=month: self.set_month(x)}
            for month in ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"]
        ]


        month_menu = MDDropdownMenu(
            caller=month,
            items=month_menu_items,
            width_mult=4,
        )
        self.month_menu = month_menu

        month.bind(on_release=lambda *args: month_menu.open())


        year = MDRectangleFlatButton(
            text = 'YYYY'
        )
        self.year = year

        current_year = datetime.now().year
        year_menu_items = [
            {"text": str(y), "on_release": lambda x=str(y): self.set_year(x)}
            for y in range(current_year, 1899, -1) 
        ]


        year_menu = MDDropdownMenu(
            caller=year,
            items=year_menu_items,
            width_mult=4,
        )
        self.year_menu = year_menu

        year.bind(on_release=lambda *args: year_menu.open())

        dmy.add_widget(day)
        dmy.add_widget(month)
        dmy.add_widget(year)

        dob.add_widget(d_label)
        dob.add_widget(dmy)
        sec_box.add_widget(dob)

        g_box = BoxLayout(
            orientation= 'vertical',
            spacing = 20,
            padding = 20     
        )
        g_label =  Label(
            text = 'Gender',
            color = (0,0,0,1),
            pos_hint = {'center_x': 0.5}
        )
        self.g_label = g_label

        gender_button = MDRectangleFlatButton(
            text="Select Gender",
            pos_hint={"center_x": 0.5},
        )
        self.gender_button = gender_button

        g_menu_items = [
            {"text": "Male", "on_release": lambda x="Male": self.set_gender(x)},
            {"text": "Female", "on_release": lambda x="Female": self.set_gender(x)},
        ]
        g_menu = MDDropdownMenu(
            caller=gender_button,
            items=g_menu_items,
            width_mult=4,
        )
        self.g_menu = g_menu

        gender_button.bind(on_release=lambda *args: g_menu.open())
        g_box.add_widget(g_label)
        g_box.add_widget(gender_button)
        
        sec_box.add_widget(g_box)

        info_box.add_widget(sec_box)
        label = Label(
            size_hint_y= None,
            height = 30
        )
        info_box.add_widget(label)
        self.add_widget(info_box)

    def set_gender(self, gender):
        self.gender_button.text = gender
        self.g_menu.dismiss()
        
    def set_day(self, day):
        self.day.text = day
        self.day_menu.dismiss()

    def set_month(self, month):
        self.month.text = month
        self.month_menu.dismiss()

    def set_year(self, year):
        self.year.text = year
        self.year_menu.dismiss()

    def f_label_1(self, instance, focus):
        if not focus: 
            if instance.text == '':
                pass
            else:
                self.first_name_var_TEMP = instance.text

    def l_label_1(self, instance, focus):
        if not focus: 
            if instance.text == '':
                pass
            else:
                self.last_name_var_TEMP = instance.text

    def med_screen(self, instance):
        if (self.first_name.text == '' or
            self.last_name.text == '' or
            self.gender_button.text == 'Select Gender' or
            self.day.text == 'DD' or
            self.month.text == 'MM' or
            self.year.text == 'YYYY'):
            
            if not hasattr(self, 'next_message'):
                self.next_message = Label(
                    text="",
                    color=(1, 0, 0, 1),
                    size_hint=(None, None),
                    size=(400, 10),
                    halign='center',
                    valign='middle',
                    size_hint_y= None,
                    height = 10,
                    pos_hint={'center_x': 0.5, 'y': 0.85}  
                )
                self.info_box.add_widget(self.next_message)

            if self.first_name.text == '':
                self.next_message.text = "Please enter your first name"
            elif self.last_name.text == '':
                self.next_message.text = "Please enter your last name"
            elif self.day.text == 'DD' or self.month.text == 'MM' or self.year.text == 'YYYY':
                self.next_message.text = "Please select your date of birth"
            elif self.gender_button.text == 'Select Gender':
                self.next_message.text = "Please select your gender"

            return
    
        global dob_var, gender_var, first_name_var, last_name_var
        dob_var = f"{self.day.text}-{self.month.text}-{self.year.text}"
        gender_var = self.gender_button.text
        first_name_var = self.first_name.text
        last_name_var = self.last_name.text
        self.parent.current = 'Medical'



