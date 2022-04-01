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


class Command:
    ROTATE_RIGHT: str = 'R'
    ROTATE_LEFT: str = 'L'
    MOVE_FORWARD: str = 'M'
    __COMMANDS: dict = {
        ROTATE_LEFT: ROTATE_LEFT,
        ROTATE_RIGHT: ROTATE_RIGHT,
        MOVE_FORWARD: MOVE_FORWARD
    }

    def __init__(self, command: str):
        if self.__COMMANDS.get(command) is None:
            raise TypeError('Invalid command used: ' + command)

        self.__command = self.__COMMANDS.get(command)

    def __eq__(self, other: str):
        return self.__command == other


class CommandList:
    commands: list[Command] = []

    def __init__(self, commands: str):
        for command in commands:
            self.commands.append(Command(command))

    def get_all_commands(self) -> list[Command]:
        return self.commands


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
        for str_command in commands:
            command = Command(str_command)
            if command == Command.MOVE_FORWARD:
                self.__move()
            if command == Command.ROTATE_LEFT:
                self.__compass.rotate_left()
            if command == Command.ROTATE_RIGHT:
                self.__rotate_right()
        return str(self.__row) + ':' + str(self.__column) + ':' + self.__compass.orientation()
