from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import ScreenManager, Screen

class MyScreenManager(ScreenManager):
    pass

class FirstScreen(Screen):
    def calculate(self, lvl, attack, power, effectiveness, stab, defense):
        lvl = int(lvl) if lvl else 1
        attack = int(attack) if attack else 1
        power = int(power) if power else 1
        effectiveness = float(effectiveness) if effectiveness else 1
        stab = float(stab) if stab else 1
        defense = int(defense) if defense else 1

        damageMin = (((2 * lvl + 10) / 250) * (attack / defense) * power + 2) * stab * effectiveness * 0.85
        damageMax = (((2 * lvl + 10) / 250) * (attack / defense) * power + 2) * stab * effectiveness
        damageMinC = (((2 * lvl + 10) / 250) * (attack / defense) * power + 2) * stab * effectiveness * 0.85 * 1.5
        damageMaxC = (((2 * lvl + 10) / 250) * (attack / defense) * power + 2) * stab * effectiveness * 1.5

        self.damage_label.text = "Без крита:\nМин урон: {}\nМакс урон: {}\nС критом:\nМин урон: {}\nМакс урон: {}".format(
            damageMin, damageMax, damageMinC, damageMaxC)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        button_layout = BoxLayout(size_hint_y=None, height='40dp')
        button1 = Button(text="Рассчет урона", size_hint_x=0.5, on_press=self.invalid_action)
        button2 = Button(text="Рассчет статов", size_hint_x=0.5, on_press=self.switch_to_second)
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        self.layout.add_widget(button_layout)

        lvl_layout = BoxLayout(size_hint_y=None, height='40dp')
        lvl_label = Label(text="Уровень:", size_hint_x=0.5)
        self.lvl_entry = TextInput(size_hint_x=0.5, height='40dp')
        lvl_layout.add_widget(lvl_label)
        lvl_layout.add_widget(self.lvl_entry)
        self.layout.add_widget(lvl_layout)

        attack_layout = BoxLayout(size_hint_y=None, height='40dp')
        attack_label = Label(text="Стат атаки:", size_hint_x=0.5)
        self.attack_entry = TextInput(size_hint_x=0.5, height='40dp')
        attack_layout.add_widget(attack_label)
        attack_layout.add_widget(self.attack_entry)
        self.layout.add_widget(attack_layout)

        # Layout for defense input
        defense_layout = BoxLayout(size_hint_y=None, height='40dp')
        defense_label = Label(text="Стат защиты:", size_hint_x=0.5)
        self.defense_entry = TextInput(size_hint_x=0.5, height='40dp')
        defense_layout.add_widget(defense_label)
        defense_layout.add_widget(self.defense_entry)
        self.layout.add_widget(defense_layout)

        power_layout = BoxLayout(size_hint_y=None, height='40dp')
        power_label = Label(text="Мощность атаки:", size_hint_x=0.5)
        self.power_entry = TextInput(size_hint_x=0.5, height='40dp')
        power_layout.add_widget(power_label)
        power_layout.add_widget(self.power_entry)
        self.layout.add_widget(power_layout)

        effectiveness_layout = BoxLayout(size_hint_y=None, height='40dp')
        effectiveness_label = Label(text="Эффективность атаки:", size_hint_x=0.5)
        self.effectiveness_combobox = Spinner(text='1', values=('0', '0.5', '1', '2', '4'), size_hint_x=0.5, height='40dp')
        effectiveness_layout.add_widget(effectiveness_label)
        effectiveness_layout.add_widget(self.effectiveness_combobox)
        self.layout.add_widget(effectiveness_layout)

        stab_layout = BoxLayout(size_hint_y=None, height='40dp')
        stab_label = Label(text="Стаб эффект:", size_hint_x=0.5)
        self.stab_combobox = Spinner(text='1', values=('1', '1.5', '2'), size_hint_x=0.5, height='40dp')
        stab_layout.add_widget(stab_label)
        stab_layout.add_widget(self.stab_combobox)
        self.layout.add_widget(stab_layout)
        submit_button = Button(text="Подтвердить", on_press=self.submit, size_hint_y=None, height='40dp')
        self.layout.add_widget(submit_button)

        self.damage_label = Label(text="Урон равен:", size_hint_y=None, height='40dp')
        self.layout.add_widget(self.damage_label)

        self.add_widget(self.layout)

    def switch_to_second(self, instance):
        if instance.text == "Рассчет статов":
            self.manager.current = 'second'

    def invalid_action(self, instance):
        self.damage_label.text = "Нельзя переходить на эту вкладку отсюда"

    def submit(self, instance):
        self.calculate(
            self.lvl_entry.text,
            self.attack_entry.text,
            self.power_entry.text,
            self.effectiveness_combobox.text,
            self.stab_combobox.text,
            self.defense_entry.text
        )

