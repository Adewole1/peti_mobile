import os
from datetime import datetime
from kivy.app import App
from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window
from kivy.core.text import LabelBase

from kivy.uix.screenmanager import (Screen, ScreenManager,
                                    NoTransition)
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.pickers import (MDTimePicker, MDDatePicker)
from kivymd.uix.behaviors import (RectangularElevationBehavior,
                                  RoundedRectangularElevationBehavior,
                                  FakeRectangularElevationBehavior)
from kivymd.uix.card import MDCard
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.widget import MDWidget
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock


# Window.size = (360,640)
# Window.top = 30
# Window.left = 5

# KIVY_DPI=409

# Window.softinput_mode = 'pan'
Window.softinput_mode = 'below_target'

colors = {
    'Blue': {
        '50': '93AADC',
        '100': '849ED7',
        '200': '7492D2',
        '300': '6586CD',
        '400': '567AC8',
        '500': '466EC3',
        '600': '3B61B5',
        '700': '3457A2',
        '800': '2E4D8E',
        '900': '28427B',
        'A100': '849ED7',
        'A200': '7492D2',
        'A400': '567AC8',
        'A700': '3457A2',
    },
    "Red": {
        "50": "FFEBEE",
        "100": "FFCDD2",
        "200": "EF9A9A",
        "300": "E57373",
        "400": "EF5350",
        "500": "F44336",
        "600": "E53935",
        "700": "D32F2F",
        "800": "C62828",
        "900": "B71C1C",
        "A100": "FF8A80",
        "A200": "FF5252",
        "A400": "FF1744",
        "A700": "D50000",
    },
    "Light": {
        "StatusBar": "E0E0E0",
        "AppBar": "F5F5F5",
        "Background": "FAFAFA",
        "CardsDialogs": "FFFFFF",
        "FlatButtonDown": "cccccc",
    },
    "Dark": {
        "StatusBar": "000000",
        "AppBar": "212121",
        "Background": "303030",
        "CardsDialogs": "424242",
        "FlatButtonDown": "999999",
    }
}


class MD3BottomNavigation(MDBottomNavigation, FakeRectangularElevationBehavior):
    text = StringProperty()


class MD3FloatLayout(MDFloatLayout, FakeRectangularElevationBehavior):
    pass


class MD3Card(MDCard, RoundedRectangularElevationBehavior):
    '''Implements a material design v3 card.'''

    text = StringProperty()


class WelcomeScreen(MDScreen):
    pass


class LoginScreen(Screen):

    def signup(self):
        self.manager.current = 'signup'

    def check(self):
        ids = self.ids
        if self.ids.password.text == '':
            self.ids.password.error = True
        if self.ids.email.text == '':
            self.ids.email.error = True
        if ids.password.text != '' and ids.email.text != '':
            self.manager.current = 'home-login'
                
    # pass


class SignupScreen(Screen):

    def login(self):
        self.manager.current = 'login'

    def signup_check(self):
        ids = self.ids
        if ids.signup_name.text == '':
            ids.signup_name.error = True
        if ids.signup_email.text == '':
            ids.signup_email.error = True
        if ids.signup_password.text == '':
            ids.signup_password.error = True
        if ids.signup_phone.text == '':
            ids.signup_phone.error = True
        if ids.signup_password.text != '' and ids.signup_email.text != '' and ids.signup_name != '' and ids.signup_phone != '':
            self.manager.current = 'introduction'                

    # pass


class HomeSignupScreen(Screen):

    def on_enter(self, *args):
        Clock.schedule_interval(self.ids.carousel.load_next, 8)

    def carousel_changed(self):

        if self.ids.carousel.index == 0:
            self.ids.circle1.icon_color = 240 / 255, 101 / 255, 67 / 255, 1
            self.ids.circle2.icon_color = 1, 1, 1, 1
            self.ids.circle3.icon_color = 1, 1, 1, 1

        elif self.ids.carousel.index == 1:
            self.ids.circle2.icon_color = 240 / 255, 101 / 255, 67 / 255, 1
            self.ids.circle1.icon_color = 1, 1, 1, 1
            self.ids.circle3.icon_color = 1, 1, 1, 1

        elif self.ids.carousel.index == 2:
            self.ids.circle3.icon_color = 240 / 255, 101 / 255, 67 / 255, 1
            self.ids.circle1.icon_color = 1, 1, 1, 1
            self.ids.circle2.icon_color = 1, 1, 1, 1


