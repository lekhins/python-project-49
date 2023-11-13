from random import randint
from typing import Callable
from typing import Tuple

from brain_games.game_engine import run_game

CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game_data() -> Tuple[int, str]:
    question = randint(1, 100)

    if question % 2 == 0:
        is_even = "yes"
    else:
        is_even = "no"

    return question, is_even


def play():
    run_game(CONDITION, generate_game_data)
