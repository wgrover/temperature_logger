import serial, os, sys, datetime
outfile = open("out.csv", "a")
port = ""
usb_count = 0
devices = os.listdir("/dev")
for device in devices:
    if "cu.usb" in device:
        port = device
        usb_count += 1
if usb_count == 0:
    sys.exit("No port found")
if usb_count > 1:
    sys.exit("Multiple ports found")
port = "/dev/" + port
print(port)
data = []
ser = serial.Serial(port, 115200, timeout=1)
ser.flush()
while True:
    s = ser.readline().decode("utf-8")
    if s.startswith("X") and s.strip().endswith("Y") and s.count("X") == 1 and s.count("Y") == 1:
        print(ser.inWaiting(), datetime.datetime.now().isoformat(), end="\t")
        outfile.write(datetime.datetime.now().isoformat())
        measurement = float(s[1:-3])
        print("%0.2f\t" % (measurement))
        outfile.write("," + str("%0.2f" % measurement))
        outfile.write("\n")