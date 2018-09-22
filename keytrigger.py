from pynput.keyboard import Key, Listener, KeyCode
import threading
import handler

def on_press(key):
    pass
    #print('{0} pressed'.format(key))

def on_release(key):
    if key == Key.esc:
        return False
    elif key == KeyCode.from_char('s'):
        handler.bot_flag = True

def run():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
        handler.stop_flag = True

class KeyTrigger:

    def __init__(self):
        self.thread = threading.Thread(target=run)

    def start(self):
        self.thread.start()
#with Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()
