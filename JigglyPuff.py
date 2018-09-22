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

    def tick(self):
        Character.tick(self)

    def stop_moving(self):
        self.stop_moving_down()
        self.stop_moving_left()
        self.stop_moving_right()

    def short_jump(self):
        pyautogui.keyDown('up')
        pyautogui.keyUp('up')

    def move_left(self):
        pyautogui.keyDown('left')

    def move_right(self):
        pyautogui.keyDown('right')

    def stop_moving_left(self):
        pyautogui.keyUp('left')

    def stop_moving_right(self):
        pyautogui.keyUp('right')

    def move_down(self):
        pyautogui.keyDown('down')

    def stop_moving_down(self):
        pyautogui.keyUp('down')

    def run(self):
        start_time = time.time()
        while not handler.stop_flag:
            if time.time() - start_time >= .001:
                self.tick()
            else:
                time.sleep(.001)

    def start(self):
        if not self.isAlive:
            self.thread.start()
            self.isAlive = True

    def setLoc(self, x, y):
        Character.setLoc(x, y)
