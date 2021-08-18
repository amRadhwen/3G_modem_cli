from modem import MODEM
from ussd import USSD


myModem = MODEM("COM78", 460800).connect()
myModem.__changeCSCSMode__()
myUssd = USSD(myModem.getModem())
myUssd.execUSSD("*124*5*3*1#")
