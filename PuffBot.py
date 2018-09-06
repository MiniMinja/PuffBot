import handler
import automation
import keytrigger

class PuffBot:

    def __init__(self):
        self.automation = automation.Automation()
        self.keytrigger = keytrigger.KeyTrigger()

    def start(self):
        #self.automation.start()
        self.keytrigger.start()


if __name__ == "__main__":
    bot = PuffBot()
    bot.start()
