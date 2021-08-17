from gsmmodem import GsmModem
from gsmmodem import exceptions
import serial
from serial import SerialException


class Modem:

    def __init__(self, port, baudrate, pin=None):
        self.port = port
        self.baudrate = baudrate
        self.pin = pin
    

    def connect(self):
        self.modem = GsmModem(self.port, self.baudrate)
        try:
            self.modem.connect(self.pin)
            self.modem.waitForNetworkCoverage()
            return self
        except exceptions.IncorrectPinError:
            print("Incorrect PIN !")
            return False
        except SerialException:
            print("Port \""+self.port+"\" already in use !")
            return False
        else:
            prin("Unexpected Error, Try again !")
            return False
    
    def __changeCSCSMode__(self):
        #self.modem.serial.write(str("AT^USSDMODE=0+\r").encode())
        check = self.modem.write("AT^USSDMODE?")[0].__contains__(": 1")
        self.modem.write('AT+CSCS="GSM"')
        if check:
            self.modem.write("AT^USSDMODE=0")
            return True
        else:
            return False




myModem = Modem("COM78", 460800).connect();
print(myModem)

    