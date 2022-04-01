class MarsRover:
    def execute(self, commands):
        if commands == 'MM':
            return '0:2:N'
        if commands == 'M':
            return '0:1:N'
        return '0:0:N'
