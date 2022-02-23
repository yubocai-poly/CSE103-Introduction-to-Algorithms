"""
CSE 103 Tutorial_2
Yubo Cai
10/02/2022
"""


# ######################################################################################################################################
# Exercise 1 - binary search 二叉树搜索 - check
def binary_search(a, l):
    if l == []:
        return False
    mid = len(l) // 2
    if a == l[mid]:
        return True
    elif a < l[mid]:
        h = [0] * mid
        for i in range(mid):
            h[i] = l[i]
        return binary_search(a, h)
    else:
        h = [0] * mid
        for i in range(len(l) - mid):
            h[i] = l[i + mid + 1]
        return binary_search(a, h)


def binary_search_improve(a, l, start=0, end=-1):
    if end == -1:
        end = len(l)
    if l == []:
        return -1
    if start >= end:
        return -1

    mid = (start + end) // 2

    if a == l[mid]:
        return mid
    elif a < l[mid]:
        return binary_search_improve(a, l, start, mid)
    else:
        return binary_search_improve(a, l, mid + 1, end)


"""
So I try to apply the method from last semester about the binary search which is in place, we set two auxiliary index start and end
and use mid of the l[start:end] and to binary search both sides
"""

# ######################################################################################################################################
# Exercise 2 - Merge Sort 归并排序 - check
"""Merge Sort-归并排序: 
采用分治法:
分割：递归地把当前序列平均分割成两半。
集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。
"""


def merge(l1, l2):
    n1 = len(l1)
    n2 = len(l2)
    if n1 + n2 <= 1:
        return l1 + l2
    l = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:
        if l1[i1] <= l2[i2]:
            l[i] = l1[i1]
            i1 += 1
            i += 1
        elif l1[i1] > l2[i2]:
            l[i] = l2[i2]
            i2 += 1
            i += 1
    while (i1 < n1 and i2 == n2):
        l[i] = l1[i1]
        i1 += 1
        i += 1
    while (i2 < n2 and i1 == n1):
        l[i] = l2[i2]
        i2 += 1
        i += 1
    return l


def mergesort(l):
    n = len(l)
    if n <= 1:
        return
    mid = n // 2
    left = [0] * mid
    right = [0] * (n - mid)
    for i in range(mid):
        left[i] = l[i]
    for i in range(n - mid):
        right[i] = l[mid + i]
    return merge(mergesort(left), mergesort(right))


"""
https://www.youtube.com/watch?v=cVZMah9kEjI
"""

# ######################################################################################################################################
# Exercise 3 - Insertion sort 插入排序 - check
"""
插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
插入排序在实现上，通常采用in-place排序，因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：
1. 从第一个元素开始，该元素可以认为已经被排序
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5. 将新元素插入到该位置后
6. 重复步骤2~5
"""


def insertion_sort(l):
    n = len(l)
    if n <= 1:
        return l
    for i in range(len(l)):
        if i == 0:
            continue
        j = i
        while j > 0 and l[j - 1] > l[j]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1
    """j -= 1 是为了避免例如[4,3,2,7]调换完顺序以后变成[3,4,2,7]导致4，2的顺序没有调换的问题"""

    return l


"""
https://www.youtube.com/watch?v=R_wDA-PmGE4
"""

# ######################################################################################################################################
# Exercise 4 -  quicksort with Lomuto’s partitioning scheme - 快速排列
"""
Lomuto’s Partition Scheme:
This algorithm works by assuming the pivot element as the last element. If any other element is given as a pivot element then swap it first with the last element. 
Now initialize two variables i as low and j also low, swap whenever arr[I] <= arr[j], and increment i, otherwise only increment j. 
After coming out from the loop swap arr[i] with arr[hi]. This i stores the pivot element.

Hoare’s Partition Scheme:
Hoare’s Partition Scheme works by initializing two indexes that start at two ends, 
the two indexes move toward each other until an inversion is (A smaller value on the left side and greater value on the right side) found. 
When an inversion is found, two values are swapped and the process is repeated.

https://www.geeksforgeeks.org/hoares-vs-lomuto-partition-scheme-quicksort/

两者的关键区别在于是使用一个index还是两个
"""


def quicksort(l):
    quicksortRec(l, 0, len(l) - 1)
    return l


def quicksortRec(l, b, e):
    if b < e:
        p = partition(l, b, e)
        quicksortRec(l, b, p - 1)
        quicksortRec(l, p + 1, e)


def partition(l, b, e):
    pivot = l[e]
    p = b
    for i in range(b, e):
        if l[i] < pivot:
            l[i], l[p] = l[p], l[i]
            p += 1
    l[p], l[e] = l[e], l[p]
    return p


"""
https://www.youtube.com/watch?v=86WSheyr8cM
"""


# ######################################################################################################################################
# Exercise 5 - quicksort with Hoare’s partitioning scheme
def quicksort1(l):
    quicksortRec1(l, 0, len(l) - 1)
    return l


def quicksortRec1(l, b, e):
    if b < e:
        p = partition1(l, b, e)
        quicksortRec1(l, b, p)
        quicksortRec1(l, p + 1, e)


