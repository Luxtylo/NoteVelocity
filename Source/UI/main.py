from imports import *

class PushButton(Image):
	wimg = Image(source='TestButtons/TestButton1.png')

class MainWindow(Widget):
	dude = ObjectProperty(None)

class NoteApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    NoteApp().run()