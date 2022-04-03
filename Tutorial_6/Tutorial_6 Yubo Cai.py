"""
CSE 103 Tutorial_6
Yubo Cai
24/03/2022
"""


# ######################################################################################################################################
# Samples - Dynamic programming to the rescue
def localMaxs(G, i, j, H):
    if i == len(G) or j == len(G[i]):
        H[i][j] = 0
        return
    if H[i + 1][j] < 0:
        localMaxs(G, i + 1, j, H)
    if H[i][j + 1] < 0:
        localMaxs(G, i, j + 1, H)
    H[i][j] = max(H[i + 1][j], H[i][j + 1]) + G[i][j]


def maxWDyn(G):
    H = [-1] * (len(G) + 1)
    for i in range(len(G)):
        H[i] = [-1] * (len(G[i]) + 1)
    H[len(G)] = [-1] * (len(G) + 1)
    localMaxs(G, 0, 0, H)
    return H[0][0]


map1 = [[1, 2, 2], [1, 1, 1], [9, 9, 1]]
print(maxWDyn(map1))


# ######################################################################################################################################
# Exercise 1 - the grid game, dynamically and greedily
def maxWDynNonRec(G):
    # G rectangular , non empty
    m, n = len(G) + 1, len(G[0]) + 1
    H = [None] * m
    for i in range(m):
        H[i] = [0] * n
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                H[m - i - 1][n - j - 1] = 0
            else:
                H[m - i - 1][n - j - 1] = max(H[m - i][n - j - 1],
                                              H[m - i - 1][n - j])
                H[m - i - 1][n - j - 1] += G[m - i - 1][n - j - 1]
    return H[0][0]


print(maxWDynNonRec(map1))


def maxWGreedy(G, i=0, j=0):
    if i >= len(G) or j >= len(G[i]):
        return 0
    if i == len(G) - 1:
        if j == len(G[i]) - 1:
            return G[i][j]
        else:
            j += 1
    else:
        if j == len(G[i]) - 1:
            i += 1
        else:
            if G[i + 1][j] > G[i][j + 1]:
                i += 1
            else:
                j += 1

    return G[i][j] + maxWGreedy(G, i, j)


print(maxWGreedy(map1))

import random

n = 1000
G = [0] * n
for i in range(n):
    G[i] = [0] * n
    for j in range(n):
        G[i][j] = random.randint(0, 9)

import time

t0 = time.time()
maxWDyn(G)
print(" Recursive DP algorithm took ", time.time() - t0, " seconds ")
t0 = time.time()
opt = maxWDynNonRec(G)
print(" Non - recursive DP algorithm took ", time.time() - t0, " seconds ")
t0 = time.time()
subopt = maxWGreedy(G)
print(" Greedy algorithm took ", time.time() - t0, " seconds ")
print(" Optimal weight :", opt)
print(" Suboptimal weight :", subopt)
print(" Ratio :", float(subopt) / float(opt))
"""
result 1: 
    Recursive DP algorithm took  0.9360108375549316  seconds 
    Non - recursive DP algorithm took  1.0886378288269043  seconds 
    Greedy algorithm took  0.0019030570983886719  seconds 
    Optimal weight : 13882
    Suboptimal weight : 11905
    Ratio : 0.8575853623397205

result 2: 
    Recursive DP algorithm took  1.1293649673461914  seconds 
    Non - recursive DP algorithm took  1.0080010890960693  seconds 
    Greedy algorithm took  0.0019059181213378906  seconds 
    Optimal weight : 13884
    Suboptimal weight : 12214
    Ratio : 0.879717660616537

Therefore we have:
1. the non-recursive implementation is slightly faster than the recursive one, although not
significantly so with this input size.

2. the greedy algorithm is significantly faster (by something like 2 orders of magnitude).

3. the weight found by the greedy algorithm is always about 85% of the optimal weight. This
is not a general rule, it just happens for this problem.
"""


# ######################################################################################################################################
# Exercise 2 - the edit distance
def editDist(u, v):
    if u == "":
        return len(v)
    elif v == "":
        return len(u)
    else:
        a = u[len(u) - 1]
        b = v[len(v) - 1]
        u = u[0:len(u) - 1]
        v = v[0:len(v) - 1]
        wsub = 0
        if a != b:
            wsub = 2
        s = editDist(u, v) + wsub
        d = editDist(u, v + b) + 1
        i = editDist(u + a, v) + 1
        return min(s, d, i)

"""
yes, the occurrences of (a,d) and (ab,d) appear in several times. This suggests that a dynamic programming approach might  
speed up the computation of the edit distance.
"""

# ######################################################################################################################################
# Exercise 3 -  the Needleman-Wunsch algorithm