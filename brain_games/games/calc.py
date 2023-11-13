import random

from brain_games.game_engine import run_game

CONDITION = 'What is the result of the expression?'


def generate_game_data() -> tuple:
    """
    Генерация данных
    :return:
    """
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    question = f'{random_number1} {operation} {random_number2}'

    correct_result = 0  # переменная по дефолту
    if operation == '+':
        question = f'{random_number1} + {random_number2}'
        correct_result = random_number1 + random_number2
    elif operation == '-':
        question = f'{random_number1} - {random_number2}'
        correct_result = random_number1 - random_number2
    elif operation == '*':
        question = f'{random_number1} * {random_number2}'
        correct_result = random_number1 * random_number2

    return question, correct_result


def play():
    run_game(CONDITION, generate_game_data)
