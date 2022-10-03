from os import *
from sys import *
from collections import *
from math import *
from heapq import heappop, heappush
from bisect import bisect, insort

def getInversions(arr, n) :
    if n < 2: return 0
    sortList = []
    res = []
    for i, v in enumerate(arr):
        heappush(sortList, (v,i))
    x = []
    while sortList:
        v, i = heappop(sortList)
        y = bisect(x, i)
        res += y-i
        insort(x, i)
	return res