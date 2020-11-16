from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest
import time


class MyLayout(BoxLayout):

    def Deter(self):
        phone = str(self.inp_txt.text)
        getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone + ".json"
        try:
            infoPhone = UrlRequest(getInfo, verify=False)
            infoPhone.wait()
        except:
            self.label_w.text = "- Phone not found -"
        infoPhone = infoPhone.result
        self.label_w.text = "Страна:   " + str(infoPhone['country']["name"])
        self.label_w1.text = "Регион:  " + str(infoPhone["region"]["name"])
        self.label_w2.text = "Округ:   " + str(infoPhone["region"]["okrug"])
        self.label_w3.text = "Оператор:    " + str(infoPhone["0"]["oper"])


class App(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    App().run()
