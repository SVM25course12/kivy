from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
import os


class Window1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "main"
        self.setUpMainWindow()

    def setUpMainWindow(self):
        layout = FloatLayout()


        hello_label = Label(
            text="Здравствуйте!",
            font_size=20,
            size_hint=(None, None),
            size=(300, 50),
            pos=(100, 450)
        )
        layout.add_widget(hello_label)


        switch_button = Button(
            text="Перейти в профиль",
            font_size=14,
            size_hint=(None, None),
            size=(150, 50),
            pos=(175, 400)
        )
        switch_button.bind(on_press=self.switch_to_profile)
        layout.add_widget(switch_button)


        image_path = r"pht\317.jpg"
        try:
            if os.path.exists(image_path):
                world_image = Image(
                    source=image_path,
                    size_hint=(None, None),
                    size=(490, 380),
                    pos=(5, 0)
                )
                layout.add_widget(world_image)
            else:
                print(f"Image not found: {image_path}")

                error_label = Label(
                    text="Изображение не найдено",
                    pos=(150, 200)
                )
                layout.add_widget(error_label)
        except Exception as error:
            print(f"Error loading image: {error}")
            error_label = Label(
                text="Ошибка загрузки изображения",
                pos=(150, 200)
            )
            layout.add_widget(error_label)

        self.add_widget(layout)

    def switch_to_profile(self, instance):
        self.manager.current = "second"


class Window2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "second"
        self.setUpMainWindow()

    def setUpMainWindow(self):

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)


        back_button = Button(
            text="Назад",
            size_hint=(None,None),
            size=(100, 50),
            pos=(175, 400)
        )
        back_button.bind(on_press=self.switch_to_main)


        float_layout = FloatLayout()
        float_layout.add_widget(back_button)

        image_path = r"pht\3820.jpg"
        try:
            if os.path.exists(image_path):
                profile_image = Image(
                    source=image_path,
                    size_hint=(1, None),
                    height=900,
                    allow_stretch=True
                )
                float_layout.add_widget(profile_image)
            else:
                print(f"Файл {image_path} не найден")
                error_label = Label(text="Изображение профиля не найдено")
                float_layout.add_widget(error_label)
        except Exception as e:
            print(f"Ошибка при загрузке изображения {image_path}: {e}")
            error_label = Label(text="Ошибка загрузки изображения")
            float_layout.add_widget(error_label)
        main_layout.add_widget(float_layout)
        info_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        bio_label = Label(
            text="Мовсесян Тигран",
            font_size=16,
            size_hint_y=None,
            height=30,
            text_size=(380, None),
            halign='left'
        )
        info_layout.add_widget(bio_label)

        teach_label = Label(
            text="Обучаюсь в МАИ на 2 курсе 317 кафедры управление инновациями",
            font_size=16,
            size_hint_y=None,
            height=60,
            text_size=(380, None),
            halign='left'
        )
        info_layout.add_widget(teach_label)

        skills_label = Label(
            text="Скиллы: программирование, владение инностранными языками ",
            font_size=16,
            size_hint_y=None,
            height=30,
            text_size=(380, None),
            halign='left'
        )
        info_layout.add_widget(skills_label)

        main_layout.add_widget(info_layout)
        self.add_widget(main_layout)

    def switch_to_main(self, instance):
        self.manager.current = "main"


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        main_screen = Window1()
        second_screen = Window2()
        sm.add_widget(main_screen)
        sm.add_widget(second_screen)
        sm.current = "main"
        return sm

if __name__ == "__main__":
    Window.size = (400, 500)
    MyApp().run()
