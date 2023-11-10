from random import randint, choice
from typing import Callable

from brain_games.game_engine import run_game

CONDITION = 'What is the result of the expression?'

PLUS = '+'
MINUS = '-'
MULTIPLY = '*'

NAME_OPERATIONS = (MINUS, PLUS, MULTIPLY)


def generate_game_data() -> tuple:
    """Генерация данных"""
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    operation = choice(NAME_OPERATIONS)
    question = f'{random_number1} {operation} {random_number2}'

    """Алгоритм расчет верного ответа"""
    correct_result = True  # переменная по дефолту
    if operation == PLUS:
        correct_result = random_number1 + random_number2
    elif operation == MINUS:
        correct_result = random_number1 - random_number2
    elif operation == MULTIPLY:
        correct_result = random_number1 * random_number2

    return question, correct_result


def play() -> Callable:
    run_game(CONDITION, generate_game_data)
