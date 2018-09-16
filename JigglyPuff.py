import pyautogui
import time

import Character


class JigglyPuff(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y)
        self.thread = Thread(target=self.run)

    def short_jump(self):
        pyautogui.keyDown('up')
        pyautogui.keyUp('up')

    def tick(self):
        short_jump()

    def run(self):
        handler.bot_flag = True

        start_time = time.time()
        while not handler.stop_flag:
            if time.time() - start_time >= 1.0 / 30.0:
                tick()
            else:
                time.sleep(.001)
