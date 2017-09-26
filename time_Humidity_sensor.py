from matplotlib import pyplot, dates
from csv import reader
from dateutil import parser

with open('GKGF-1_GKGF_1_Greece_20170501_115603.csv', 'r') as f:
    data = list(reader(f))
humidity = [i[4] for i in data[1::]]
time = [parser.parse(i[1]) for i in data[1::]]
pyplot.xticks(time, time , rotation='vertical')
pyplot.xlabel('Time')
pyplot.ylabel('Humidity Sensor (%rH) ')
pyplot.grid()
pyplot.title('Time - Humidity Sensor \nDate: Mon 1/5/2017 from 11:56:03 until 14:55:51\nTeam: GKGF-1')
pyplot.ylim(35.5 , 40.0)
pyplot.plot(time, humidity, 'bo-')
pyplot.show()
