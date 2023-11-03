from random import randint

CONDITION = "What number is missing in the progression?"


def generate_progression():
    start = randint(1, 100)
    step = randint(1, 10)
    stop = start + step * 10

    # progression = list(range(start, stop, step))
    progression = [str(x) for x in range(start, stop, step)]
    return progression


def run_game():
    progression = generate_progression()

    random_index = randint(0, 9)
    correct = progression[random_index]

    progression[random_index] = ".."
    question = " ".join(progression)
    return (question, correct)