class SecondScreen(Screen):
    def calculate(self, lvl,base, gen,ev, stab,effectiveness):
        lvl = int(lvl) if lvl else 1
        base = int(base) if base else 1
        gen = int(gen) if gen else 1
        effectiveness = float(effectiveness) if effectiveness else 1
        stab = float(stab) if stab else 1
        ev = int(ev) if ev else 1

        stat=((base*2+gen+(ev/2)*(lvl/100)+5)*stab*effectiveness)

        self.damage_label.text = "Стат равен: {}\n".format(stat)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        button_layout = BoxLayout(size_hint_y=None, height='40dp')
        button1 = Button(text="Рассчет урона", size_hint_x=0.5, on_press=self.switch_to_first)
        button2 = Button(text="Рассчет статов", size_hint_x=0.5, on_press=self.invalid_action)
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        self.layout.add_widget(button_layout)

        lvl_layout = BoxLayout(size_hint_y=None, height='40dp')
        lvl_label = Label(text="Уровень:", size_hint_x=0.5)
        self.lvl_entry = TextInput(size_hint_x=0.5, height='40dp')
        lvl_layout.add_widget(lvl_label)
        lvl_layout.add_widget(self.lvl_entry)
        self.layout.add_widget(lvl_layout)

        base_layout = BoxLayout(size_hint_y=None, height='40dp')
        base_label = Label(text="Базовый стат:", size_hint_x=0.5)
        self.base_entry = TextInput(size_hint_x=0.5, height='40dp')
        base_layout.add_widget(base_label)
        base_layout.add_widget(self.base_entry)
        self.layout.add_widget(base_layout)

        gen_layout = BoxLayout(size_hint_y=None, height='40dp')
        gen_label = Label(text="Ген:", size_hint_x=0.5)
        self.gen_entry = TextInput(size_hint_x=0.5, height='40dp')
        gen_layout.add_widget(gen_label)
        gen_layout.add_widget(self.gen_entry)
        self.layout.add_widget(gen_layout)

        ev_layout = BoxLayout(size_hint_y=None, height='40dp')
        ev_label = Label(text="Кол-во ev:", size_hint_x=0.5)
        self.ev_entry = TextInput(size_hint_x=0.5, height='40dp')
        ev_layout.add_widget(ev_label)
        ev_layout.add_widget(self.ev_entry)
        self.layout.add_widget(ev_layout)

        stab_layout = BoxLayout(size_hint_y=None, height='40dp')
        stab_label = Label(text="Характер:", size_hint_x=0.5)
        self.stab_combobox = Spinner(text='1', values=('0.9', '1', '1.1'), size_hint_x=0.5, height='40dp')
        stab_layout.add_widget(stab_label)
        stab_layout.add_widget(self.stab_combobox)
        self.layout.add_widget(stab_layout)
        effectiveness_layout = BoxLayout(size_hint_y=None, height='40dp')
        effectiveness_label = Label(text="Уровень модификации:", size_hint_x=0.5)
        self.effectiveness_combobox = Spinner(text='1', values=('1', '1.09', '1.15', '1.22', '1.29','1.35','1.4'), size_hint_x=0.5, height='40dp')
        effectiveness_layout.add_widget(effectiveness_label)
        effectiveness_layout.add_widget(self.effectiveness_combobox)
        self.layout.add_widget(effectiveness_layout)

        submit_button = Button(text="Подтвердить", on_press=self.submit, size_hint_y=None, height='40dp')
        self.layout.add_widget(submit_button)

        self.damage_label = Label(text="Стат равен:", size_hint_y=None, height='40dp')
        self.layout.add_widget(self.damage_label)

    def switch_to_first(self, instance):
        if instance.text == "Рассчет урона":
            self.manager.current = 'first'

    def invalid_action(self, instance):
        self.damage_label.text = "Нельзя переходить на эту вкладку отсюда"

    def submit(self, instance):
        self.calculate(
            self.lvl_entry.text,
            self.base_entry.text,
            self.gen_entry.text,
            self.ev_entry.text,
            self.stab_combobox.text,
            self.effectiveness_combobox.text
        )

class MyScreenApp(App):
    def build(self):
        screen_manager = MyScreenManager()
        screen_manager.add_widget(FirstScreen(name='first'))
        screen_manager.add_widget(SecondScreen(name='second'))
        return screen_manager

if __name__ == '__main__':
    MyScreenApp().run()
