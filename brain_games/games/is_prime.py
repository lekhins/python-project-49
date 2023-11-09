import math
from random import randint

CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    root = math.sqrt(num)
    i = 2
    while i <= root:
        if num % i == 0:
            return False
        else:
            i += 1
    return True


def run_game():
    question = randint(0, 100)
    prime = 'yes' if is_prime(question) else 'no'

    return question, prime
