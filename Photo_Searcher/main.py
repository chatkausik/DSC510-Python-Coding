from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def search_image(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        print(query)
        # Get wikipedia link and first image
        page = wikipedia.page(query, auto_suggest=False, redirect=True, preload=False)
        link = page.images[0]
        return link

    def download_image(self):
        # Download the image
        headers = {'User-agent': 'Safari/15.5'}
        req = requests.get(self.search_image(), headers=headers)
        imagepath = 'files/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        return imagepath

    def set_image(self):
        # Set the image in the Image widget
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()