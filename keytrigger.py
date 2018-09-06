from pynput.keyboard import Key, Listener
import threading

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        return False

def run():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

class KeyTrigger:

    def __init__(self):
        self.thread = threading.Thread(target=run)

    def start(self):
        self.thread.start()
#with Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()
