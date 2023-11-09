from operator import add, sub, mul
from random import randint, choice

from brain_games.engine_for_games import run_game_engine

CONDITION = 'What is the result of the expression?'
OPERATIONS = [("+", add), ("-", sub), ("*", mul)]


def run_game():
    a = randint(1, 100)
    b = randint(1, 100)

    operator, func = choice(OPERATIONS)

    question = f"{a} {operator} {b}"

    correct = func(a, b)

    return question, str(correct)


def play():
    run_game_engine(game=CONDITION)
