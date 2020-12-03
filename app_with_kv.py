from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from menu_prices import PRICES

Builder.load_file("views/screen_one/screen_one.kv")
Builder.load_file("views/screen_two/screen_two.kv")
Builder.load_file("views/screen_three/screen_three.kv")
Builder.load_file("views/screen_four/screen_four.kv")

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()

    def snack_screen_selected(self):
        self.app.root.switch_screen('_first_screen_')

    def drinks_screen_selected(self):
        self.app.root.switch_screen('_second_screen_')
    
    def retail_screen_selected(self):
        self.app.root.switch_screen('_third_screen_')
    
    def food_screen_selected(self):
        self.app.root.switch_screen('_fourth_screen_')



    def receipt_screen_selected(self):
        self.app.root.switch_screen('_fifth_screen_')

    def add_to_total(self, button_name):
        self.app.root.add_to_total(button_name)
        self.ids.running_total.text = '$ ' + str(self.app.root.total)

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super(ThirdScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super(FourthScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()

class MyScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.total = 0

    def switch_screen(self, screen_name='_first_screen_'):
        self.current = screen_name

    def add_to_total(self, button_name):
        print(f'Adding : {PRICES[button_name]} to total! \n')
        self.total += PRICES[button_name]

class SwitchingScreenApp(App):

    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    SwitchingScreenApp().run()