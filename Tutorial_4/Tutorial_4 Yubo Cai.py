"""
CSE 103 Tutorial_4
Yubo Cai
10/03/2022
"""


# ######################################################################################################################################
# Exercise 1 - solving recurrences
"""
1. We may apply the Master Theorem with a = 2, b = 4 and c = 0.51:  we have a < b^c, so T(n) = Θ(n^0.51).

2. We may apply the Master Theorem with a = 4, b = 2 and c = 1:  we have a > b^c, so T(n) = Θ(n^2).

3. we find that the Master Theorem does not works, and T(n) <= 4nlog(n) which is bounded by 4nlog(n) and we compute with the lower and upper
bound we can fully prove that T(n) = Θ(nlogn)

4. We may apply the Master Theorem with a = 3, b = 3 and c = 1:  we have a = b^c, so T(n) = Θ(nlogn).

5. We may apply the Master Theorem with a = 7, b = 3 and c = 2:  we have a < b^c, so T(n) = Θ(n^2).

6. we may apply the similar way like 3 that we can find T(n) <= 3n^2log(n), also we can compute the lower and upper bound by induction that
T(n) = Θ(n^2logn)

7. We may apply the Master Theorem with a = 5, b = 2 and c = 2:  we have a > b^c, so T(n) = Θ(n^log2 5).

8. We substitute S(m) := T(2^m) then we have S(m) = 4S(m/2) + n^2, then we have S(m) = Θ(n^2logn) then we can compute the 
T(n) = Θ(log^2n*log(log n)).

9. We may apply the Master Theorem with a = 2, b = 8 and c = 1/3:  we have a = b^c, so T(n) = Θ(n^(1/3)logn).

10. We may substitute S(m) = T(logm) then we have T(logm) = 65T(logm) + 4^logm, and we have S(m) = 65S(m/8) + m^2. Finally we can apply the Master Theorem
that  a = 65, b = 8 and c = 2:  we have a > b^c, so T(n) = Θ(n^log8 65).

"""

# ######################################################################################################################################
# Exercise 2 - complexity analysis of loops
"""
1. Θ(n^2)

2. Θ(n^(1/2))

3. Θ(7n/8) = Θ(n)

4. Θ(n^(1/2))

5. Θ(n^(1/2)*n*n)= Θ(n^(5/2))

6. Θ(n^(1/2)*n*n)= Θ(n^(5/2))

7. if the last loop is not excuted, the complexity of the function is Θ(h^3), however if the last loop is excuted, since only 
when j is the factor of h, therefore there are h of factor of h in the range(h*h), then the complexity of the function is Θ(h*h*(h^2))
which imply that the complexity of the function is Θ(h^3+h*h*(h^2)) = Θ(h^4) = Θ(n^2)
"""