from random import randint, choice
from operator import add, sub, mul

CONDITION = "What is the result of the expression?"
OPERATIONS = [("+", add), ("-", sub), ("*", mul)]


def run_game():
    a = randint(1, 100)
    b = randint(1, 100)

    operator, func = choice(OPERATIONS)

    question = f"{a} {operator} {b}"

    correct = func(a, b)

    return (question, str(correct))
