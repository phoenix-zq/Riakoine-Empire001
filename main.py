from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.button import Button
import json, os

class RiakoineUniversal(App):
    def build(self):
        # High-Contrast Empire Theme (Black and Gold)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.header = Label(text="RIAKOINE UNIVERSAL V3.1", font_size='28sp', bold=True, color=(1, 0.8, 0, 1))
        
        # Language Selector
        available_files = [f.replace('.json', '').capitalize() for f in os.listdir('languages') if f.endswith('.json')]
        self.lang_spinner = Spinner(text='Select Language', values=available_files, size_hint=(1, 0.2))
        
        # Accessibility Toggle
        self.high_contrast_btn = Button(text="Toggle High Contrast", size_hint_y=0.1)
        self.high_contrast_btn.bind(on_press=self.toggle_contrast)

        self.display = Label(text="Awaiting Selection...", halign='center', color=(1, 1, 1, 1))
        
        self.layout.add_widget(self.header)
        self.layout.add_widget(self.lang_spinner)
        self.layout.add_widget(self.high_contrast_btn)
        self.layout.add_widget(self.display)
        
        self.lang_spinner.bind(text=self.load_language)
        return self.layout

    def toggle_contrast(self, instance):
        # Switch between High Contrast (Yellow on Black) and Standard
        if self.display.color == [1, 1, 1, 1]:
            self.display.color = [1, 1, 0, 1] # High Contrast Yellow
            self.display.font_size = '32sp'   # Larger text
        else:
            self.display.color = [1, 1, 1, 1]
            self.display.font_size = '20sp'

    def load_language(self, spinner, text):
        try:
            with open(f"languages/{text.lower()}.json", 'r') as f:
                data = json.load(f)
                self.display.text = data['text']
        except:
            self.display.text = "Error loading Repo."

if __name__ == '__main__':
    RiakoineUniversal().run()
