# http://matplotlib.org/1.3.1/examples/pylab_examples/multiple_yaxis_with_spines.html
import matplotlib.pyplot as plt
from csv import reader
from dateutil import parser
from matplotlib import dates

fig, host = plt.subplots()
fig.subplots_adjust(right=0.98, left=0.05)

with open('GKGF-1_GKGF_1_Greece_20170501_115603.csv', 'r') as f:
    data = list(reader(f))
temp_from_hum = [i[2] for i in data[1::]]
temp_from_press = [i[3] for i in data[1::]]
cpu_temp = [i[6] for i in data[1::]]
time = [parser.parse(i[1]) for i in data[1::]]

p1, = host.plot(time, temp_from_hum, "b^-", label="Temp from Hum")
p2, = host.plot(time, temp_from_press, "go-", label="Temp from Press")
p3, = host.plot(time, cpu_temp, "r*-", label="CPU Temp")

host.set_ylim(25, 35)

plt.xticks(time, time, rotation='vertical')

host.set_xlabel("Time")
host.set_ylabel("Temperature ($^\circ$C)")

host.yaxis.label.set_color("k")
tkw = dict(size=5, width=1.5)

host.tick_params(axis='y', colors="k", **tkw)
host.tick_params(axis='x', **tkw)

plt.title('Time - Temperatures from Sensors (Pressure, Humidity, CPU)\
           \n Date: Mon 1/5/2017 from 11:56:03 until 14:55:51 \n Team: GKGF-1')
plt.grid()
plt.legend([p1, p2, p3],
           ["Temp from Hum", "Temp from Press", "CPU Temp"], loc=0)
lines = [p1, p2, p3]
plt.show()
