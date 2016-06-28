import kivy

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class SimnpleMathApp(App):

    lblResult = Label(text='0.0', font_size='100pt')
    txtInp1 = TextInput()
    txtinp2 = TextInput()

    def add(self, event):
        res = float(self.txtInp1.text) + float(self.txtinp2.text)
        self.lblResult.text = str(res)

    def build(self):

        self.txtInp1.text = '0.0'

        self.txtinp2.text = '0.0'

        btnAdd = Button(text="Add")
        btnAdd.bind(on_press=self.add)
        lytMath = BoxLayout(size_hint=(1, None), height=50)
        lytMath.add_widget(self.txtInp1)
        lytMath.add_widget(self.txtinp2)
        lytMath.add_widget(btnAdd)

        root = BoxLayout(orientation='vertical')
        root.add_widget(self.lblResult)
        root.add_widget(lytMath)

        return root


if __name__=="__main__":
    SimnpleMathApp().run()

