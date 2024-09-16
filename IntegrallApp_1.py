from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
import math

class IntegralCalculator(GridLayout):
    def __init__(self, **kwargs):
        super(IntegralCalculator, self).__init__(**kwargs)
        
        self.result_label = Label(text='',  size_hint_x=None)
        self.add_widget(self.result_label)
        self.function_input = TextInput(multiline=False, size_hint_x=3)
        self.add_widget(self.function_input)
        self.cols = 2
        self.add_widget(Label(text='Введите значение alpha:', height='40dp', size_hint_x=1))
        self.alpha_input = TextInput(multiline=False, size_hint_x=1, height='40dp')
        self.add_widget(self.alpha_input)

        self.add_widget(Label(text='Введите значение a:', height='40dp', size_hint_x=1))
        self.a_input = TextInput(multiline=False, size_hint_x=1, height='40dp')
        self.add_widget(self.a_input)
        self.add_widget(Label(text='Список доступных функций:',  height='20dp', size_hint_x=1))


        self.function_dropdown = DropDown()

        math_functions = [
            "math.sin(x)",
            "math.cos(x)",
            "math.tan(x)",
            "math.exp(x)",
            "math.log(x)",
            "math.sqrt(x)",
            "math.pow(x, y)",
            "x",
        ]

        for func in math_functions:
            btn = Button(text=func, size_hint_y=None, height=50, width=50)
            btn.bind(on_release=lambda btn: self.select_function(btn.text))
            self.function_dropdown.add_widget(btn)

        self.function_button = Button(text='Выбрать функцию', size_hint=(None, None), height='40dp', width=50)
        self.function_button.bind(on_release=self.function_dropdown.open)
        self.add_widget(self.function_button)

        self.zero = Button(text='0', size_hint_y=None, height=50, width=50)
        self.zero.bind(on_press=lambda instance: self.add_operator('0'))
        self.add_widget(self.zero)

        self.one = Button(text='1', size_hint_y=None, height=50, width=50)
        self.one.bind(on_press=lambda instance: self.add_operator('1'))
        self.add_widget(self.one)

        self.two = Button(text='2', size_hint_y=None, height=50, width=50)
        self.two.bind(on_press=lambda instance: self.add_operator('2'))
        self.add_widget(self.two)

        self.three = Button(text='3', size_hint_y=None, height=50, width=50)
        self.three.bind(on_press=lambda instance: self.add_operator('3'))
        self.add_widget(self.three)

        self.four = Button(text='4', size_hint_y=None, height=50, width=50)
        self.four.bind(on_press=lambda instance: self.add_operator('4'))
        self.add_widget(self.four)

        self.five = Button(text='5', size_hint_y=None, height=50, width=50)
        self.five.bind(on_press=lambda instance: self.add_operator('5'))
        self.add_widget(self.five)

        self.six = Button(text='6', size_hint_y=None, height=50, width=50)
        self.six.bind(on_press=lambda instance: self.add_operator('6'))
        self.add_widget(self.six)

        self.seven = Button(text='7', size_hint_y=None, height=50, width=50)
        self.seven.bind(on_press=lambda instance: self.add_operator('6'))
        self.add_widget(self.seven)

        self.eate = Button(text='8', size_hint_y=None, height=50, width=50)
        self.eate.bind(on_press=lambda instance: self.add_operator('6'))
        self.add_widget(self.eate)

        self.night = Button(text='9', size_hint_y=None, height=50, width=50)
        self.night.bind(on_press=lambda instance: self.add_operator('6'))
        self.add_widget(self.night)

        self.addition_button = Button(text='+', size_hint_y=None, height=50, width=50)
        self.addition_button.bind(on_press=lambda instance: self.add_operator('+'))
        self.add_widget(self.addition_button)

        self.subtraction_button = Button(text='-', size_hint_y=None, height=50, width=50)
        self.subtraction_button.bind(on_press=lambda instance: self.add_operator('-'))
        self.add_widget(self.subtraction_button)

        self.multiplication_button = Button(text='*', size_hint_y=None, height=50, width=50)
        self.multiplication_button.bind(on_press=lambda instance: self.add_operator('*'))
        self.add_widget(self.multiplication_button)

        self.division_button = Button(text='/', size_hint_y=None, height=50, width=50)
        self.division_button.bind(on_press=lambda instance: self.add_operator('/'))
        self.add_widget(self.division_button)

        self.delete_button = Button(text='Удалить', size_hint_y=None, height=50, width=50)
        self.delete_button.bind(on_press=self.delete_element)
        self.add_widget(self.delete_button)

        self.calculate_button = Button(text='Вычислить', size_hint_y=None, height=50, width=50)
        self.calculate_button.bind(on_press=self.calculate_integral)
        self.add_widget(self.calculate_button)

        

    def select_function(self, selected_function):
        current_text = self.function_input.text

        new_text = current_text + " " + selected_function

        self.function_input.text = new_text

    def add_operator(self, operator):
        current_text = self.function_input.text

        new_text = current_text + "" + operator

        self.function_input.text = new_text

    def delete_element(self, instance):
        current_text = self.function_input.text

        new_text = ' '.join(current_text.split()[:-1])

        self.function_input.text = new_text

    def f(self, x, function_str):
        allowed_vars = {'x': x}
        try:
            return eval(function_str, globals(), allowed_vars)
        except Exception as e:
            print(f"Ошибка в выражении: {e}")
            return None

    def g(self, x, h, function_str):
        f_x = self.f(x, function_str)
        if f_x is None:
            return None
        return (h) * (f_x + 3 * self.f(x + h/3.0, function_str) +
                      3 * self.f(x + 2.0*h/3.0, function_str) + self.f(h + x, function_str)) / 8


    def integral(self, a, alpha, eps, function_str):
        if self.f(a, function_str) is None:
            print("Функция не существует")
            return None
        y = 0
        x = a
        h = 0.1
        sum_val = 0
        sum_delta = 0
        sum_delta_abs = 0
        n = 0
        while sum_val < alpha - eps:
            I1 = self.g(x, h, function_str)
            I2 = self.g(x, h/2, function_str) + self.g(x + h/2, h/2, function_str)
            delta = (I2 - I1) / 15
            delta_fabs = abs(delta)
            chi = (delta_fabs / eps) ** 0.2
            chi = min(max(chi, 0.1), 10)
            hnew = 0.95 * h / chi
            if delta_fabs < eps:
                if sum_val + I2 > alpha + eps:
                    hnew = h * (alpha - sum_val) / I2
                    y += 1
                else:
                    x += h
                    sum_val += I2
                    sum_delta += delta
                    sum_delta_abs += delta_fabs
                    n += 1
            h = hnew
        xmin = (alpha - sum_val - sum_delta_abs) / self.f(x, function_str)
        xmax = (alpha - sum_val + sum_delta_abs) / self.f(x, function_str)
        return x, sum_delta, sum_delta_abs, n, xmin, xmax

    def calculate_integral(self, instance):
        try:
            alpha = float(self.alpha_input.text)
            a = float(self.a_input.text)
            function_str = self.function_input.text
            eps = 1e-7
            x, sum_delta, sum_delta_abs, n, xmin, xmax = self.integral(a, alpha, eps, function_str)
            if None in (x, sum_delta, sum_delta_abs, n, xmin, xmax):
                self.result_label.text = "Ошибка: Проверьте правильность ввода функции"
            else:
                result_text = (
                    f"x = {x}\n"
                    f"Шаги = {n}\n"
                    f"Среднев. погрешность = {abs(sum_delta)}\n"
                    f"Гарант. погрешность = {sum_delta_abs}\n"
                    f"min of x = {xmin}\n"
                    f"max of x = {xmax}"
                )
                self.result_label.text = result_text
        except ValueError:
            self.result_label.text = "Ошибка: Введите числовые значения для alpha и a"

class IntegralApp(App):
    def build(self):
        return IntegralCalculator()

if __name__ == '__main__':
    IntegralApp().run()