def partition1(l, b, e):
    pivot = l[b + (e - b + 1) // 2]
    i = b - 1
    j = e + 1
    while i < j:
        if i >= b:
            l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    while l[i] < pivot:
        i += 1
    while l[j] > pivot:
        j -= 1
    if j == e:
        j -= 1
    return j


# ######################################################################################################################################
# Exercise 6 - counting sorted lists - 计数排列
"""
https://www.youtube.com/watch?v=OKd534EWcdk
"""


def countingsort(l):
    c = [0] * 100
    n = len(l)
    for i in range(n):
        c[l[i]] += 1

    i = 0
    for k in range(100):
        for j in range(c[k]):
            l[i] = k
            i += 1
    return l


def csort(l, j, k):
    c = [0] * k
    n = len(l)
    for i in range(n):
        c[l[i][j]] += 1

    b = [0] * k
    for i in range(1, k):
        b[i] = b[i - 1] + c[i - 1]

    o = [0] * k
    r = [0] * n
    for i in range(n):
        h1 = l[i][j]
        r[b[h1] + o[h1]] = l[i]
        o[h1] += 1

    return r


"""
In[6]: csort([('frank', 198, 57), ('david', 167,83), ('charles', 174,59)], 2, 100)
Out[7]: [('frank', 198, 57), ('charles', 174, 59), ('david', 167, 83)]
"""

# ######################################################################################################################################
# Exercise 7 - radix sort - 基数排列
"""https://www.youtube.com/watch?v=XiuSW_mEn7g&t=23s"""


def lexsort(l, m, k):
    for i in range(m):
        l = csort(l, m - i - 1, k)
    return l


def maximum(l):
    i = 0
    for el in l:
        if el > i:
            i = el
    return i


def declen(n):
    if n == 0:
        return 1
    i = 0
    while n > 0:
        n = n // 10
        i += 1
    return i


def decexp(n, m):
    l = [0] * m
    for i in range(m):
        l[m - 1 - i] = n % 10
        n = n // 10
    return l


def deccmp(l):
    b = 1
    n = 0
    m = len(l)
    for i in range(m):
        n += l[m - 1 - i] * b
        b *= 10
    return n


def radixsort(l):
    if len(l) == 0:
        return l
    n = len(l)
    mx = maximum(l)
    m = declen(mx)
    d = [0] * n
    for i in range(n):
        d[i] = decexp(l[i], m)
    d = lexsort(d, m, 10)
    for i in range(n):
        l[i] = deccmp(d[i])
    return l

# ######################################################################################################################################
# Exercise 8 - stability - 基数排列

# Mergeosrt with the key
def mergekey(l1, l2, k):
    n1 = len(l1)
    n2 = len(l2)
    if n1 + n2 <= 1:
        return l1 + l2
    l = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2:
        if l1[i1][k] <= l2[i2][k]:
            l[i] = l1[i1]
            i1 += 1
            i += 1
        elif l1[i1] > l2[i2]:
            l[i] = l2[i2]
            i2 += 1
            i += 1
    while (i1 < n1 and i2 == n2):
        l[i] = l1[i1]
        i1 += 1
        i += 1
    while (i2 < n2 and i1 == n1):
        l[i] = l2[i2]
        i2 += 1
        i += 1
    return l


def mergesortkey(l, k):
    n = len(l)
    if n <= 1:
        return l
    mid = n // 2
    left = [0] * mid
    right = [0] * (n - mid)
    for i in range(mid):
        left[i] = l[i]
    for i in range(n - mid):
        right[i] = l[mid + i]
    return mergekey(mergesortkey(left, k), mergesortkey(right, k), k)

# Insertion sort with key
def insertion_sort_key(l, key):
    n = len(l)
    if n <= 1:
        return l
    for i in range(len(l)):
        if i == 0:
            continue
        j = i
        while j > 0 and l[j - 1][key] > l[j][key]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1

    return l

# Lomuto quicksort with key
def quicksort_key(l, key):
    quicksortRec_key(l, 0, len(l) - 1, key)
    return l


def quicksortRec_key(l, b, e, key):
    if b < e:
        p = partition_key(l, b, e, key)
        quicksortRec_key(l, b, p - 1, key)
        quicksortRec_key(l, p + 1, e, key)


def partition_key(l, b, e, key):
    pivot = l[e][key]
    p = b
    for i in range(b, e):
        if l[i][key] < pivot:
            l[i], l[p] = l[p], l[i]
            p += 1
    l[p], l[e] = l[e], l[p]
    return p

# quicksort with Hoare’s partitioning scheme with key
def quicksort1_key(l, key):
    quicksortRec1_key(l, 0, len(l) - 1, key)
    return l


def quicksortRec1_key(l, b, e, key):
    if b < e:
        p = partition1_key(l, b, e, key)
        quicksortRec1_key(l, b, p, key)
        quicksortRec1_key(l, p + 1, e, key)


def partition1_key(l, b, e, key):
    pivot = l[b + (e - b + 1) // 2][k]
    i = b - 1
    j = e + 1
    while i < j:
        if i >= b:
            l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    while l[i][k] < pivot:
        i += 1
    while l[j][k] > pivot:
        j -= 1
    if j == e:
        j -= 1
    return j
