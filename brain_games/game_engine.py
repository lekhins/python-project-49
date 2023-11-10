import prompt

INCORRECT_ANSWER = '''\'{}\' is wrong answer ;(. Correct answer was \'{}\'.
Let\'s try again, \'{}\'!'''


def run_game(condition: str, generate_game_data: tuple):
    """

    Args:
        condition:str
        generate_game_data: tuple

    Returns:

    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    """Принтуем правила игры и генерируем циклы"""
    print(condition)
    game_cicl = 1

    while game_cicl <= 3:
        question = generate_game_data()
        correct_result = generate_game_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        """Получаем результат"""
        bool_result = str(correct_result) == user_answer.lower()

        """Ответ в зависимости корректности ответа"""
        if not bool_result:
            # Итого: неправильный ответ
            print(INCORRECT_ANSWER.format(user_answer, correct_result, name))
            break

        """Итого: правильный ответ"""
        print('Correct!')
        if game_cicl == 3:
            print(f'Congratulations, {name}!')

        game_cicl += 1
