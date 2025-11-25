import random
import utils
import gui
import tkinter

class GuessTheNumberGame:
    def __init__(self, range_min=1, range_max=100):
        self.range_min = range_min
        self.range_max = range_max
        self.secret_number = None
        self.attempts = 0
        self.game_over = False
        self.start_new_game()

    def start_new_game(self):
        self.secret_number = random.randint(self.range_min, self.range_max)
        self.attempts = 0
        self.game_over = False
        # print(f"Новая игра! Загадано число от {self.range_min} до {self.range_max}.")

    def make_guess(self, guess):
        if self.game_over:
            return "Игра окончена. Начните новую игру."

        self.attempts += 1
        
        return utils.get_hint_message(self.secret_number, guess) + " Сделано попыток: " + str(self.attempts)


def test_game_initial_state():
    game = GuessTheNumberGame(1, 10)
    assert 1 <= game.secret_number <= 10
    assert game.attempts == 0
    assert game.game_over is False

def test_make_guess_increments_attempts():
    game = GuessTheNumberGame(1, 10)
    game.secret_number = 5
    game.make_guess(3)
    assert game.attempts == 1
    game.make_guess(7)
    assert game.attempts == 2

def test_make_guess_game_over():
    game = GuessTheNumberGame()
    game.secret_number = 10
    game.game_over = True
    result = game.make_guess(10)
    assert result == "Игра окончена. Начните новую игру."

def test_start_new_game_resets_attempts():
    game = GuessTheNumberGame()
    game.attempts = 5
    game.start_new_game()
    assert game.attempts == 0
    assert 1 <= game.secret_number <= 100

if __name__ == "__main__":
    test_game_initial_state()
    test_make_guess_increments_attempts()
    test_make_guess_game_over()
    test_start_new_game_resets_attempts()
    root = tkinter.Tk()
    gui = gui.GameGUI(root)
    root.mainloop()