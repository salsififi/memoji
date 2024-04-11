"""
Contains Game class
"""

import time

from board import Board
from square import Square, CoordinateError
from CONSTANTS import LEVELS, VALID_SIZES


class Game:
    """
    A game of MEMOJI
    """
    __slots__ = ['level', 'nb_of_turns', 'nb_of_pairs_found', 'board']

    def __init__(self, level: int) -> None:
        self.level = Game.check_level(level)
        self.nb_of_turns = 0
        self.nb_of_pairs_found = 0
        self.board = Board(self.board_size)

    @property
    def board_size(self) -> int:
        return VALID_SIZES[LEVELS.index(self.level)]

    @property
    def total_nb_of_pairs(self) -> int:
        return self.board_size ** 2 // 2

    def __repr__(self) -> str:
        return f"Partie de Memoji, niveau {self.level}"

    def ask_which_square(self, card_1_or_2: int) -> str:
        """
        Asks user which square to flip.
        User must give a valid coordinate of square, such as "C7" or "A2".
        Square must be face down (face_up) = False
        :param card_1_or_2: 1 or 2 (because user must flip 2 cards at each turn)
        :return: user's valid choice as a tuple(letter, number).
        """
        if self.nb_of_turns == 0 and card_1_or_2 == 1:
            print("Indiquez les coordonnées des cases en commençant par la lettre "
                  "(par exemple: c4).")

        while True:
            coordinates = input(f"Émoji n°{card_1_or_2} à dévoiler: ").upper()
            try:
                if Square.has_well_formatted_coordinates(coordinates) \
                        and self.board.is_existing_square(coordinates) \
                        and not self.board[coordinates].face_up:
                    return coordinates
                elif not self.board.is_existing_square(coordinates):
                    print(f"Le plateau de jeu n'a pas de case {coordinates}.")
                else:
                    print(f"L'émoji de la case {coordinates} est déjà dévoilé !")

            except CoordinateError as e:
                print(f"Saisie invalide: {e}")

    def display_board(self) -> None:
        """
        Displays board with:
        - columns letters and lines numbers
        - question marks for face-down cards
        - emojis for face-up cards
        """
        self.board.display_board()

    def say_turn_result(self, square1: str, square2: str) -> None:
        """
        Compares emojis, displays a message and adjusts squares face-up attribute value.
        :param square1: first square coordinates (such as "c7") specified by player
        :param square2: second square coordinates (such as "c7") specified by player
        """
        if self.board[square1].emoji == self.board[square2].emoji:
            print("Vous avez trouvé une paire ! 👍🏼")
            self.nb_of_pairs_found += 1
        else:
            print("Raté...")
            self.board[square1].face_up = False
            self.board[square2].face_up = False
        self.nb_of_turns += 1
        time.sleep(2)

    @staticmethod
    def check_level(level: int) -> int:
        if level not in LEVELS:
            raise LevelError("niveau invalide. Les niveaux vont "
                             f"de {min(LEVELS)} à {max(LEVELS)}.")
        return level


class LevelError(Exception):
    pass


if __name__ == '__main__':
    g = Game(3)
    g.display_board()
