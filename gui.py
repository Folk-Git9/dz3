# gui.py
import tkinter as tk
from tkinter import messagebox
from main import GuessTheNumberGame  # Импортируем игровой класс

class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Угадай число")
        self.game = GuessTheNumberGame()

        self.label = tk.Label(master, text="Введите число от 1 до 100:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()
        self.entry.bind('<Return>', lambda event: self.check_guess())  # По нажатию Enter

        self.guess_button = tk.Button(master, text="Проверить", command=self.check_guess)
        self.guess_button.pack()

        self.new_game_button = tk.Button(master, text="Новая игра", command=self.new_game)
        self.new_game_button.pack()

        self.output = tk.Text(master, height=10, width=50, state=tk.DISABLED)
        self.output.pack()

    def check_guess(self):
        user_input = self.entry.get()
        self.entry.delete(0, tk.END)  # Очищаем поле ввода

        try:
            guess = int(user_input)
            result = self.game.make_guess(guess)
            self.display_message(result)
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите целое число.")

    def display_message(self, message):
        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, message + "\n")
        self.output.see(tk.END)  # Прокрутка вниз
        self.output.config(state=tk.DISABLED)

    def new_game(self):
        self.game.start_new_game()
        self.output.config(state=tk.NORMAL)
        self.output.delete(1.0, tk.END)  # Очищаем поле вывода
        self.output.config(state=tk.DISABLED)
        self.display_message("Новая игра началась! Угадайте число.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = GameGUI(root)
    root.mainloop()