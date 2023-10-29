from random import randint

CONDITION = "Find the greatest common divisor of given numbers."


def get_gcd(a, b):
    if a == b:
        return a
    if a < b:
        b, a = a, b

    remainder = a - b

    if remainder == 0:
        return b

    while remainder != 0:
        remainder = a - b
        a, b = b, remainder
    return a


def run_game():
    a = randint(1, 100)
    b = randint(1, 100)

    question = f"{a} {b}"

    correct = get_gcd(a, b)

    return (question, str(correct))
