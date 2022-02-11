"""
CSE 103 Tutorial_1
Yubo Cai
10/02/2022
"""


# ######################################################################################################################################
# Exercise 1
def square_root(n):
    k = 0
    while k * k < n:
        k = k + 1
    if k * k > n:
        k -= 1
    return k


# ######################################################################################################################################
# Exercise 2
def newton_square_root(n):
    k = n
    while k * k > n:
        k = int(0.5 * (k + n // k))
    return k


"""
It's really clear that the second method is much more effective compare with the first one, the first algorithm compute 
really slow when the input is around 10^16. However the second algorithm only have the computation of plus and divide which means 
it does not have to compute one number by one number like the first one, which makes it more effective.
"""


# ######################################################################################################################################
# Exercise 3
def isPrime(n):  # brute algorithms
    if n < 2:
        return False
    foundDivisor = False
    k = 2
    bound = newton_square_root(n)
    while (not foundDivisor) and (k <= bound):
        if n % k == 0:
            foundDivisor = True
        k += 1
    return not foundDivisor


def piBrute(n):
    num = 0
    for k in range(2, n + 1):
        if isPrime(k) is True:
            num += 1
    return num


def piEratosthenes(n):
    p = 0
    # initialize a row of n+1 lamp posts
    # all of which are lighted except the first two
    l = 2 * [False] + (n - 1) * [True]
    for k in range(2, n + 1):
        if l[k]:
            p += 1
            for m in range(2 * k, n + 1, k):
                l[m] = False
    return p


"""
When I apply the 10^6 and 10^7 the piBrute started to compute with a relative longer time compare with the second algorithms.
And the second program stop computing around at 10^9 that my computer is not able to compute the result.
"""


# ######################################################################################################################################
# Exercise 4
def reverseleft(l):  # from left to right
    r = []
    for i in range(len(l)):
        r = [l[i]] + r
    return r


def reverseright(l):  # from right to left
    r = []
    for i in range(len(l)):
        r.append(l[len(l) - 1 - i])
    return r


"""
We find that the reverseright this algorithms is much more effective compare with the first one. This implies that
adding the element at the end of the list is much effective since it's only change the length of the list and then
append the element into that new list
however the first method also change the index of all other elements in the list which cause the unefficiency
"""


# ######################################################################################################################################
# Exercise 5
def reverse_list(l):
    for i in range(len(l) // 2):
        tmp = l[i]
        l[i] = l[len(l) - 1 - i]
        l[len(l) - 1 - i] = tmp
    return l


def reverse_sublist(l, w, n):
    new_lis = l[w:w + n]
    return reverse_list(new_lis)

def revBlock (l , start , n ):
    if start >= 0 and start + n //2 < len ( l ):
        for i in range ( n //2):
            tmp = l [ start + i ]
            l [ start + i ] = l [ start +n -i -1]
            l [ start +n -i -1] = tmp

# ######################################################################################################################################
# Exercise 6
def rotate_list(l, k):
    if k > 0:
        left_half = l[len(l) - k:]
        right_half = l[:len(l) - k]
        return left_half + right_half
    elif k < 0:
        left_half = l[-k:]
        right_half = l[:-k]
        return left_half + right_half


"""ok the method above is not clear and I find a relavtive betther solution"""


def rotate(l, k):
    r = [0] * len(l)
    for i in range(len(l)):
        r[i] = l[(i + k) % len(
            l
        )]  # cause we might have the situation that i + k > len(l), therefore we need to use mod
    return r


# ######################################################################################################################################
# Exercise 7
def rotLInPlace(l):
    n = len(l)
    if n > 0:
        tmp = l[0]
        for i in range(1, n):
            l[i - 1] = l[i]
        l[n - 1] = tmp


def rotRInPlace(l):
    n = len(l)
    if n > 0:
        tmp = l[n - 1]
        for i in range(n - 1, 0,
                       -1):  # like the inverse procedure of the first one
            l[i] = l[i - 1]
        l[0] = tmp


def rotateInPlace(l, k):
    if k >= 0:
        for i in range(k):
            rotRInPlace(l)

    else:
        for i in range(-k):
            rotLInPlace(l)
    return l


"""
The function rotLInPlace performs 2 assignments at first then with a loop have (n-1) + 1 = n assignments, 
therefore for the rotLInPlace have n+2 assignments
So for the rotateInPlace have run k times of rotRInPlace which we have the result that the ratateInPlace 
have k*(n+2) assignments

However we compare with the function in EX6 we find this function only have the n assignment
"""

def rotateInPlaceRev(l, k):
    n = len(l)
    if k >= 0:
        k = n - (k % n )
    else:
        k = -k % n
    revBlock (l ,0 , k )
    revBlock (l ,k ,n - k)
    revBlock (l ,0 , n )
    return l 