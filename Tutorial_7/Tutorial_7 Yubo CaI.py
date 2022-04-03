"""
CSE 103 Tutorial_7
Yubo Cai
31/03/2022
"""

# ######################################################################################################################################
# Exercise 1 -  Preconditions and postconditions 前置条件和后置条件
"""
1. x <= 0 

2. x = 3 

3. x = i

4. x = 3 - y

5. x = 1 ∧ y = 47

6. y > 0 ∧ x = y + 6
"""


# ######################################################################################################################################
# Exercise 2 -  Decoding encodings 编码与解码
def adjLstToMat(L):
    n = len(L)
    G = n * [0]
    for i in range(n):
        G[i] = n * [0]
        for el in L[i]:
            G[i][el] = 1

    return G


def adjMatToLst(G):
    n = len(G)
    L = n * [0]
    for i in range(n):
        L[i] = []
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                L[i].append(j)

    return L


# ######################################################################################################################################
# Exercise 3 -  The list of weighted edges
mat1 = [[-1, 9, 7, 5], [-1, -1, -1, 2], [-1, -1, -1, 1], [3, -1, -1, -1]]


def getEdges(G):
    n = len(G)
    lis = []
    for i in range(n):
        for j in range(n):
            if G[i][j] != -1:
                lis.append((G[i][j], i, j))

    return lis

"""
print(getEdges(mat1))
result: [(9, 0, 1), (7, 0, 2), (5, 0, 3), (2, 1, 3), (1, 2, 3), (3, 3, 0)]
"""

# ######################################################################################################################################
# Exercise 4 -  Stacks and queues
class stack:
    def __init__(self):
        self.l = []

    def isEmpty(self):
        return self.l == []

    def push(self, x):
        self.l.append(x)

    def pop(self):
        return self.l.pop()


class queue:
    def __init__(self):
        self.l = []

    def isEmpty(self):
        return self.l == []

    def push(self, x):
        self.l.append(x)

    def pop(self):
        return self.l.pop(0)


s = stack()
for i in range(5):
    s.push(i)
for i in range(5):
    print(s.pop(), end=" ")

print(s)

q = queue()
for i in range(5):
    q.push(i)
for i in range(5):
    print(q.pop(), end=" ")

print(q)


class queue:
    def __init__(self):
        self.l = []
        self.h = 0

    def isEmpty(self):
        return self.h >= len(self.l)

    def push(self, x):
        self.l.append(x)

    def pop(self):
        self.h += 1
        return self.l[self.h - 1]

    def compress(self):
        for i in range(len(self.l) - self.h):
            self.l[i] = self.l[i + self.h]

        for i in range(self.h):
            self.l.pop()
        self.h = 0


q = queue()
for i in range(6):
    q.push(i)
for i in range(5):
    print(q.pop(), end=" ")
print()
print(q.l, q.h)
l = q.l
q.compress()
print(l, q.h)
"""
should print:
0 1 2 3 4
[0 , 1 , 2 , 3 , 4 , 5] 5
[5] 0

result: 
4 3 2 1 0 <__main__.stack object at 0x11331aee0>
0 1 2 3 4 <__main__.queue object at 0x11331a580>
1 2 3 4 5 
[0, 1, 2, 3, 4, 5] 5
[5, 1, 2, 3, 4, 5]
[5] 0
"""


# ######################################################################################################################################
# Exercise 5 -  Traversing a graph 图遍历/图搜索
