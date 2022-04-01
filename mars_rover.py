class MarsRover:
    __PLATEAU_SIZE = 10

    def execute(self, commands):
        return '0:' + str(len(commands) % self.__PLATEAU_SIZE) + ':N'
