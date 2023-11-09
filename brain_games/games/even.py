from random import randint
from typing import Tuple

CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def run_game(): # -> Tuple[int, str]
    question = randint(1, 100)

    if question % 2 == 0:
        is_even = "yes"
    else:
        is_even = "no"

    return question, is_even
