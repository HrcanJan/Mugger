import numpy as np
import sys

sys.setrecursionlimit(4000)

f = open("ADS2022_cv5kradezDAT.txt", "r")
all = []
l = f.readline()
tmp = []
while(l):
    tmp.append(int(l.split(",")[0])) 
    tmp.append(int(l.split(",")[1])) 
    all.append(tmp)
    tmp = []
    tmp.append(int(l.split(",")[2])) 
    tmp.append(int(l.split(",")[3])) 
    all.append(tmp)
    tmp = []
    l = f.readline()

W = 2000
n = 2000
table = np.zeros([len(all) + 1, len(all) + 1], dtype=int)

def K(i, w):
    if i <= 0 or w <= 0:
        return 0
    global all, table
    if(table[i][w] != 0):
        return table[i][w]
    table[i][w] = max(K(i-2, w), all[i][0] + K(i - 2, w - all[i][1]), all[i - 1][0] + K(i - 2, w-all[i - 1][1])) 
    return table[i][w]

path = []

def reverseSearch(i, w):
    if i <= 0:
        return
    global table, path
    place = []
    max = table[i - 2][w]
    place = [i - 2, w, max]
    if(max < all[i][0] + table[i - 2][w - all[i][1]]):
        max = all[i][0] + table[i - 2][w - all[i][1]]
        palce = [i - 2, w - all[i][1], max]
    if(max < all[i - 1][0] + table[i - 2][w-all[i - 1][1]]):
        max = all[i-1][0] + table[i - 2][w-all[i - 1][1]]
        palce = [i - 2, w - all[i - 1][1], max]
    path.append(place)
    reverseSearch(place[0], place[1])


print(K(n - 1, W))
reverseSearch(n - 1 ,W)
# print(path)
# np.savetxt("table.txt", table, fmt="%s")
