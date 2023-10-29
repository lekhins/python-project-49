from random import randint

CONDITION = 'Answer "yes" if number even otherwise answer "no".'


def run_game():
    question = randint(1, 100)

    if question % 2 == 0:
        is_even = "yes"
    else:
        is_even = "no"

    return (question, is_even)