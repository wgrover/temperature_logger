import numpy, matplotlib.pyplot as plt, datetime, math


def arduino2celsius(arduino):
    tempK = math.log(
        10000.0 * ((1024.0 / arduino - 1))
    )  # natural logarithm, in both Arduino and Python
    tempK = 1 / (
        0.001129148 + (0.000234125 + (0.0000000876741 * tempK * tempK)) * tempK
    )
    tempC = tempK - 273.15
    return tempC


# f = open("test.csv", "r")

# times = []
# data = []

# for line in f:
#     tokens = line.split(",")
#     times.append(datetime.fromisoformat(tokens[0]))
#     data.append(float(tokens[1]))

# plt.plot(times, data)
# plt.show()

print(arduino2celsius(120))
