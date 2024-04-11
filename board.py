"""
Contains Board class
"""

import random
import copy

from square import Square, CoordinateError
from CONSTANTS import (COLUMNS_LETTERS, ROWS_NUMBERS, EMOJIS,
                       VALID_SIZES, MIN_BOARD_SIZE, MAX_BOARD_SIZE)


class Board:

    __slots__ = ["size", "emojis", "content"]

    def __init__(self, size: int) -> None:
        self.size = Board.check_size(size)
        self.emojis = random.sample(EMOJIS, k=size ** 2 // 2)
        self.content = self.set_content()

    @property
    def squares(self):
        return {f"{square.column}{square.row}": square
                for row_content in self.content for square in row_content}

    @property
    def columns_letters(self) -> list:
        return COLUMNS_LETTERS[1:self.size + 1]

    @property
    def rows_numbers(self) -> list:
        return ROWS_NUMBERS[1:self.size + 1]

    def __getitem__(self, coordinates: str) -> Square:
        coordinates = coordinates.upper()
        column_letter, row_number = coordinates[0], int(coordinates[1:])
        for row in self.content:
            for square in row:
                if square.column == column_letter and square.row == row_number:
                    return square
        raise CoordinateError(f"la case {coordinates} n'existe pas sur ce plateau.")

    def __repr__(self) -> str:
        return f"Plateau de taille {self.size}"

    def set_content(self) -> list[list[Square]]:
        """
        Creates a board with one pair of each emoji.
        :return: list of all lines of the board
        """
        # Emojis pool contains size ** 2 // 2 emojis
        emojis_pool = copy.deepcopy(self.emojis) * 2
        random.shuffle(emojis_pool)

        board_squares = []
        for i_line in range(1, self.size + 1):
            line_squares = []
            for i_column in range(1, self.size + 1):
                line_squares.append(
                    Square(COLUMNS_LETTERS[i_column],
                           ROWS_NUMBERS[i_line],
                           emojis_pool.pop()))
            board_squares.append(line_squares)
        return board_squares

    def display_board(self) -> None:
        """
        Displays board with:
        - columns letters and lines numbers
        - question marks for face-down cards
        - emojis for face-up cards
        """
        letters = COLUMNS_LETTERS[:self.size + 1]
        numbers = ROWS_NUMBERS[:self.size + 1]

        # Column headers
        for letter in letters[1:]:
            print("\t" + letter.rjust(2), end="")
        print()
        for _ in range(len(letters[1:])):
            print("\t" + "_".rjust(2), end="")
        print()

        for number in numbers[1:]:
            emojis_line = [square.emoji if square.face_up else "❓"
                           for square in self.content[number - 1]]
            print(f"{number} |".rjust(4) + "\t".join(emojis_line))

    def is_existing_square(self, coordinates: str) -> bool:
        """
        Check if coordinates exists on the board. Before using this function, you must ensure
        that coordinate is valid with Square.is_a_well_formatted_coordinate static method.
        :param coordinates: a valid square coordinate such as "C7" or "A10"
        :return: True if coordinate exists on this board, False if not.
        """
        coordinates = coordinates.upper()
        column_letter, line_number = coordinates[0], int(coordinates[1:])
        return column_letter in self.columns_letters and line_number in self.rows_numbers

    @staticmethod
    def check_size(size: int) -> int:
        """
        Checks if board size is valid.
        :param size: integer, must be in VALID_SIZES list
        :return: integer
        """
        if size not in VALID_SIZES:
            raise BoardSizeError(f"taille invalide. Les tailles doivent être "
                                 f"des nombres pairs compris entre {MIN_BOARD_SIZE} et {MAX_BOARD_SIZE} inclus.")
        return size


class BoardSizeError(Exception):
    pass


if __name__ == '__main__':
    p = Board(10)
    p.display_board()
    print(p["g1"])
    p["g1"].face_up = True
    p.display_board()
