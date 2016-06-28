from kivy.app import App
from kivy.uix.widget import Widget


class HelloWorld(Widget):
    pass

class HelloWorldApp(App):
    def build(self):
        return HelloWorld()

if __name__=='__main__':
    HelloWorldApp().run()
