import threading
import time
import handler

bot_active = False
jp = handler.jp

class Automation:
    def __init__(self):
        self.thread = threading.Thread(target=self.run)

    def start(self):
        global bot_active
        bot_active = True
        print('Starting Bot')
        self.thread.start()

    def run(self):
        global jp
        while not handler.stop_flag:
            jp.tick()
            print(jp)
            time.sleep(1.0/30.0)
