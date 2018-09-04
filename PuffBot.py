import handler
import automation
import keytrigger

class PuffBot:

    def __init__(self):
        self.automation = automation.Automation
        self.keytrigger = keytigger.KeyTrigger

    def start(self):
        self.automation.start()
        self.keytrigger.start()
