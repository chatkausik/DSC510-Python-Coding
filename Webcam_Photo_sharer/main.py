import webbrowser

from filestack import Client
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

import time

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filepath = f"files/{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filepath


class FileSharer:
    # Upload to cloud

    def __init__(self, filepath, api_key):
        self.api_key = api_key
        self.filepath = filepath

    def share_file(self):

        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url


class ImageScreen(Screen):
    link_var = "Create a Link first"
    def create_link(self):
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        print(file_path)
        filesharer = FileSharer(filepath=file_path, api_key='Aytwt7ujiTnmFnnNKvRWbz')
        self.url = filesharer.share_file()
        print(self.url)
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            print("copy")
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_var

    def open_link(self):
        try:
            print("opening link")
            webbrowser.open(self.url)
            print(f"{self.url} opening..")
        except:
            self.ids.link.text = self.link_var


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()

