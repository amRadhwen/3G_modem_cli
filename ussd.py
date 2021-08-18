from gsmmodem.exceptions import CmeError


class USSD:

    def __init__(self, modem):
        self.modem = modem

    
    def execUSSD(self, ussd_string):
        ussd_code_string = self.validateUssd(ussd_string)
        if ussd_code_string:
            self.response = None
            try:
                self.response = self.modem.sendUssd(ussd_code_string[0], 5)
                #print(self.response.message)
                for responseText in ussd_code_string[1:]:
                    print(responseText)
                    #self.sessionControl(responseText)
                return self
            except CmeError:
                print("Invalid USSD mode !")
                return False
            else:
                print("Unexpected Error, Try Again !")
                return False
        else:
            return False
    
    def sessionControl(self, repText):
        while self.response.sessionActive:
            print(repText)
            self.response = self.response.reply(repText)
            print(self.response.message)
    
    def validateUssd(self, ussdCodeText):
        ussdSeq = []
        if ussdCodeText.startswith("*") and ussdCodeText.endswith("#"):
            index = ussdCodeText.find("*", 1)
            if index != -1:
                ussdSeq.append(ussdCodeText[0:index]+"#")
                while index != -1:
                    index = ussdCodeText.find("*",index+1)
                    ussdSeq.append(ussdCodeText[index-1])
                #ussdSeq.append("#")
                return ussdSeq
            else:
                ussdSeq.append(ussdCodeText)
                return ussdSeq
        else:
            return False