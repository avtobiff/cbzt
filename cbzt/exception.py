class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

class EndGame(Exception):
    def __init__(self, msg):
        self.msg = msg
