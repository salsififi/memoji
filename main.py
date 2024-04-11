"""
MÉMOJI !
A memory game with emojis
This project comes from a challenge proposed by @bucdany
on the Docstring Discord server.

Author: Simon Salvaing
Date of first version: 2024-04

Entry point
"""

from game import Game
from CONSTANTS import LEVELS


def choose_level() -> int:
    """
    Asks user to choose a game level.
    :return: level chosen, as an integer
    """
    print(f"Choisis un niveau de difficulté, de {LEVELS[0]} (facile) "
          f"à {LEVELS[-1]} (extrême): ", end="")
    while True:
        level = input()

        try:
            level = int(level)
        except ValueError:
            print("Saisie invalide. Recommence: ", end="")
            continue

        if level in LEVELS:
            return level
        print(f"Les niveaux vont de {LEVELS[0]} à {LEVELS[-1]}. Recommence: ", end="")


def main() -> None:
    level = choose_level()
    game = Game(level)

    while game.nb_of_pairs_found < game.total_nb_of_pairs:
        game.display_board()
        chosen_squares_coordinates = []
        for i in (1, 2):
            square_coordinates = game.ask_which_square(i)
            game.board[square_coordinates].face_up = True
            chosen_squares_coordinates.append(square_coordinates)
            game.display_board()
        game.say_turn_result(*chosen_squares_coordinates)

    print("🎉🍾🎉 BRAVO !!! 🎉🍾🎉")
    print(f"Tu as fini la partie en {game.nb_of_turns} coups.")


if __name__ == '__main__':
    main()
