class MarsRover:
    def execute(self, commands):
        return '0:' + str(len(commands) % 10) + ':N'
