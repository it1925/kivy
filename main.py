from kivy.config import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from menu.menu import MenuScreen
from translator.translator import TranslatorScreen

class MyApp(App):
    def build(self):
        # return Label(text="CISCO")
        Config.set('graphics', 'resizable', '1')
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="menu"))
        sm.add_widget(TranslatorScreen(name="translator"))
        return sm


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MyApp().run()
