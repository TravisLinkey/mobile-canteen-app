from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

from kivy.lang import Builder
Builder.load_file("main.kv")

from menu_prices import PRICES

class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class FourthScreen(Screen):
    pass


class MyScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.running_total = 0

    def switch_screen(self, screen_name='_home_screen_'):
        if screen_name == '_screen_one_': self.current = screen_name
        elif screen_name == '_screen_two_': self.current = screen_name
        elif screen_name == '_screen_three_': self.current = '_third_screen_'
        elif screen_name == '_screen_four_': self.current = '_fourth_screen_'
        elif screen_name == '_screen_five_': self.current = '_fifth_screen_'

    def add_to_total(self, button_name):
        ''' method to add the button 
            price to the running total
        '''

        print(f'Adding button price to total \n')

        # get the button price
        button_price = self.lookup_button_price(button_name)

        print(f'Adding {button_price} to the Total! \n')

        # add the button price to the running total
        self.running_total += button_price

        self.ids.running_total.text = '$ ' + str(self.running_total)

    def lookup_button_price(self, button_name):
        return PRICES[button_name]


class MobileCanteenApp(App):

    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    MobileCanteenApp().run()
