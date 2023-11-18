from math import gcd
from random import randint
from typing import Tuple

from brain_games.game_engine import run_game

CONDITION = "Find the greatest common divisor of given numbers."


def generate_game_data() -> Tuple[str, str]:
    """Генерация данных"""
    a = randint(1, 100)
    b = randint(1, 100)

    question = f"{a} {b}"

    correct = gcd(a, b)

    return question, str(correct)


def play():
    run_game(CONDITION, generate_game_data)
