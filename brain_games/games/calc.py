from operator import add, sub, mul
from random import randint, choice
from typing import Tuple

from brain_games.engine_for_games import run_game_engine

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


def process_game(question_generator, start_game_text):
    pass


def play():
    process_game(
        question_generator=run_game_engine,
        start_game_text=CONDITION,
    )