class HomeLoginScreen(Screen):
    pass


class IconListItem(OneLineIconListItem):
    icon = StringProperty()


class IntroductionScreen(Screen):

    def __init__(self, **kw):
        super().__init__(**kw)

        menu_items = [
            {
                "viewclass": "IconListItem",
                "icon": "dog",
                "height": dp(56),
                "text": f"Dog",
                "on_release": lambda x=f"Dog": self.set_item(x),
            },
            {
                "viewclass": "IconListItem",
                "icon": "cat",
                "height": dp(56),
                "text": f"Cat",
                "on_release": lambda x=f"Cat": self.set_item(x),
            },
        ]
        self.type_menu = MDDropdownMenu(
            caller=self.ids.pet_type,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )

        self.breed_items = [
            {
                "viewclass": "IconListItem",
                # "icon": "cat",
                "height": dp(56),
                "text": f"Set pet type first",
            }
        ]

        self.breed_menu = MDDropdownMenu(
            caller=self.ids.pet_breed,
            items=self.breed_items,
            position='bottom',
            width_mult=4,
        )

    def set_item(self, breed):

        self.ids.pet_type.text = breed
        self.type_menu.dismiss()
        self.manager.current = 'introduction'
        if self.ids.pet_type.text == 'Dog':
            self.breed_items = [
                {
                    "viewclass": "IconListItem",
                    "icon": "dog",
                    "height": dp(56),
                    "text": f"Akita",
                    "on_release": lambda x=f"Akita": self.set_breed(x),
                },
                {
                    "viewclass": "IconListItem",
                    "icon": "dog",
                    "height": dp(56),
                    "text": f"Azawakh",
                    "on_release": lambda x=f"Azawakh": self.set_breed(x),
                },
                {
                    "viewclass": "IconListItem",
                    "icon": "dog",
                    "height": dp(56),
                    "text": f"Beabull",
                    "on_release": lambda x=f"Beabull": self.set_breed(x),
                },
                {
                    "viewclass": "IconListItem",
                    "icon": "dog",
                    "height": dp(56),
                    "text": f"Boerboel",
                    "on_release": lambda x=f"Boerboel": self.set_breed(x),
                },
                {
                    "viewclass": "IconListItem",
                    "icon": "dog",
                    "height": dp(56),
                    "text": f"Caucasian",
                    "on_release": lambda x=f"Caucasian": self.set_breed(x),
                },
            ]
        elif self.ids.pet_type.text == 'Cat':
            self.breed_items = [
                {
                    "viewclass": "IconListItem",
                    "icon": "cat",
                    "height": dp(56),
                    "text": f"Persian cat",
                    "on_release": lambda x=f"Persian cat": self.set_breed(x),
                },
                {
                    "viewclass": "IconListItem",
                    "icon": "cat",
                    "height": dp(56),
                    "text": f"Ragdoll",
                    "on_release": lambda x=f"Ragdoll": self.set_breed(x),
                },
                {
                    "viewclass": "IconListItem",
                    "icon": "cat",
                    "height": dp(56),
                    "text": f"Munchkin Cat",
                    "on_release": lambda x=f"Munchkin Cat": self.set_breed(x),
                },
                {
                    "viewclass": "IconListItem",
                    "icon": "cat",
                    "height": dp(56),
                    "text": f"Maine coon",
                    "on_release": lambda x=f"Maine coon": self.set_breed(x),
                },
            ]
        else:
            self.breed_items = []

        self.breed_menu = MDDropdownMenu(
            caller=self.ids.pet_breed,
            items=self.breed_items,
            position='bottom',
            width_mult=4,
        )

    def set_breed(self, breed):
        self.ids.pet_breed.text = breed
        self.breed_menu.dismiss()

    def time_picker(self):
        self.time_dialog = MDTimePicker()
        self.time_dialog.set_time(datetime.now().time())
        self.time_dialog.bind(time=self.get_time)
        self.time_dialog.open()

    def get_time(self, instance, time):
        self.ids.pet_feed.text = str(time)
        # return time

    def introduction_check(self):
        if self.ids.pet_name.text == '':
            self.ids.pet_name.error = True
        if self.ids.pet_type.text == '':
            self.ids.pet_type.error = True
        if self.ids.pet_breed.text == '':
            self.ids.pet_breed.error = True
        if (
                self.ids.pet_name.text != '' and self.ids.pet_type.text != '' and self.ids.pet_name.text != ''
        ):
            self.manager.current = 'home-signup'



