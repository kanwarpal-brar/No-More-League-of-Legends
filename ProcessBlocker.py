import psutil
import threading
import time
import os
import sys


# Application to Block a provided exe/process name from running

class ProcessBlocker:
    def __init__(self, names, interval, timerminutes=-1):
        self.process = names
        self.checkInterval = interval
        self.endTime = int(time.time() + timerminutes * 60) if timerminutes >= 0 else None

    # returns array of true/false if any process in this.process is running
    def processIsRunning(self):
        checks = [False for i in self.process]
        for p in psutil.process_iter():
            if p.name() in self.process:
                checks[self.process.index(p.name())] = True
        return checks

    # Will attempt to kill/end a process with any of this.process
    def killProcess(self, checks):
        for i in range(0, len(checks)):
            if checks[i]:
                try:
                    os.system("taskkill /f /im " + self.process[i])
                except:
                    pass

    # Checks if processing is running, or sleeps if not
    def waitForProcess(self):
        while self.endTime is None or time.time() <= self.endTime:
            checks = self.processIsRunning()
            if True in checks:
                self.killProcess(checks)
            else:
                time.sleep(self.checkInterval)
