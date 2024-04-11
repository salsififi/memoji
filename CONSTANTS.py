"""
Constants used for several modules
"""

# Board sizes: must be multiples of 2
MIN_BOARD_SIZE = 2
MAX_BOARD_SIZE = 10
VALID_SIZES = list(range(MIN_BOARD_SIZE, MAX_BOARD_SIZE + 1, 2))
LEVELS = list(range(len(VALID_SIZES)))

# For those 2 constants, index 0 is fake so that numbers correspond to their index
COLUMNS_LETTERS = [chr(i) for i in range(ord('A') - 1, ord('A') + MAX_BOARD_SIZE)]
ROWS_NUMBERS = list(range(0, MAX_BOARD_SIZE + 1))

EMOJIS = ['😀', '😁', '😂', '😃', '😄',
          '😊', '😋', '😎', '😍', '😘',
          '🍎', '⌚', '📱', '🚗', '🏠',
          '🐶', '🐱', '🐰', '🐻', '🐸',
          '🎻', '🎸', '🎷', '🎺', '🎹',
          '⚽', '🏀', '🎲', '🎳', '🎨',
          '🍕', '🍔', '🍟', '🍦', '🍰',
          '🍉', '🍇', '🍓', '🥝', '🥑',
          '🍺', '🍷', '🍸', '🍹', '🥂',
          '🌞', '🌙', '🌈', '☀️', '☁️']


if __name__ == '__main__':
    print(ROWS_NUMBERS)
