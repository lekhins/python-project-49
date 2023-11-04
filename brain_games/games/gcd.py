from math import gcd
from random import randint
from typing import Tuple
CONDITION = "Find the greatest common divisor of given numbers."


def run_game() -> Tuple[str, str]:
    a = randint(1, 100)
    b = randint(1, 100)

    question = f"{a} {b}"

    correct = gcd(a, b)

    return question, str(correct)
