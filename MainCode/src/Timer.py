import time


class Timer:
    def __init__(self, delaySeconds):
        self.active = False
        self.startTime = 0
        self.endTime = delaySeconds

    def startTimer(self):
        self.startTime = time.time()
        self.active = True

    def stopTimer(self):
        self.active = False

    def resetTimer(self):
        self.startTime = time.time()

    def isTimeElapsed(self):
        if (self.startTime + self.endTime) < time.time():
            return True
        else:
            return False

    def isActive(self):
        return self.active
