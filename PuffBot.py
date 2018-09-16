import handler
import keytrigger
import threading
import time

class PuffBot:

    def __init__(self):
        self.jp = handler.jp
        self.keytrig = keytrigger.KeyTrigger()
        self.internalThread = threading.Thread(target=self.run)

    def start(self):
        self.internalThread.start()
        self.keytrig.start()

    def run(self):
        while not handler.stop_flag:
            if handler.bot_flag:
                self.jp.start()
            else:
                time.sleep(1)
        self.keytrig.thread.join()

if __name__ == "__main__":
    bot = PuffBot()
    bot.start()
