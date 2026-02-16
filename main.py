from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Professional Empire Theme
Window.clearcolor = (0.02, 0.02, 0.02, 1)

class SentinelLock(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        layout.add_widget(Label(text="[b]SENTINEL GATEKEEPER[/b]", markup=True, font_size='30sp'))
        layout.add_widget(Label(text="Enter Empire Access Key", color=(0.7, 0.7, 0.7, 1)))

        self.key_input = TextInput(password=True, multiline=False, size_hint=(1, 0.2), halign='center', font_size='24sp')
        layout.add_widget(self.key_input)

        btn = Button(text="AUTHENTICATE", background_color=(0, 0.5, 0, 1), size_hint=(1, 0.3))
        btn.bind(on_press=self.check_key)
        layout.add_widget(btn)

        self.error_label = Label(text="", color=(1, 0, 0, 1))
        layout.add_widget(self.error_label)
        self.add_widget(layout)

    def check_key(self, instance):
        # Your buddies' access key
        if self.key_input.text == "Empire2026":
            self.manager.current = 'dashboard'
        else:
            self.error_label.text = "Access Denied: Invalid Key"

class WellnessDashboard(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)

        layout.add_widget(Label(text="[b]WELLNESS DASHBOARD[/b]", markup=True, font_size='24sp'))

        # Accessibility Buttons (Large and Clear)
        layout.add_widget(Button(text="EMERGENCY SOS", background_color=(0.8, 0, 0, 1), font_size='20sp'))
        layout.add_widget(Button(text="TRANSLATE MESSAGE", background_color=(0, 0.3, 0.7, 1)))
        layout.add_widget(Button(text="HEALTH MONITOR", background_color=(0.2, 0.2, 0.2, 1)))
        layout.add_widget(Button(text="IOT HOME CONTROL", background_color=(0.2, 0.2, 0.2, 1)))

        layout.add_widget(Label(text="System Status: Encrypted & Secure", font_size='12sp', color=(0.5, 0.5, 0.5, 1)))
        self.add_widget(layout)

class RiakoineGuardian(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SentinelLock(name='lock'))
        sm.add_widget(WellnessDashboard(name='dashboard'))
        return sm

if __name__ == "__main__":
    RiakoineGuardian().run()
