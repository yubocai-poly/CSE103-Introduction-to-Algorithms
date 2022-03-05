"""
CSE 103 Tutorial_3
Yubo Cai
03/03/2022
"""

# ######################################################################################################################################
# Exercise 1 - asymptotic notation 渐进分析
"""
1. True since n^2 + 100n + 2 = O(n^2) and n^2 < n^3, therefore is True

2. True since 75n^3 + 17 = O(n^3), therefore is True_

3. False, Since n^4 > n^3

4. False, since n^2 + 10n + 6 = Θ(n^3) also means that n^3 = O(n^2) which is not corrects

5. True, we can prove this with trying to find the limit of log(n)/n^epsilon, using the L'hospital 用洛必达法则求极限，然后上面是log和Fln没有区别
因此可以求出极限为0

6. True, we can simply and compare with log(n) and n^0.5, from the conclusion from question 5 we can have thie one is True. 

7. False, since n^2log(n) > n^2

8. False, since nlog(n) > nlog

9. False, since we can consider f(n) = 2n g(n) = n, then we can find 4^n != O(2^n) and 4^n = O(4^n) which implies this two is not equality

10. True
"""

# ######################################################################################################################################
# Exercise 2 -
"""
1. We may apply the Master Theorem with a = 3, b = 2 and c = 2:  we have a < b^c, so T(n) = Θ(n^2).

2. We may apply the Master Theorem with a = 4, b = 2 and c = 2:  we have a = b^c, so T(n) = Θ(n^2log(n))

3. We may apply the Master Theorem with a = 16, b = 4 and c = 1:  we have a > b^c, so T(n) = Θ(n^(log(b a)))= Θ(n^2)

4. This question the master theorem do not apply so we may use the tree method, we find the solution that Θ(n) since we have that 
f(n) = 5/2n 运用等比数列的公式进行计算

5. T(n) = Θ(nlog^2(n))

6. We may apply the Master Theorem with a = 3, b = 3 and c = 1/2:  we have a > b^c, therefore T(n) = Θ(n)
"""

# ######################################################################################################################################
# Exercise 3 - superpolynomial and subexponential 超越多项式
"""
f(n) = n^log(n)
"""


# ######################################################################################################################################
# Exercise 4 -  complexity analysis of a few simple functions
def digadd(c, d, e):
    """
    Parameters
    ----------
    c : carry bit
    d : int
    digit
    e : int
    digit .
    Returns
    -------
    A pair (c ’,a) where a is the digit resulting from
    the sum of digits d,e and the carry bit c,
    and c’ is the resulting carry bit
    """
    if c < 0 or d < 0 or e < 0 or c > 1 or d > 9 or e > 9:
        return -1, -1
    a = c + d + e
    return a // 10, a % 10

    # Complexity: Θ(1)


