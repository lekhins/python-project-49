from random import randint
from typing import Tuple
from brain_games.game_engine import run_game

CONDITION = "What number is missing in the progression?"


def generate_progression():
    """
    Генерация данных
    :return:
    """
    start = randint(1, 100)
    step = randint(1, 10)
    stop = start + step * 10

    progression = [str(x) for x in range(start, stop, step)]
    return progression


def generate_game_data() -> Tuple[str, str]:
    progression = generate_progression()

    random_index = randint(0, 9)
    correct = progression[random_index]

    progression[random_index] = ".."
    question = " ".join(progression)
    return question, correct


def play():
    run_game(CONDITION, generate_game_data)
