from brain_games.cli import run, get_answer

def run_game_engine(game):
    player_name = run(game.CONDITION)
    score = 0
    while score < 3:
        question, correct = game.run_game()

        answer = get_answer(question)

        if answer != correct:
            print(f"'{answer}' is wrong answer ;(.\n Correct answer was '{correct}'.")
            print(f"Let's try again, {player_name}!")
            return
        else:
            print("Correct")
        score += 1

    print(f"Congratulations, {player_name}!")
