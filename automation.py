import pyautogui
import threading
import time
import handler

bot_active = False

class Automation:
    def __init__(self):
        self.thread = threading.Thread(target=self.run)

    def start(self):
        global bot_active
        bot_active = True
        print('Starting Bot')
        self.thread.start()

    def just_jump(self):
        pyautogui.keyDown('up')
        pyautogui.keyUp('up')

    def run(self):
        while not handler.stop_flag:
            self.just_jump()
            time.sleep(1)
