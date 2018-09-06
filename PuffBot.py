import handler
import automation
import keytrigger
import threading
import time

class PuffBot:

    def __init__(self):
        self.auto = automation.Automation()
        self.keytrig = keytrigger.KeyTrigger()
        self.internalThread = threading.Thread(target=self.run)

    def start(self):
        self.internalThread.start()
        self.keytrig.start()

    def run(self):
        while not handler.stop_flag:
            if handler.bot_flag:
                if not automation.bot_active:
                    self.auto.start()
            else:
                time.sleep(1)
        self.keytrig.thread.join()

if __name__ == "__main__":
    bot = PuffBot()
    bot.start()
