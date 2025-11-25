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
        print(f"Новая игра! Загадано число от {self.range_min} до {self.range_max}.")

    def make_guess(self, guess):
        if self.game_over:
            return "Игра окончена. Начните новую игру."

        self.attempts += 1
        
        return utils.get_hint_message(self.secret_number, guess) + " Сделано попыток: " + str(self.attempts)

if __name__ == "__main__":
    root = tkinter.Tk()
    gui = gui.GameGUI(root)
    root.mainloop()