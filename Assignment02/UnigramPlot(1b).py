import pylab as pl
import numpy as np

rankList = []
freqList = []
f2 = open('rank.txt', 'r')
f3 = open('freq_01.txt', 'r')

lines_rank = f2.read()
lines_freq = f3.read()

varLines_Rank = lines_rank.split('\n')
varLines_Freq = lines_freq.split('\n')

for i in varLines_Freq:
    try:
        freqList.append(int(i))
    except ValueError:
        pass
    print i

for j in varLines_Rank:
    try:
        rankList.append(int(j))
    except ValueError:
        pass
    print j

print rankList

#
pl.plot(rankList, freqList)
pl.title("Rank VS Frequency of Unigrams")
pl.xlabel("Rank")
pl.ylabel("Frequency")

pl.show()

f2.close()
f3.close()
