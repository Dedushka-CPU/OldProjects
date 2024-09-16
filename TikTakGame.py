from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color

class TicTacToeGame(BoxLayout):
    def __init__(self, **kwargs):
        super(TicTacToeGame, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10 

        self.grid = GridLayout(cols=3, rows=3, size_hint=(1, 1))
        self.add_widget(self.grid)

        self.game = ['_' for _ in range(9)]
        self.turn = 'X'
        self.game_over = False
        self.winner = None

        self.draw_board()

    def draw_board(self):
        self.grid.clear_widgets()
        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                button = Button(
                    text=self.game[index],
                    font_size=40,
                    background_color=(1, 1, 1, 1),
                    on_release=lambda btn, idx=index: self.on_button_click(btn, idx)
                )
                self.grid.add_widget(button)

    def on_button_click(self, button, index):
        if not self.game_over:
            if self.game[index] == '_':
                self.game[index] = self.turn
                button.text = self.turn

                self.turn = 'O' if self.turn == 'X' else 'X'

                self.check_winner()
                if self.winner:
                    self.game_over = True
                    self.show_result_popup()

    def check_winner(self):
        for i in range(3):
            if self.game[i] == self.game[i + 3] == self.game[i + 6] != '_':
                self.winner = self.game[i]
                return

            if self.game[i * 3] == self.game[i * 3 + 1] == self.game[i * 3 + 2] != '_':
                self.winner = self.game[i * 3]
                return

        if self.game[0] == self.game[4] == self.game[8] != '_':
            self.winner = self.game[0]
            return

        if self.game[2] == self.game[4] == self.game[6] != '_':
            self.winner = self.game[2]
            return

        if '_' not in self.game:
            self.winner = 'Draw'

    def show_result_popup(self):
        content = BoxLayout(orientation='vertical')
        if self.winner == 'Draw':
            content.add_widget(Label(text="Ничья!"))
        else:
            content.add_widget(Label(text=f'Игрок {self.winner} победил!'))

        popup = Popup(title='Игра окончена', content=content, size_hint=(None, None), size=(400, 200))
        popup.bind(on_dismiss=self.reset_game)
        popup.open()

    def reset_game(self, instance):
        self.game = ['_' for _ in range(9)]
        self.turn = 'X'
        self.game_over = False
        self.winner = None
        self.draw_board()

class TicTacToeApp(App):
    def build(self):
        return TicTacToeGame()

if __name__ == '__main__':
    TicTacToeApp().run()
