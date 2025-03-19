import matplotlib.pyplot as plt, datetime, math, sys
import matplotlib.dates as mdates

def arduino2celsius(arduino):
    tempK = math.log(10000.0 * ((1024.0 / arduino - 1)))  # natural logarithm, in both Arduino and Python
    tempK = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * tempK * tempK)) * tempK)
    tempC = tempK - 273.15
    return tempC


f = open(sys.argv[1], "r")

times = []
data = []

for line in f:
    tokens = line.split(",")
    times.append(datetime.datetime.fromisoformat(tokens[0]))
    data.append(arduino2celsius(float(tokens[1])))

plt.plot(times, data)
plt.xlabel("Time")
plt.ylabel("Temperature [°C]")
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.show()
