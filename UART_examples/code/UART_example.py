import serial
import time
port = serial.Serial('/dev/cu.usbserial-10', baudrate=9600, timeout=1)
port.reset_input_buffer()
while port.isOpen():
    for i in range(255):
        port.write(b'#|'+str(i).encode('utf-8')+b'|'+str(255-i).encode('utf-8')+b'|')
        if port.inWaiting() > 0:
            a = port.readline().decode('utf-8').split('|')
            print(a)
            time.sleep(0.5)
