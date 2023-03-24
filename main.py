import numpy as np
import sys

sys.setrecursionlimit(4000)

arr = []

def load():
    with open("ADS2022_cv5kradezDAT.txt", "r") as f:
        for i in f:
            x = [int(j.strip()) for j in i.split(',')]
            arr.append([x[0], x[1]])
            arr.append([x[2], x[3]])

load()
W = 2000
n = 2000
table = np.zeros([len(arr) + 1, len(arr) + 1], dtype=int)

def K(i, w):
    if i <= 0 or w <= 0:
        return 0
    global arr, table
    if(table[i][w] != 0):
        return table[i][w]
    table[i][w] = max(K(i - 2, w), arr[i][0] + K(i - 2, w - arr[i][1]), arr[i - 1][0] + K(i - 2, w-arr[i - 1][1])) 
    return table[i][w]

path = []

def reverseSearch(i, w):
    if i <= 0:
        return
    global table, path
    place = []
    max = table[i - 2][w]
    place = [i - 2, w, max]
    if(max < arr[i][0] + table[i - 2][w - arr[i][1]]):
        max = arr[i][0] + table[i - 2][w - arr[i][1]]
        palce = [i - 2, w - arr[i][1], max]
    if(max < arr[i - 1][0] + table[i - 2][w-arr[i - 1][1]]):
        max = arr[i-1][0] + table[i - 2][w-arr[i - 1][1]]
        palce = [i - 2, w - arr[i - 1][1], max]
    path.append(place)
    reverseSearch(place[0], place[1])


print(K(n - 1, W))
# reverseSearch(n - 1 ,W)
# print(path)
# np.savetxt("table.txt", table, fmt="%s")
