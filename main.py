import serial
import time
def readICC():
    cmd="AT+QCCID\r"
    ser.write(cmd.encode())
    time.sleep(1)
    msg=ser.read(64)
    msg = str(msg)
    m = msg.rsplit("\\r\\n")
    n = m[1].rsplit(": ")
    return(n[1])
    
def readIMEI():
    cmd="AT+CGSN\r"
    ser.write(cmd.encode())
    time.sleep(0.5)
    msg=ser.read(64)
    msg = str(msg)
    #m = msg.rsplit("QCCID: ")
    m = msg.rsplit("\\r\\n")
    print(m)

def readFIRMWARE():
    cmd="AT+CGMR\r"
    ser.write(cmd.encode())
    time.sleep(0.5)
    msg=ser.read(64)
    msg = str(msg)
    #m = msg.rsplit("QCCID: ")
    m = msg.rsplit("\\r\\n")
    print(m)

def readALL():
    cmd="ATI\r"
    ser.write(cmd.encode())
    time.sleep(0.5)
    msg=ser.read(64)
    msg = str(msg)
    #m = msg.rsplit("QCCID: ")
    #m = msg.rsplit("\\r\\n")
    print(msg)

ser = serial.Serial('COM8', 115200, timeout=5)
print("ICC: " + readICC())
readIMEI()
readFIRMWARE()
#print("ICC: " + readIMEI())


