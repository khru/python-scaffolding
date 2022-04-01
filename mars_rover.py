class _Compass:
    __compass = ['N', 'E', 'S', 'W']

    def __init__(self):
        self.__orientation = 0

    def rotate_right(self):
        self.__orientation = (self.__orientation + 1) % len(self.__compass)

    def rotate_left(self):
        self.__orientation = (self.__orientation - 1) % len(self.__compass)

    def orientation(self):
        return self.__compass[self.__orientation]


class MarsRover:
    __PLATEAU_SIZE = 10

    def __init__(self):
        self.__compass = _Compass()

    def execute(self, commands: str):
        column: int = 0
        row: int = 0
        column_increment: int = 1
        row_increment: int = 0
        for command in commands:
            if command == 'M':
                column = ((column + column_increment) % self.__PLATEAU_SIZE)
                row = ((row + row_increment) % self.__PLATEAU_SIZE)
            if command == 'L':
                self.__compass.rotate_left()
            if command == 'R':
                self.__compass.rotate_right()
                column_increment = 0
                row_increment = 1
        return str(row) + ':' + str(column) + ':' + self.__compass.orientation()