def rev(l):
    """
    Parameters 
    ----------
    l : list .
    Returns
    -------
    The list l reversed in place .
    """
    n = len(l)
    for i in range(n // 2):
        l[i], l[n - i - 1] = l[n - i - 1], l[i]

    # Complexity: Θ(n) while n is the n = len(l)


def shift(l, k):
    """
    Parameters
    ----------
    l : list
    k : int
    Returns
    -------
    The list l with k zeros appended .
    """
    for _ in range(k):
        l.append(0)
    return l

    # Complexity: Θ(k)


# ######################################################################################################################################
# Exercise 5 - a mystery function
def mystery(ml, nl):
    """
    Parameters
    ----------
    ml ,nl : list
    two non - negative integers represented as lists of digits

    Returns
    -------
    ???
    """
    h = len(ml) - len(nl)
    if h > 0:
        rev(nl)
        shift(nl, h)
        rev(nl)
    elif h < 0:
        rev(ml)  # Θ(n)
        shift(ml, -h)  # Θ(abs(h))
        rev(ml)  # Θ(n)
    n = len(ml)
    l = [0] * n
    c = 0
    for i in range(n):
        (c, l[n - i - 1]) = digadd(c, ml[n - i - 1], nl[n - i - 1])  # Θ(n)
    return l


"""
n = max(ml, nl)
Complexity: Θ(n)
addition of the two number, for example
"""


# ######################################################################################################################################
# Exercise 6 -  one more mystery function
def digmul(c, d, e):
    """
    Parameters
    ----------
    c : int
    carry digit
    d : int
    digit
    e : int
    digit .
    Returns
    -------
    A pair (c ’,a) where a is the digit resulting from d*e+c
    and c’ is the carry digit in case the result exceeds 9
    """
    if c < 0 or d < 0 or e < 0 or c > 8 or d > 9 or e > 9:
        return -1, -1
    a = c + d * e
    return a // 10, a % 10

    # Complexity: Θ(1)


def aux(nl, d):
    """
    Parameters
    ----------
    nl : list
    a non - negative integer represented as a list of digits
    d : int
    a digit .
    Returns
    -------
    ???
    """
    if d < 0 or d > 9:
        return -1
    c = 0
    l = []
    n = len(nl)
    for i in range(n):
        (c, a) = digmul(c, d, nl[n - i - 1])
        l.append(a)
    l.append(c)
    rev(l)
    return l

    # Complexity: Θ(n)


def mystery2(ml, nl):
    """
    Parameters
    ----------
    ml ,nl : list
    two non - negative integers represented as lists of digits
    Returns
    -------
    ???
    """
    ll = []
    n = len(nl)
    for i in range(n):
        ll.append(aux(
            ml, nl[n - i - 1]))  # here the complexity is Θ(n) * Θ(m = len(ml))
        shift(ll[i], i)
    r = [0]
    for i in range(len(ll)):
        r = mystery(r, ll[i])
    return r


"""
Since on the line on 217 we have the Θ(n) * Θ(m) therefore we can deduce that the complexity is Θ(mn)
"""

# ######################################################################################################################################
# Exercise 7 -  Karatsuba multiplication 卡拉楚巴算法
"""
def mul (k , m ):
    n = max(number of digits of k,number of digits of m) # O(1)
    if n == 1: # O(1)
        return k * m    # O(1)
    h = n // 2 # O(1)
    k1 = k // 10**h     # O(n)
    k2 = k % 10**h     # O(1)
    m1 = m // 10**h     # O(1)
    m2 = m % 10**h     # O(1)
    a = mul ( k1 , m1 )     # O(T(n/2))
    c = mul ( k2 , m2 )     # O(T(n/2))
    b = mul ( k1 + k2 , m1 + m2 ) - a - c     # O(T(n/2)) + O(n)
    return a * 10**(h*2) + b * 10**h + c # O(n)

1. assignments, any operation on bounded-size integers (variables in green): cost O(1);
2. getting the number of digits of an arbitrary integer: cost O(1);
3. multiplying or dividing an arbitrary integer by 10^n, or taking modulo 10^n: cost O(n);
4. adding or subtracting two n-digit numbers: O(n)
5. multiplying two 1-digit numbers: O(1)

Therefore we have the complexity of T(n) = 3T(n/2) + O(n) with a = 3 b = 2 and c = 1
then we have T(n) = O(n^log2 3) which is not the same as T(n) = Θ(n^2)
"""

# ######################################################################################################################################
# Exercise 8 -  not as clever as Anatoly
"""
a = mul ( k1 , m1 )     # O(T(n/2))
b = mul ( k1 , m2 )     # O(T(n/2))
c = mul ( k2 , m1 )     # O(T(n/2))
d = mul ( k2 , m2 )     # O(T(n/2))
retrun a+b+c+d is the computation with power of 10 don't really matter with complexity
therefore the complexity of this one is 
T(n) = 4T(n/2) + O(n) a = 4 b = 2 and c = 1 since a > b^c
T(n) = Θ(n^2) which is not as efficient as Karatsuba’s method
"""


# ######################################################################################################################################
# Exercise 9 -  naive matrix multiplication 矩阵相乘
def matmul(M, N):
    # we assume that M and N are square matrices of identical size
    n = len(M)
    R = [0] * n  # create the rows of the result
    for i in range(n):
        R[i] = [0] * n  # initialize the entries of the result to 0
    # 创造相对于的n*n的矩阵
    for i in range(n):
        for j in range(n):
            # R_ij = (i-th row of M) scalar product (j-th col of N)
            for k in range(n):
                R[i][j] += M[i][k] * N[k][j]

    return R


"""
since we have a three-time loop, therefore the complextity is T(n) = Θ(n^3)
"""

# ######################################################################################################################################
# Exercise 10 -  divide and conquer for matrix multiplication 矩阵相乘分而治之的算法
"""
T(n) = 8T(n/2) + O(n^2)
a = 4 b = 2 and c = 2 since a > b^c
T(n) = Θ(n^3)

however is we apply the Strassen’s algorithm we only need 7 recursion instead of 8
then we have T(n) = 7T(n/2) + O(n^2)
a = 7 b = 2 and c = 2 since a > b^c
T(n) = Θ(n^log2 7) which is smaller than Θ(n^3)
"""