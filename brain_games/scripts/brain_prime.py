from brain_games.engine_for_games import run_game_engine
from brain_games.games import is_prime


def main():
    run_game_engine(is_prime)


if __name__ == "__main__":
    main()