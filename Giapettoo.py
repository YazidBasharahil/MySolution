# Solve the problem by using Linear Programming in python
# Giapettoo's  Woodcarving problem
# I discoved the Giapettoo have two decision variables, and three constraints
# Decision variables: soldiers and trains (X1, X2)
# I want to know what the maximum profit for Giapettoo
# Also, what's the maximum limit from Finishing, Carpentry, and Demand
# At the end, what's the optiomal soluation
# Hint: I convert from maximize to minimize to solve it. Then, when i find the optimal solution, i need to oppsite the sign from negative to positive for taking the optimal solution for profit  

import numpy as np
import scipy as sp
from scipy.optimize import linprog

#Objective Function:-
z = np.array([-3, -2])
# Left-Hand-Side of Constraints:-
a = np.array([[2,1], [1,1], [1,0]])
# Right-Hand-Side of Constraints:-
b = np.array([100, 80, 40])
X1_bound= (0, None)
X2_bound= (0, None)

# Find the optiomal soluation and the maximum variables
result = linprog(z, A_ub=a, b_ub=b, bounds= [X1_bound, X2_bound])
print(result)

# My information:
# Name: Yazid Salem Ba Sharahil
# ID: 1944950
# Senior of Industrial Engineering student in University of Jeddah
# Date: 02-11-2023
# (+966) 58-054-6339
# likedin:https://www.linkedin.com/in/yazid-ba-sharahil-31a2a9257/
