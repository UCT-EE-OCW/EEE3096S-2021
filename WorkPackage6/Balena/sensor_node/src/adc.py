import socket
import sys
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

################TCP SEND SETUP###########################
HOST = '165.73.124.214'    # The remote host 
#HOST = '192.168.2.8'    # The remote host in local mode
PORT = 5003
f = open("/data/LocalaSensorLog.txt", "w+")
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    f.write("Could not open socket\n")
    f.close()
    sys.exit(1)



##################ADC Setup##############################
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)
#########################################################

print("Sensor Node it awake\n")
f.write("Sensor Node it awake\n")
f.flush()
s.sendall(b'Sensor Node it awake\n')

while(True):
    print("Raw ADC Value: \n", chan.value)
    print("ADC Voltage: " + str(chan.voltage) + "V\n")

    f.write("Raw ADC Value: "+ str(chan.value)+"\n")
    f.write("ADC Voltage: " + str(chan.voltage) + "V\n")
    f.flush()

    s.send(b'Sensor Node it awake')
    
    ADCstring = str(chan.value)
    s.send(b'Raw ADC Value: ' + bytes(ADCstring,'utf-8'))
    s.send(bytes(ADCstring,'utf-8'))

    voltagestring = str(chan.voltage)
    s.send(b'ADC Voltage: ')
    s.send(bytes(voltagestring,'utf-8') + b'V')
    
    time.sleep(5)


