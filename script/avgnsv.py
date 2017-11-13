import re
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pylab as plt

degree = [1, 2, 3, 4]
avgnsv = [0, 0, 0, 0]
avgnbsv = [0, 0, 0, 0]
avgmsv = []
pattern = re.compile("^nSV.*$")
for x in range(1, 5):
	out = open('deg{0}.fold'.format(x), 'r')
	for line in out:
		if pattern.match(line):
			num = re.findall(r'\b\d+\b', line)
			avgnsv[x - 1] += int(num[0])
			avgnbsv[x - 1] += int(num[1])
for x in range(0, 4):
	avgnsv[x] /= 10.0
	avgnbsv[x] /= 10.0
	avgmsv.append(avgnsv[x] - avgnbsv[x])

plt.plot(degree, avgnsv, 'ro-', label='avg nSV')
plt.plot(degree, avgmsv, 'go-', label='avg nMSV')
plt.ylabel('average number')
plt.xlabel('degree')
plt.legend(loc='best')
plt.show()
plt.savefig('./numSV.pdf')

