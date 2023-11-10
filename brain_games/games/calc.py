import random
from typing import Callable

from brain_games.game_engine import run_game

CONDITION = 'What is the result of the expression?'


def generate_game_data() -> tuple:
    """Генерация данных"""
    random_number1 = random.randint(1, 100)
    random_number2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])


    """Алгоритм расчет верного ответа"""
    correct_result = True  # переменная по дефолту
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


def play() -> Callable:
    run_game(CONDITION, generate_game_data)
