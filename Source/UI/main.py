from imports import *

class MainWindow(Widget):
	

class NoteApp(App):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    NoteApp().run()