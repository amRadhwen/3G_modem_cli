from modem import MODEM
from ussd import USSD


#myModem = MODEM("COM78", 460800).connect()
#myModem.__changeCSCSMode__()
#myUssd = USSD(myModem.getModem())
#myUssd.execUSSD("*100*5#")

ussd_code = "*100*5#"
index = ussd_code.find("*")
print(index)

def formatUssd(ussdCodeText):
    ussd = []
    if ussdCodeText.startswith("*"):
        index = ussdCodeText.find("*", 1)
        if index != -1:
            ussd.append(ussdCodeText[0:index]+"#")
            #index = ussdCodeText.find("*", index)
            while index != -1:
                index = ussdCodeText.find("*", index)
                print(ussdCodeText[index])
                ussd.append(ussdCodeText[index+1])
            return ussd
        else:
            ussd.append(ussdCodeText)
            return ussd
    else:
        return False

#print(formatUssd("*100*5#"))