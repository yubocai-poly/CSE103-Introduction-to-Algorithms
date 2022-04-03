"""
CSE 103 Tutorial_5
Yubo Cai
17/03/2022
"""

# ######################################################################################################################################
# Exercise 1 - Hoare triples, in English
"""
1. {x = n} <program> {x = n + 3}
If x contains the value n, then after executing <program>, x will contain the value n + 3.

2. {x ≤ y} <program> {y ≤ x}
If the value of x is bounded above by the value of y, then after executing <program>, the value of y will be bounded above by the value of x.

3. {True} <program> {x = 5}
After executing <program>, x will contain the value 5. (A naive formulation would start with “if
True is true, then. . . ”, which is of course always the case, so we just omit it).

4. {True} <program> {False}
<program> never terminates. (A naive formulation would be “if True is true, then after executing
<program>, False will be true”. But True is always true, so we may just say “after executing
<program>, False will be true”. But False can never be true, so the only possibility is that there
is no “after”, that is, the execution of <program> never terminates).

5. {n ≥ 0} <program> {r^2 ≤ n ∧ (r + 1)^2 > n}
If n is non-negative, then after executing <program>, r will contain the floor of square root of n, we will have r = floor(n^0.5)
"""

# ######################################################################################################################################
# Exercise 2 - valid and invalid Hoare triples
"""
1. valid 

2. valid

3. valid

4. valid, since the precondition is False cause x can't contain 0 and 1 at the same time therefore as the logic, if the precondition is True then
no matter what the terminates about is True.

5. invalid pass change Nothing

6. valid, since 42 < 100 

7. valid, since pass never terminates

8. valid, since the condition for the while loop holds then excute

9. valid, since the condition for the while loop doesn't hold therefore if the precondition is true then the Hoare triples is valid

10. Valid: for the same reason as above, but here we actually have an additional reason: if the loop did terminate, then it would do so precisely because x = 0!
"""

# ######################################################################################################################################
# Exercise 3 - valid and invalid Hoare triples
"""
1. 2x <= 10

2. 0 ≤ 3 ∧ 3 ≤ 5

3. 
(a) y > 0 ∧ y = 7 (no replacement);
(b) x > 0 ∧ y = 7 (we replace the first instance of y);
(c) y > 0 ∧ x = 7 (we replace the second instance of y);
(d) x > 0 ∧ x = 7 (we replace both instances of y);

4. x > 0 ∧ x = 7

5. This cannot be made into a valid instance of the assignment rule because the assertion before
the assignment contains x, which is the variable being assigned to, and the assigned expression
is constant (does not contain x).
"""

# ######################################################################################################################################
# Exercise 4 - a wrong assignment rule
"""
{True} x = x + 1 {x = x + 1}. Since x = x + 1 this is not a true condition then we can rewrite as {True} x = x + 1 {False},

Since if we apply this rule and we have {True} x = x + 1 {x = x + 1}, in {x = x + 1} which is obviously not a true condition.
since x = x + 1 can not be itself.
Then we have {True} x = x + 1 {False} which is not correct
"""

# ######################################################################################################################################
# Exercise 5 - the while loop

#! x ≤ 100
while x < 100:
    #! x ≤ 100 ∧ x < 100
    x = x + 1
    #! x ≤ 100
#! ???

#! x > 100
while x > 100:
    #! x > 100 ∧ x > 100
    x = x + 1
    #! x > 100
#! ???
"""
for the first condition should be {x <= 100 ∧ x >= 100} since the last line of the condition should be I ∧ ¬<expr> since if not the while
condition is met and the loop whould excuted
for the same reason the second should be {x>100 ∧ x <= 100}

then for the first one {x <= 100 ∧ x >= 100} the {x==100} and for the second which is {false}
"""

# ######################################################################################################################################
# Exercise 6 - The Truth Will Always Be
"""
1. normal structure
#! True
<var> = <expr>
#! True
This holds because True does not have any variable so there is unchanged any substitution, therefore this is always True

2. if sentense
#! True
if < expr >:
    #! True ∧ <expr>
    #! True
    < thenblock >
    #! True (by the induction hypothesis)
else :
    #! True ∧ ¬<expr>
    #! True
    < elseblock >
    #! True (by the induction hypothesis)
#! True

3. while sentense
#! True
while < expr >:
    #! True ∧ <expr>
    #! True
    < body >
    #! True (by the induction hypothesis)
#! True ∧ ¬<expr>
#! True
"""

# ######################################################################################################################################
# Exercise 7 - proving Exercise 2
"""
1.
    #! True
    #! 4 = 4
    x = 4
    #! x = 4

2. 
    #! x = 3
    #! x + 1 = 4 （传递项）
    x = x + 1
    #! x = 4

3.
    #! True
    #! 3 = 3
    x = 3
    #! x = 3
    y = 1    (y的赋值不改变x)
    #! x = 3

4.
    #! x = 0 ∧ x = 1
    #! False (因为x不可能即等于0又等于1，因此是False)
    x = 5
    #! False
    #! x = 42

5.
    #！x = 42
    pass
    #! x = 42
    #! x = 41

6. 
    #! x = 42
    pass
    #! x = 42
    #! x ≤ 100

7.
    #! True
    while True :
        #! True ∧ True
        pass
        #! True ∧ True
        #! True
    #! True ∧ ¬True (true and false therefore is false)
    #! False

8. 
    #! x = 0
    #! x = 0 ∨ x = 1
    while x = 0:
        #! (x = 0 ∨ x = 1) ∧ x = 0
        #! x = 0
        #! x + 1 = 1
        x = x + 1
        #! x = 1
        #! x = 0 ∨ x = 1
    #! (x = 0 ∨ x = 1) ∧ x 6= 0
    #! x = 1
"""

