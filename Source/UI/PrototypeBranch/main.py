"""Initial testing of Kivy for note-taking program UI"""

## Imports
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class layout(Widget):
	# Make float layout
	layout = FloatLayout(size=(800,500))

	# Button
	button = Button(
		text = "Testing",
		size = (41,21),
		pos = (20,20))

	layout.add_widget(button)

## Main class
class NoteApp(App):

	# Build method returns layout
	def build(self):
		return layout

if __name__ == '__main__':
    NoteApp().run()