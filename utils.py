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

def test_hint_message_higher():
    assert get_hint_message(10, 5) == "Загаданное число больше."

def test_hint_message_lower():
    assert get_hint_message(5, 10) == "Загаданное число меньше."

def test_hint_message_equal():
    assert get_hint_message(7, 7) == "Вы угадали!"
    
def test_validate_input_with_integer():
    assert validate_input("123") is True

def test_validate_input_with_negative_integer():
    assert validate_input("-5") is True

def test_validate_input_with_non_integer():
    assert validate_input("abc") is False

def test_validate_input_with_float():
    assert validate_input("12.3") is False

def test_validate_input_empty_string():
    assert validate_input("") is False


if __name__ == "__main__":
    test_hint_message_higher()
    test_hint_message_lower()
    test_hint_message_equal()
    test_validate_input_with_integer()
    test_validate_input_with_negative_integer()
    test_validate_input_with_non_integer()
    test_validate_input_with_float()
    test_validate_input_empty_string()