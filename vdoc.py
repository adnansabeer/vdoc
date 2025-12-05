from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.card import MDCard
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.textfield import MDTextFieldRect, MDTextField
from kivymd.uix.button import MDFlatButton, MDFillRoundFlatIconButton,MDRectangleFlatIconButton ,MDIconButton, MDRoundFlatButton, MDRaisedButton, MDFillRoundFlatButton, MDRectangleFlatButton
from kivy.properties import StringProperty, BooleanProperty, Clock
from video import CameraScreen
from info import InfoScreen
from database import save_result, full_checkup_save


class main(Screen):
    pass

class vdocApp(MDApp):
    save_result()
    instructions = [
    '''
                            Blood Pressure Measurement

    1. Please insert your arm into the cuff opening on the side
    of the robot.

    2. The cuff will now tighten — please stay still and relaxed.

    3. Measurement in progress. You may remove your arm
    once complete.
    ''',

    '''
                            Blood Oxygen Level (SpO2)

    1. Place your index finger into the slot just below the screen.

    2. Hold still while your oxygen level is being measured.

    3. You may now remove your finger.
    ''',

    '''
                                    Body Temperature

    1. Stand directly in front of the robot.

    2. Align your forehead with the sensor above the screen.

    3. Remain still while your temperature is scanned.
    ''',

    '''
                                    Height Measurement

    1. Stand upright below the sensor rod extended above.

    2. The rod will lower gently. Please remain still.

    3. Height has been recorded successfully.
    ''',

    '''
                                    Weight Measurement

    1. Step onto the weighing platform extended at the bottom 
    of the robot.

    2. Stand still while your weight is recorded.

    3. You may now step down.
    ''',

    '''
                            Breathing Rate Test (Spirometer)

    1. Take the spirometer and disposable mouthpiece from 
    the dispenser.

    2. Follow the video instructions on the screen to assemble.

    3. Take a deep breath and blow steadily into the tube.

    4. Dispose of the used mouthpiece in the waste slot.
    ''',

    '''
                                Blood Sample Collection

    1. Collect the blood collection kit from the dispenser.

    2. Watch the instruction video to guide you through the 
    process.

    3. Place the filled test tube into the tray labeled 'Blood Sample'.

    4. Close the tray after placing the sample.
    ''',

    '''
                            Urine Sample Collection (Optional)

    1. Take the urine sample container from the dispenser.

    2. Collect your sample in privacy.

    3. Return and place the sealed container into the tray 
    labeled 'Urine Sample'.

    4. Close the tray once done.
    '''
    ]

    bol = BooleanProperty(True)

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        Builder.load_file('vdoc.kv')

    def camera_cancel(self, instance):
        self.root.ids.main_screen.remove_widget(self.home_card)
    def open_popup(self):
        self.bol = False
        screen_manager = ScreenManager()
        self.screen_manager = screen_manager

        nav_bar_2 = BoxLayout(orientation='horizontal', padding=20, spacing=20)
        cancel = MDRaisedButton(text="Cancel")
        cancel.bind(on_release = self.camera_cancel)
        nav_bar_2.add_widget(cancel)
        camera_screen = CameraScreen(nav_bar_2=nav_bar_2)
        screen_manager.add_widget(camera_screen)
        
        home_card = MDCard(
            orientation = 'vertical',
            spacing=10,
            elevation=10,
            padding=20,
            size_hint = (None, None),
            size = (700, 500),
            radius=[24, 24, 24, 24],
            pos_hint = {'center_x': 0.5,'center_y': 0.5}
        )
        self.home_card = home_card



        Screen0 = Screen(
            name = 'Medical'
        )

        full = MDFillRoundFlatIconButton(
            text='Full Medical Checkup',
            icon = 'hospital-box',
            font_size=32,
            pos_hint= {'center_x': 0.5,'center_y': 0.0}
        )
        self.full = full
        full.bind(on_release = self.full_checkup)
        screen_box = BoxLayout(
            orientation= 'vertical',
            spacing = 20,
            padding = 20
        )

        grid = GridLayout(
            cols= 2,
            spacing= 25,
            padding= 10,
            size_hint= (0.5, 0.5),
            pos_hint= {'center_x': 0.38,'center_y': 0.0}
        )

        bp = MDRectangleFlatIconButton(
            text='Blood Pressure',
            icon = 'heart-pulse',
            font_size=22,
            size_hint=(1, None),
            height=50
        )
        bp.bind(on_release = self.bloodp)

        spo2 = MDRectangleFlatIconButton(
            text='Spirometer',
            icon = 'lungs',
            font_size=22,
            size_hint=(1, None),
            height=50
        )
        spo2.bind(on_release = self.spiro)

        temperature = MDRectangleFlatIconButton(
            text='Temperature',
            icon = 'thermometer',
            font_size=22,
            size_hint=(1, None),
            height=50
        )
        temperature.bind(on_release = self.temp)

        height = MDRectangleFlatIconButton(
            text='Height',
            icon = 'ruler',
            font_size=22,
            size_hint=(1, None),
            height=50
        )
        height.bind(on_release = self.height_func)

        weight = MDRectangleFlatIconButton(
            text='Weight',
            icon = 'scale-bathroom',
            font_size=22,
            size_hint=(1, None),
            height=50
        )
        weight.bind(on_release = self.weight_func)

        breathing = MDRectangleFlatIconButton(
            text='Breathing',
            icon = 'weather-windy',
            font_size=22,
            size_hint=(1, None),
            height=50
        )
        breathing.bind(on_release = self.breath)

        blood_sample = MDRectangleFlatIconButton(
            text='Blood Sample',
            icon = 'blood-bag',
            font_size=22,
            size_hint=(1, None),
            height=50
        )
        blood_sample.bind(on_release = self.blood)

        urine_sample = MDRectangleFlatIconButton(
            text='Urine Sample',
            icon = 'beaker-outline',
            font_size=22,
            size_hint=(1, None),
            height=50
        )
        urine_sample.bind(on_release = self.urine)

        empty_l = Label(
            size_hint_y= None,
            height = 30
        )
        grid.add_widget(bp)
        grid.add_widget(spo2)
        grid.add_widget(temperature)
        grid.add_widget(height)
        grid.add_widget(weight)
        grid.add_widget(breathing)
        grid.add_widget(blood_sample)
        grid.add_widget(urine_sample)

        screen_box.add_widget(empty_l)
        screen_box.add_widget(full)
        screen_box.add_widget(grid)
        Screen0.add_widget(screen_box)
        screen_manager.add_widget(Screen0)
        home_card.add_widget(screen_manager)

        nav_bar = BoxLayout(orientation='horizontal', padding=20, spacing=20)
        cancel = MDRaisedButton(text="Cancel")
        cancel.bind(on_release = self.remove)
        nav_bar.add_widget(cancel)

        info_screen = InfoScreen(nav_bar=nav_bar)
        screen_manager.add_widget(info_screen)
        
        self.root.ids.main_screen.add_widget(home_card)

    def remove(self, instacne):
        self.root.ids.main_screen.remove_widget(self.home_card)
        self.bol = True
        
    def full_checkup(self, instance):
        self.root.ids.main_screen.remove_widget(self.home_card)
        self.button_refs = {}
        self.box_refs = {}
        self.bol = False
        card = MDCard(
            orientation = 'vertical',
            spacing=10,
            elevation=10,
            padding=10,
            size_hint = (None, None),
            size = (700, 500),
            radius=[24, 24, 24, 24],
            pos_hint = {'center_x': 0.5,'center_y': 0.5}
        )
        self.card = card

        screen_list = ['BP', 'OXYGEN', 'BODYTEMP', 'HEIGHT', 'WEIGHT', 'BREATHING', 'BSAMPLE', 'USAMPLE']
        self.screen_list = screen_list

        screen_manager = ScreenManager()
        self.screen_manager = screen_manager

        
        c=0
        for x in screen_list:
            Screen1 = Screen(name = x)

            label = Label(
                markup = True,
                text=f'[size=20]{self.instructions[c]}[/size]',
                color=(0, 0, 0, 1),
                halign='left',
                valign='top'
            )
            label.bind(size=label.setter('text_size'))
            self.label = label

            start_button = MDFillRoundFlatButton(
                text = 'start',
                font_size = 24,
                pos_hint={'center_x': 0.5, 'y': 0},
                size_hint=(None, None),
                size=(150, 50)
            )
            self.start_button = start_button
            start_button.bind(on_release = self.start)


            main_box = BoxLayout(
                    orientation= 'vertical',
                    padding= 20,
                    spacing = 20,                
            )
            self.main_box = main_box
            
            main_box.add_widget(label)
            main_box.add_widget(start_button)
            Screen1.add_widget(main_box)
            screen_manager.add_widget(Screen1)

            self.button_refs[x] = start_button
            self.box_refs[x] = main_box

            c+=1

        close = MDRaisedButton(
            text = 'Close',
        )
        self.close = close
        close.bind(on_release = self.rem)

        spacer = Widget(size_hint_x=1)
        box = BoxLayout(
            padding = 15,
            spacing = 20,
            size_hint_y=None,
            height=100
        )
        self.box = box


        box.add_widget(close)
        box.add_widget(spacer)

        card.add_widget(screen_manager)
        card.add_widget(box)
        self.root.ids.main_screen.add_widget(card)

    def rem(self, instance):
        self.bol = True
        self.root.ids.main_screen.remove_widget(self.card)
        full_checkup_save()
    
    def start(self, instace):

        new_card = MDCard(
            orientation = 'vertical',
            spacing=10,
            padding=10, 
            size_hint = (None, None),
            size = (700, 500),
            radius=[24, 24, 24, 24],
            pos_hint = {'center_x': 0.5,'center_y': 0.5}
        )
        self.new_card = new_card
        if self.screen_manager.current.upper()=='BP':
            label = Label(
                text = 
                '''
    Blood Pressure

Systolic: 120 mmHg
Diastolic: 80 mmHg
Heart Rate: 72 BPM
                ''',
                color = (0, 0, 0, 1),
                font_size = 40
            )
            new_card.add_widget(label)
            
        if self.screen_manager.current.upper()=='OXYGEN':
            label = Label(
                text = 
                '''
    Blood Oxygen Level (SpO2)

    Oxygen Saturation: 98%
    Pulse Rate: 74 BPM
                ''',
                color = (0, 0, 0, 1),
                font_size = 40
            )
            new_card.add_widget(label)

        if self.screen_manager.current.upper()=='BODYTEMP':
            label = Label(
                text = 
                '''
    Body Temperature

Temperature: 36.7 °C
                ''',
                color = (0, 0, 0, 1),
                font_size = 40
            )
            new_card.add_widget(label)

        if self.screen_manager.current.upper()=='HEIGHT':
            label = Label(
                text = 
                '''
        Height

Height: 170 cm
                ''',
                color = (0, 0, 0, 1),
                font_size = 40
            )
            new_card.add_widget(label)

        if self.screen_manager.current.upper()=='WEIGHT':
            label = Label(
                text = 
                '''
        Weight

Weight: 65 kg
BMI: 22.5
                ''',
                color = (0, 0, 0, 1),
                font_size = 40
            )
            new_card.add_widget(label)


        if self.screen_manager.current.upper()=='BREATHING':
            label = Label(
                text = 
                '''
    Breathing Rate (Spirometer)

Breathing Rate: 16 breaths/min
Lung Capacity: 3.5 L
                ''',
                color = (0, 0, 0, 1),
                font_size = 40
            )
            new_card.add_widget(label)

        if self.screen_manager.current.upper()=='BSAMPLE':
            label = Label(
                text = 
                '''
    Blood Sample

    Collected: Yes
                ''',
                color = (0, 0, 0, 1),
                font_size = 40
            )
            new_card.add_widget(label)

        if self.screen_manager.current.upper()=='USAMPLE':
            label = Label(
                text = 
                '''
    Urine Sample

    Collected: Yes
                ''',
                color = (0, 0, 0, 1),
                font_size = 40
            )
            new_card.add_widget(label)



        cancel_2 = MDFlatButton(
            text = 'Close',
        )
        self.cancel_2 = cancel_2
        cancel_2.bind(on_release = self.rem2)

        new_card.add_widget(cancel_2)
        self.root.ids.main_screen.add_widget(new_card)

    def rem2(self, instance):
        self.root.ids.main_screen.remove_widget(self.new_card)

        current =  self.screen_manager.current.upper()
        if current in self.box_refs and current in self.button_refs:
            box = self.box_refs[current]
            button = self.button_refs[current]

            if button in box.children:
                box.remove_widget(button)
                next  =MDRaisedButton(
                    text = 'Next',
                )
                self.next = next
                next.bind(on_release = self.next_screen)
                
                prev  =MDRaisedButton(
                    text = 'Previous',
                )
                self.prev = prev

                mini_box = BoxLayout(
                    spacing = 10,
                    padding = 10,
                    size_hint= (0.5, None),
                    height = 20,
                    pos_hint= {'center_x': 0.6,'center_y': 0.0}
                )
                prev.bind(on_release = self.prev_screen)
                mini_box.add_widget(prev)
                mini_box.add_widget(next)
                box.add_widget(mini_box)

    def next_screen(self, instance):
        current_index = self.screen_list.index(self.screen_manager.current)
        if current_index < len(self.screen_list) - 1:
            self.screen_manager.transition.direction = 'left'
            next_screen_name = self.screen_list[current_index + 1]
            self.screen_manager.current = next_screen_name
    
    def prev_screen(self, instance):
        current_index = self.screen_list.index(self.screen_manager.current)
        if current_index > 0:
            self.screen_manager.transition.direction = 'right'
            prev_screen_name = self.screen_list[current_index - 1]
            self.screen_manager.current = prev_screen_name

    def bloodp(self, instance):
        self.root.ids.main_screen.remove_widget(self.home_card)
        self.bol = False
        bp_card = MDCard(
            orientation = 'vertical',
            spacing=10,
            elevation=10,
            padding=20,
            size_hint = (None, None),
            size = (700, 500),
            radius=[24, 24, 24, 24],
            pos_hint = {'center_x': 0.5,'center_y': 0.5}
        )
        self.bp_card = bp_card

        bp_text = self.instructions[0]

        bp_label = Label(
                markup = True,
                text=f'[size=20]{bp_text}[/size]',
                color=(0, 0, 0, 1),
                halign='left',
                valign='top'
            )
        bp_start_button = MDFillRoundFlatButton(
                text = 'start',
                font_size = 24,
                pos_hint={'center_x': 0.5, 'y': 0},
                size_hint=(None, None),
                size=(150, 50)
            )
        self.bp_start_button = bp_start_button
        bp_start_button.bind(on_release = self.bp_start)
        
        cancel = MDRaisedButton(
            text = 'Cancel'
        )
        cancel.bind(on_release = self.bp_cancel)
        bp_box = BoxLayout(
                orientation= 'vertical',
                padding= 20,
                spacing = 20,                
            )

        bp_box.add_widget(bp_label)
        bp_box.add_widget(bp_start_button)
        bp_card.add_widget(bp_box)
        bp_card.add_widget(cancel)
        self.root.ids.main_screen.add_widget(bp_card)

    def bp_start(self, instance):
        self.root.ids.main_screen.remove_widget(self.bp_card)
        bp_new_card = MDCard(
            orientation = 'vertical',
            spacing=10,
            elevation = 10,
            padding=10, 
            size_hint = (None, None),
            size = (700, 500),
            radius=[24, 24, 24, 24],
            pos_hint = {'center_x': 0.5,'center_y': 0.5}
        )
        self.bp_new_card = bp_new_card
        label = Label(
                text = 
                '''
    Blood Pressure

Systolic: 120 mmHg
Diastolic: 80 mmHg
Heart Rate: 72 BPM
                ''',
            color = (0, 0, 0, 1),
            font_size = 40
        )
        bp_new_card.add_widget(label)
        self.root.ids.main_screen.add_widget(bp_new_card)
        cancel_2 = MDFlatButton(
            text = 'Close',
        )
        self.cancel_2 = cancel_2
        cancel_2.bind(on_release = self.bp_close)

        bp_new_card.add_widget(cancel_2)

    def bp_cancel(self, instance):
        self.root.ids.main_screen.remove_widget(self.bp_card)
    def bp_close(self, instance):
        self.root.ids.main_screen.remove_widget(self.bp_new_card)


    def spiro(self, instance):
        self.root.ids.main_screen.remove_widget(self.home_card)
        self.bol = False
        spo2_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=20,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.spo2_card = spo2_card

        spo2_text = self.instructions[1]

        spo2_label = Label(
            markup=True,
            text=f'[size=20]{spo2_text}[/size]',
            color=(0, 0, 0, 1),
            halign='left',
            valign='top'
        )
        spo2_start_button = MDFillRoundFlatButton(
            text='start',
            font_size=24,
            pos_hint={'center_x': 0.5, 'y': 0},
            size_hint=(None, None),
            size=(150, 50)
        )
        self.spo2_start_button = spo2_start_button
        spo2_start_button.bind(on_release=self.spo2_start)

        cancel = MDRaisedButton(
            text='Cancel'
        )
        cancel.bind(on_release=self.spo2_cancel)
        spo2_box = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20,
        )

        spo2_box.add_widget(spo2_label)
        spo2_box.add_widget(spo2_start_button)
        spo2_card.add_widget(spo2_box)
        spo2_card.add_widget(cancel)
        self.root.ids.main_screen.add_widget(spo2_card)

    def spo2_start(self, instance):
        self.root.ids.main_screen.remove_widget(self.spo2_card)
        spo2_new_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=10,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.spo2_new_card = spo2_new_card
        label = Label(
            text=
            '''
        Blood Oxygen (SpO₂)

    Oxygen Saturation: 98%
    Pulse Rate: 74 BPM
            ''',
            color=(0, 0, 0, 1),
            font_size=40
        )
        spo2_new_card.add_widget(label)
        self.root.ids.main_screen.add_widget(spo2_new_card)
        cancel_2 = MDFlatButton(
            text='Close',
        )
        self.cancel_2 = cancel_2
        cancel_2.bind(on_release=self.spo2_close)

        spo2_new_card.add_widget(cancel_2)

    def spo2_cancel(self, instance):
        self.root.ids.main_screen.remove_widget(self.spo2_card)
    def spo2_close(self, instance):
        self.root.ids.main_screen.remove_widget(self.spo2_new_card)


    def temp(self, instance):
        self.root.ids.main_screen.remove_widget(self.home_card)
        self.bol = False
        temperature_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=20,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.temperature_card = temperature_card

        temperature_text = self.instructions[2]

        temperature_label = Label(
            markup=True,
            text=f'[size=20]{temperature_text}[/size]',
            color=(0, 0, 0, 1),
            halign='left',
            valign='top'
        )
        temperature_start_button = MDFillRoundFlatButton(
            text='start',
            font_size=24,
            pos_hint={'center_x': 0.5, 'y': 0},
            size_hint=(None, None),
            size=(150, 50)
        )
        self.temperature_start_button = temperature_start_button
        temperature_start_button.bind(on_release=self.temperature_start)

        cancel = MDRaisedButton(
            text='Cancel'
        )
        cancel.bind(on_release=self.temperature_cancel)
        temperature_box = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20,
        )

        temperature_box.add_widget(temperature_label)
        temperature_box.add_widget(temperature_start_button)
        temperature_card.add_widget(temperature_box)
        temperature_card.add_widget(cancel)
        self.root.ids.main_screen.add_widget(temperature_card)

    def temperature_start(self, instance):
        self.root.ids.main_screen.remove_widget(self.temperature_card)
        temperature_new_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=10,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.temperature_new_card = temperature_new_card
        label = Label(
            text=
            '''
        Body Temperature

    Temperature: 36.7 °C
            ''',
            color=(0, 0, 0, 1),
            font_size=40
        )
        temperature_new_card.add_widget(label)
        self.root.ids.main_screen.add_widget(temperature_new_card)
        cancel_2 = MDFlatButton(
            text='Close',
        )
        self.cancel_2 = cancel_2
        cancel_2.bind(on_release=self.temperature_close)

        temperature_new_card.add_widget(cancel_2)

    def temperature_cancel(self, instance):
        self.root.ids.main_screen.remove_widget(self.temperature_card)
    def temperature_close(self, instance):
        self.root.ids.main_screen.remove_widget(self.temperature_new_card)


    def height_func(self, instance):
        self.root.ids.main_screen.remove_widget(self.home_card)
        self.bol = False
        height_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=20,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.height_card = height_card

        height_text =self.instructions[3]

        height_label = Label(
            markup=True,
            text=f'[size=20]{height_text}[/size]',
            color=(0, 0, 0, 1),
            halign='left',
            valign='top'
        )
        height_start_button = MDFillRoundFlatButton(
            text='start',
            font_size=24,
            pos_hint={'center_x': 0.5, 'y': 0},
            size_hint=(None, None),
            size=(150, 50)
        )
        self.height_start_button = height_start_button
        height_start_button.bind(on_release=self.height_start)

        cancel = MDRaisedButton(
            text='Cancel'
        )
        cancel.bind(on_release=self.height_cancel)
        height_box = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20,
        )

        height_box.add_widget(height_label)
        height_box.add_widget(height_start_button)
        height_card.add_widget(height_box)
        height_card.add_widget(cancel)
        self.root.ids.main_screen.add_widget(height_card)

    def height_start(self, instance):
        self.root.ids.main_screen.remove_widget(self.height_card)
        height_new_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=10,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.height_new_card = height_new_card
        label = Label(
            text=
            '''
        Height

    Height: 170 cm
            ''',
            color=(0, 0, 0, 1),
            font_size=40
        )
        height_new_card.add_widget(label)
        self.root.ids.main_screen.add_widget(height_new_card)
        cancel_2 = MDFlatButton(
            text='Close',
        )
        self.cancel_2 = cancel_2
        cancel_2.bind(on_release=self.height_close)

        height_new_card.add_widget(cancel_2)

    def height_cancel(self, instance):
        self.root.ids.main_screen.remove_widget(self.height_card)
    def height_close(self, instance):
        self.root.ids.main_screen.remove_widget(self.height_new_card)

    def weight_func(self, instance):
        self.root.ids.main_screen.remove_widget(self.home_card)
        self.bol = False
        weight_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=20,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.weight_card = weight_card

        weight_text =self.instructions[4]

        weight_label = Label(
            markup=True,
            text=f'[size=20]{weight_text}[/size]',
            color=(0, 0, 0, 1),
            halign='left',
            valign='top'
        )
        weight_start_button = MDFillRoundFlatButton(
            text='start',
            font_size=24,
            pos_hint={'center_x': 0.5, 'y': 0},
            size_hint=(None, None),
            size=(150, 50)
        )
        self.weight_start_button = weight_start_button
        weight_start_button.bind(on_release=self.weight_start)

        cancel = MDRaisedButton(
            text='Cancel'
        )
        cancel.bind(on_release=self.weight_cancel)
        weight_box = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20,
        )

        weight_box.add_widget(weight_label)
        weight_box.add_widget(weight_start_button)
        weight_card.add_widget(weight_box)
        weight_card.add_widget(cancel)
        self.root.ids.main_screen.add_widget(weight_card)

    def weight_start(self, instance):
        self.root.ids.main_screen.remove_widget(self.weight_card)
        weight_new_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=10,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.weight_new_card = weight_new_card
        label = Label(
            text=
            '''
        Weight

    Weight: 65 kg
    BMI: 22.5
            ''',
            color=(0, 0, 0, 1),
            font_size=40
        )
        weight_new_card.add_widget(label)
        self.root.ids.main_screen.add_widget(weight_new_card)
        cancel_2 = MDFlatButton(
            text='Close',
        )
        self.cancel_2 = cancel_2
        cancel_2.bind(on_release=self.weight_close)

        weight_new_card.add_widget(cancel_2)

    def weight_cancel(self, instance):
        self.root.ids.main_screen.remove_widget(self.weight_card)
    def weight_close(self, instance):
        self.root.ids.main_screen.remove_widget(self.weight_new_card)


    def breath(self, instance):
        self.root.ids.main_screen.remove_widget(self.home_card)
        self.bol = False
        breathing_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=20,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.breathing_card = breathing_card

        breathing_text = self.instructions[5]

        breathing_label = Label(
            markup=True,
            text=f'[size=20]{breathing_text}[/size]',
            color=(0, 0, 0, 1),
            halign='left',
            valign='top'
        )
        breathing_start_button = MDFillRoundFlatButton(
            text='start',
            font_size=24,
            pos_hint={'center_x': 0.5, 'y': 0},
            size_hint=(None, None),
            size=(150, 50)
        )
        self.breathing_start_button = breathing_start_button
        breathing_start_button.bind(on_release=self.breathing_start)

        cancel = MDRaisedButton(
            text='Cancel'
        )
        cancel.bind(on_release=self.breathing_cancel)
        breathing_box = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20,
        )

        breathing_box.add_widget(breathing_label)
        breathing_box.add_widget(breathing_start_button)
        breathing_card.add_widget(breathing_box)
        breathing_card.add_widget(cancel)
        self.root.ids.main_screen.add_widget(breathing_card)

    def breathing_start(self, instance):
        self.root.ids.main_screen.remove_widget(self.breathing_card)
        breathing_new_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=10,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.breathing_new_card = breathing_new_card
        label = Label(
            text=
            '''
        Breathing Rate

    Breathing Rate: 16 breaths/min
    Lung Capacity: 3.5 L
            ''',
            color=(0, 0, 0, 1),
            font_size=40
        )
        breathing_new_card.add_widget(label)
        self.root.ids.main_screen.add_widget(breathing_new_card)
        cancel_2 = MDFlatButton(
            text='Close',
        )
        self.cancel_2 = cancel_2
        cancel_2.bind(on_release=self.breathing_close)

        breathing_new_card.add_widget(cancel_2)

    def breathing_cancel(self, instance):
        self.root.ids.main_screen.remove_widget(self.breathing_card)
    def breathing_close(self, instance):
        self.root.ids.main_screen.remove_widget(self.breathing_new_card)


    def blood(self, instance):
        self.root.ids.main_screen.remove_widget(self.home_card)
        self.bol = False
        blood_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=20,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.blood_card = blood_card

        blood_text = self.instructions[6]

        blood_label = Label(
            markup=True,
            text=f'[size=20]{blood_text}[/size]',
            color=(0, 0, 0, 1),
            halign='left',
            valign='top'
        )
        blood_start_button = MDFillRoundFlatButton(
            text='start',
            font_size=24,
            pos_hint={'center_x': 0.5, 'y': 0},
            size_hint=(None, None),
            size=(150, 50)
        )
        self.blood_start_button = blood_start_button
        blood_start_button.bind(on_release=self.blood_start)

        cancel = MDRaisedButton(
            text='Cancel'
        )
        cancel.bind(on_release=self.blood_cancel)
        blood_box = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20,
        )

        blood_box.add_widget(blood_label)
        blood_box.add_widget(blood_start_button)
        blood_card.add_widget(blood_box)
        blood_card.add_widget(cancel)
        self.root.ids.main_screen.add_widget(blood_card)

    def blood_start(self, instance):
        self.root.ids.main_screen.remove_widget(self.blood_card)
        blood_new_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=10,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.blood_new_card = blood_new_card
        label = Label(
            text=
            '''
        Blood Sample

    Hemoglobin: 14.2 g/dL
    Glucose: 95 mg/dL
            ''',
            color=(0, 0, 0, 1),
            font_size=40
        )
        blood_new_card.add_widget(label)
        self.root.ids.main_screen.add_widget(blood_new_card)
        cancel_2 = MDFlatButton(
            text='Close',
        )
        self.cancel_2 = cancel_2
        cancel_2.bind(on_release=self.blood_close)

        blood_new_card.add_widget(cancel_2)

    def blood_cancel(self, instance):
        self.root.ids.main_screen.remove_widget(self.blood_card)
    def blood_close(self, instance):
        self.root.ids.main_screen.remove_widget(self.blood_new_card)

    def urine(self, instance):
        self.root.ids.main_screen.remove_widget(self.home_card)
        self.bol = False
        urine_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=20,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.urine_card = urine_card

        urine_text = self.instructions[7]

        urine_label = Label(
            markup=True,
            text=f'[size=20]{urine_text}[/size]',
            color=(0, 0, 0, 1),
            halign='left',
            valign='top'
        )
        urine_start_button = MDFillRoundFlatButton(
            text='start',
            font_size=24,
            pos_hint={'center_x': 0.5, 'y': 0},
            size_hint=(None, None),
            size=(150, 50)
        )
        self.urine_start_button = urine_start_button
        urine_start_button.bind(on_release=self.urine_start)

        cancel = MDRaisedButton(
            text='Cancel'
        )
        cancel.bind(on_release=self.urine_cancel)
        urine_box = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20,
        )

        urine_box.add_widget(urine_label)
        urine_box.add_widget(urine_start_button)
        urine_card.add_widget(urine_box)
        urine_card.add_widget(cancel)
        self.root.ids.main_screen.add_widget(urine_card)

    def urine_start(self, instance):
        self.root.ids.main_screen.remove_widget(self.urine_card)
        urine_new_card = MDCard(
            orientation='vertical',
            spacing=10,
            elevation=10,
            padding=10,
            size_hint=(None, None),
            size=(700, 500),
            radius=[24, 24, 24, 24],
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.urine_new_card = urine_new_card
        label = Label(
            text=
            '''
        Urine Sample

    pH: 6.0
    Protein: Negative
            ''',
            color=(0, 0, 0, 1),
            font_size=40
        )
        urine_new_card.add_widget(label)
        self.root.ids.main_screen.add_widget(urine_new_card)
        cancel_2 = MDFlatButton(
            text='Close',
        )
        self.cancel_2 = cancel_2
        cancel_2.bind(on_release=self.urine_close)

        urine_new_card.add_widget(cancel_2)

    def urine_cancel(self, instance):
        self.root.ids.main_screen.remove_widget(self.urine_card)
    def urine_close(self, instance):
        self.root.ids.main_screen.remove_widget(self.urine_new_card)
vdocApp().run()