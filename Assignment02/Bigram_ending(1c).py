import pylab as pl
import numpy as np



f = open('Bi_try.txt', 'r')

lines = f.read()
varLines = lines.split("\n")
#
# f1 = open('rank_bi.txt', 'wa')
# f2 = open('freq_bi.txt', 'wa')

rankList = []
freqList = []

rank = 1
for line in varLines:
    l1 = line.split(" ")
    if len(l1)>1:
        if l1[1]=='</s>':
            rankList.append(rank)
            freqList.append(int(l1[2]))
            rank+=1
    else:
        pass
#
# print freqList
# print rankList

pl.plot(rankList, freqList)
pl.title("Rank VS Frequency of P(X|</s>)")
pl.xlabel("Rank")
pl.ylabel("Frequency")
pl.ylim(0.0, 200.0)
pl.show()

f.close()
