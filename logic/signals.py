from forms.game_screen import GameScreen


def open_game_screen(old_window):
    old_window.close()
    window = GameScreen()
    window.show()



signals = {
    'open_game_screen': open_game_screen
}