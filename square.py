"""
Contains Square class
"""


class Square:
    """
    A square in a board game
    """

    __slots__ = ['column', 'row', 'emoji', 'face_up']

    def __init__(self, column_letter: str, row_number: int, emoji: str):
        self.column = column_letter
        self.row = row_number
        self.emoji = emoji
        self.face_up = False

    def __repr__(self):
        return f"{self.column}{self.row}: {self.emoji}"

    @staticmethod
    def has_well_formatted_coordinates(coordinates: str) -> bool:
        """
        Check if coordinates have a valid format.
        :param coordinates: a square coordinates such as "C7" or "A10"
        :return: True if coordinates have a valid format. Raises a CoordinateError if not

        >>> Square.has_well_formatted_coordinates("C15")
        True

        >>> Square.has_well_formatted_coordinates("z1")
        True

        >>> Square.has_well_formatted_coordinates("D0")
        Traceback (most recent call last):
            ...
        square.CoordinateError: Le nombre indiqué doit être strictement positif.

        >>> Square.has_well_formatted_coordinates("G")
        Traceback (most recent call last):
            ...
        square.CoordinateError: Il manque des informations dans cette coordonnée.

        >>> Square.has_well_formatted_coordinates("")
        Traceback (most recent call last):
            ...
        square.CoordinateError: Il manque des informations dans cette coordonnée.

        >>> Square.has_well_formatted_coordinates("22")
        Traceback (most recent call last):
            ...
        square.CoordinateError: 2 n'est pas une lettre de A à Z non accentuée.
        """

        # checking coordinate size
        if len(coordinates) < 2:
            raise CoordinateError("Il manque des informations dans cette coordonnée.")

        coordinates = coordinates.upper()
        column_letter, str_row_number = coordinates[0], coordinates[1:]

        # checking column letter
        if not ord('A') <= ord(column_letter) <= ord('Z'):
            raise CoordinateError(f"{column_letter} n'est pas une lettre de A à Z non accentuée.")

        # checking line number
        try:
            row_number = int(str_row_number)
        except ValueError:
            raise CoordinateError(f"{str_row_number} n'est pas un nombre.")
        if row_number < 1:
            raise CoordinateError("Le nombre indiqué doit être strictement positif.")

        return True


class CoordinateError(Exception):
    pass


if __name__ == '__main__':
    while True:
        test = input("(Q pour quitter): ")
        if test.upper() == 'Q':
            break
        try:
            Square.has_well_formatted_coordinates(test)
            print("OK!")
        except CoordinateError as e:
            print(f"PAS OK: {e}")
