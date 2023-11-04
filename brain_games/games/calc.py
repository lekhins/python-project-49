from operator import add, sub, mul
from random import randint, choice
from typing import Tuple

CONDITION = "What is the result of the expression?"
OPERATIONS = [("+", add), ("-", sub), ("*", mul)]


def run_game() -> Tuple[str, str]:
    # """
    #
    # :return:
    # """
    a = randint(1, 100)
    b = randint(1, 100)

    operator, func = choice(OPERATIONS)

    question = f"{a} {operator} {b}"

    correct = func(a, b)

    return question, str(correct)
