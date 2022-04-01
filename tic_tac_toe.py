class Game:

    def __init__(self):
        self._last_player = None
        self._board = _Board()

    def play(self, player, x, y):
        if self._last_player is None and player != 'X':
            raise Exception('Invalid first player')

        if player == self._last_player:
            raise Exception('Invalid next player')

        self._board.play(player, x, y)

        self._last_player = player

    def winner(self):
        return self._board.has_a_winner()


class _Board:
    __BOARD_SIZE = 3

    def __init__(self):
        self.__plays = []

    def play(self, symbol, x, y):
        if self.__move_at(x, y) is not None:
            raise Exception('Invalid position')
        self.__plays.append(_Move(x, y, symbol))

    def __move_at(self, x, y):
        for t in self.__plays:
            if t.x == x and t.y == y:
                return t
        return None

    def a_player_won_on_a_row(self, row):
        return self.__move_at(row, 0) == self.__move_at(row, 1) \
               and self.__move_at(row, 2) == self.__move_at(row, 1)

    def has_a_winner(self):
        for row in range(self.__BOARD_SIZE):
            if self.__move_at(row, 0) is not None \
                    and self.__move_at(row, 1) is not None \
                    and self.__move_at(row, 2) is not None \
                    and self.a_player_won_on_a_row(row):
                return str(self.__move_at(row, 0).symbol)

        return None


class _Move:
    def __init__(self, x: int, y: int, player: str):
        self.x = x
        self.y = y
        self.symbol = _Player(player)

    def __eq__(self, other) -> bool:
        return other is not None and self.symbol == other.symbol


class _Player:
    def __init__(self, symbol: str):
        self.symbol = symbol

    def __eq__(self, other) -> bool:
        return other is not None and type(self) == type(other) and str(self) == str(other)

    def __str__(self) -> str:
        return self.symbol

