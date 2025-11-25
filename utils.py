def validate_input(user_input):
    """Проверяет, можно ли преобразовать ввод в целое число."""
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def get_hint_message(secret, guess):
    if guess < secret:
        return "Загаданное число больше."
    elif guess > secret:
        return "Загаданное число меньше."
    else:
        return "Вы угадали!"