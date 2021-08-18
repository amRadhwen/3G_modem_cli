from gsmmodem.exceptions import CmeError


class USSD:

    def __init__(self, modem):
        self.modem = modem

    
    def execUSSD(self, ussd_string):
        self.response = None
        try:
            self.response = self.modem.sendUssd(ussd_string, 5)
            print(self.response.message)
            #self.sessionControl()
            return self
        except CmeError:
            print("Invalid USSD mode !")
            return False
        else:
            print("Unexpected Error, Try Again !")
            return False
    
    def sessionControl(self, repText):
        while self.response.sessionActive:
            self.response = self.response.reply(repText)