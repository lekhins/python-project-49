import math
from random import randint
from typing import Tuple
from brain_games.game_engine import run_game

CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """Генерация данных"""
    root = math.sqrt(num)
    i = 2
    while i <= root:
        if num % i == 0:
            return False
        else:
            i += 1
    return True


def generate_game_data()-> Tuple[int, str]:
    question = randint(0, 100)
    prime = 'yes' if is_prime(question) else 'no'

    return question, prime


def play():
    run_game(CONDITION, generate_game_data)
