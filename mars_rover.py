class Compass:
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
        self.__compass = Compass()

    def execute(self, commands: str):
        column: int = 0
        for command in commands:
            if command == 'M':
                column = ((column + 1) % self.__PLATEAU_SIZE)
            if command == 'L':
                self.__compass.rotate_left()
            if command == 'R':
                self.__compass.rotate_right()
        return '0:' + str(column) + ':' + self.__compass.orientation()
