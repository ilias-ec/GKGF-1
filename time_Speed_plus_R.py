# http://matplotlib.org/1.3.1/examples/pylab_examples/multiple_yaxis_with_spines.html
import matplotlib.pyplot as plt
from csv import reader
from dateutil import parser
from matplotlib import dates

fig, host = plt.subplots()
fig.subplots_adjust(right=0.95, left=0.05)

par1 = host.twinx()

with open('GKGF_1_Greece_calculations.csv', 'r') as f:
    data = list(reader(f))
v_km_h = [i[6] for i in data[1::]]
R_earth_plus_ISS_alt = [(float(i[3])+float(i[4]))/1000.0 for i in data[1::]]
time = [parser.parse(i[0]) for i in data[1::]]

p1, = host.plot(time, v_km_h, "b^-", label="Speed (Km/h")
p2, = par1.plot(time, R_earth_plus_ISS_alt, "go-", label="R earth + altitude ISS (Km)")

host.set_ylim(27550 , 27650)
par1.set_ylim(6756, 6793)

plt.xticks(time, time, rotation='vertical')

host.set_xlabel("Time")
host.set_ylabel("Speed (Km/h)")
par1.set_ylabel("R earth + altitude ISS (Km)")

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())

tkw = dict(size=5, width=1.5)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)

host.tick_params(axis='x', **tkw)

plt.title('Time - Speed (Km/h) and R earth + altitude ISS (Km)\
           \n Date: Mon 1/5/2017 from 11:56:03 until 14:55:51 \n Team: GKGF-1')
plt.grid()
plt.legend([p1, p2],
           ["Speed (Km/h)", "R earth + altitude ISS (Km)"], loc=0)

lines = [p1, p2]

plt.show()