class ProfilesScreen(Screen):
    pass


class ChatsScreen(Screen):
    pass


class BookingsScreen(Screen):
    dialog = None                

    def date_picker(self):
        date_dialog = MDDatePicker(
            mode='range',
            helper_text='Wrong date range',
            radius=[dp(28), dp(28), dp(28), dp(28)],
            title='Select date of drop off and pick up',
            text_current_color=[70 / 255, 110 / 255, 195 / 255, 1],
            min_date=datetime.now().date(),
        )
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        self.ids.drop_off_date.text = str(date_range[0]) + ' - ' + str(date_range[1])

    def on_cancel(self, instance, value):
        pass
        # pass

    def time_picker(self):
        self.time_dialog = MDTimePicker()
        self.time_dialog.set_time(datetime.now().time())
        self.time_dialog.bind(time=self.get_time)
        self.time_dialog.open()

    def get_time(self, instance, time):
        self.ids.drop_off_time.text = str(time)

    def cash_payment(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Pay the sum of ₦2500 to Kennedy Leonard on drop off.",
                title="Payment pending",
                type='simple',
                radius=[dp(20), dp(7), dp(20), dp(7)],
                buttons=[
                    MDFlatButton(
                        text="GO TO HOME",
                        theme_text_color="Custom",
                        text_color=[70 / 255, 110 / 255, 195 / 255, 1],
                        on_release=self.switch_screen
                    ),
                ],
            )
        self.dialog.open()

    def switch_screen(self, instance):
        self.manager.current = 'home-login'
        self.dialog.dismiss()

    def switch_profiles(self, instance):
        self.manager.current = 'profiles'


class CardPaymentScreen(Screen):
    dialog = None                

    def card_paid(self):
        ids = self.ids
        if ids.card_number.text == '':
            ids.card_number.error = True
        if ids.expiry_date.text == '':
            ids.expiry_date.error = True
        if ids.cvv.text == '':
            ids.cvv.error = True
        if ids.card_number.text != '' and ids.expiry_date.text != '' and ids.cvv != '':
            if not self.dialog:
                self.dialog = MDDialog(
                    text="Booking successful!",
                    title="Payment successful",
                    type='simple',
                    radius=[dp(20), dp(7), dp(20), dp(7)],
                    buttons=[
                        MDFlatButton(
                            text="GO TO HOME",
                            theme_text_color="Custom",
                            text_color=[70 / 255, 110 / 255, 195 / 255, 1],
                            on_release=self.switch_screen
                        ),
                    ],
                )
            self.dialog.open()

    def switch_screen(self, instance):
        self.manager.current = 'home-login'
        self.dialog.dismiss()

    def switch_book(self, instance):
        self.manager.current = 'bookings'


class PetiApp(MDApp):

    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = 'Blue'
        hour = datetime.now().hour
        # if hour >= 19 and hour <= 7:
        #     self.theme_cls.theme_style = 'Dark'
        # else:
        #     self.theme_cls.theme_style = 'Light'
        self.theme_cls.theme_style = 'Light'
        manager = ScreenManager(transition=NoTransition())
        manager.add_widget(WelcomeScreen(name='welcome'))
        manager.add_widget(LoginScreen(name='login'))
        manager.add_widget(SignupScreen(name='signup'))
        manager.add_widget(HomeSignupScreen(name='home-signup'))
        manager.add_widget(HomeLoginScreen(name='home-login'))
        manager.add_widget(IntroductionScreen(name='introduction'))
        manager.add_widget(ProfilesScreen(name='profiles'))
        manager.add_widget(ChatsScreen(name='chats'))
        manager.add_widget(BookingsScreen(name='bookings'))
        manager.add_widget(CardPaymentScreen(name='card-payment'))
        # manager.current = 'home-signup'
        return manager

LabelBase.register(name='Proxima', 
                   fn_regular = 'assets/fonts/Demo_Fonts/regular.otf',
                   fn_bold = 'assets/fonts/Demo_Fonts/bold.otf',)

if __name__ == '__main__':
    PetiApp().run()
