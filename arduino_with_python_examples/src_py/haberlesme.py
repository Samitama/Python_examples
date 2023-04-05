import serial

port = serial.Serial("COM3" ,115200,timeout=1)

while True:
    data_read = port.readline().decode("utf-8").strip()
    if not data_read:
        pass
    else:
        first, pot_value1, pot_value2, _ = data_read.split("|")
        print(first)
        print(pot_value1)
        print(pot_value2)
