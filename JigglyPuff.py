import handler
import pyautogui
import time
import threading

from Character import Character

class JigglyPuff(Character):
    def __init__(self, x, y):
        Character.__init__(self, x, y)
        self.thread = threading.Thread(target=self.run)
        self.isAlive = False

    def short_jump(self):
        pyautogui.keyDown('up')
        pyautogui.keyUp('up')
        Character.move

    def tick(self):
        Character.tick(self)

        if self.grounded:
            self.short_jump()

    def run(self):
        start_time = time.time()
        while not handler.stop_flag:
            if time.time() - start_time >= 1.0 / 30.0:
                self.tick()
            else:
                time.sleep(.001)

    def start(self):
        if not self.isAlive:
            self.thread.start()
            self.isAlive = True
