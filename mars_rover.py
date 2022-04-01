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
        self.__column: int = 0
        self.__column_increment: int = 1
        self.__row: int = 0
        self.__row_increment: int = 0

    def __move(self):
        self.__column = ((self.__column + self.__column_increment) % self.__PLATEAU_SIZE)
        self.__row = ((self.__row + self.__row_increment) % self.__PLATEAU_SIZE)

    def __rotate_right(self):
        self.__compass.rotate_right()
        self.__column_increment = 0
        self.__row_increment = 1        

    def execute(self, commands: str):
        for command in commands:
            if command == 'M':
                self.__move()
            if command == 'L':
                self.__compass.rotate_left()
            if command == 'R':
                self.__rotate_right()
        return str(self.__row) + ':' + str(self.__column) + ':' + self.__compass.orientation()
