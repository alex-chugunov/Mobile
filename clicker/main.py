from kivy.app import App
from kivy.uix.boxlayout import BoxLayout



class MyLayout(BoxLayout):

    def Win1(self):
        self.b1_w.text = ">  —  <"
        self.b1_w.background_color = 1,0,1,1
        self.b2_w.text = ":("
        self.b2_w.background_color = 255, 0, 0, 255

    def Win2(self):
        self.b2_w.text = ">  +  <"
        self.b2_w.background_color = 1,0,1,1
        self.b1_w.text = ":("
        self.b1_w.background_color = 0, 0, 255, 255

    def Clean(self):
        self.b2_w.text = "  +  "
        self.b1_w.background_color = 0,0,255,255
        self.b1_w.text = "  —  "
        self.b2_w.background_color = 255,0,0,255


class TutorialApp(App):
    def build(self):
        return MyLayout()


TutorialApp().run()