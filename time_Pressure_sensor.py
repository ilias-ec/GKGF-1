from matplotlib import pyplot, dates
from csv import reader
from dateutil import parser

with open('GKGF-1_GKGF_1_Greece_20170501_115603.csv', 'r') as f:
    data = list(reader(f))
pressure = [i[5] for i in data[1::]]
time = [parser.parse(i[1]) for i in data[1::]]
pyplot.xticks(time, time , rotation='vertical')
pyplot.xlabel('Time')
pyplot.ylabel('Pressure (mbar)')
pyplot.grid()
pyplot.title('Time - Pressure Sensor \nDate: Mon 1/5/2017 from 11:56:03 until 14:55:51\nTeam: GKGF-1')
pyplot.ylim(999.2 , 999.85)
pyplot.plot(time, pressure, 'go-')
pyplot.show()
