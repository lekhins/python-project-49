#!/usr/bin/env python3
from brain_games.engine_for_games import run_game_engine
from brain_games.games import gcd


def main():
    run_game_engine(gcd)


if __name__ == "__main__":
    main()
