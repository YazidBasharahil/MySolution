# Solve the problem by using Linear Programming in python
# Powerco problem
# I discoved the Powerco have 12 decision variables, 3 supply constraints, and 4 demand constraints.
# decision variables: i are discribe the plant and j are decribe city (Xij)
# I want to know what the minimum cost for Powerco
# Also, what's the minimum limit from supply and demand
# At the end, what's the optiomal soluation

from pulp import *
import pandas as pd
import numpy as np

n_Plants = 3
n_Cities = 4

# Cost Matrix
Cost = np.array([[8, 6, 10, 9],
                [9, 12, 13, 7],
                [14, 9, 16, 5]])
# Demand Matrix
Cities_demands = np.array([45, 20, 30, 30])

# Supply Matrix
Plant_supply = np.array([35, 50, 40])
model = LpProblem("Supply-Demand-Problem", LpMinimize)
variable_names = [str(i)+str(j) for j in range(1, n_Cities+1) for i in range(1, n_Plants+1)]
variable_names.sort()
print("Variable Indices:", variable_names)
Decision_variables = LpVariable.matrix("X", variable_names, cat = "Integer", lowBound= 0 )
allocation = np.array(Decision_variables).reshape(3,4)
print("Decision Variable/Allocation Matrix: ")
print(allocation)
objective_function = lpSum(allocation*Cost)
print(objective_function)
model +=  objective_function
print(model)
# Supply Constraints
for i in range(n_Plants):
    print(lpSum(allocation[i][j] for j in range(n_Cities)) <= Plant_supply[i])
    model += lpSum(allocation[i][j] for j in range(n_Cities)) <= Plant_supply[i] , "Supply Constraints " + str(i)
# Demand Constraints
for j in range(n_Cities):
    print(lpSum(allocation[i][j] for i in range(n_Plants)) >= Cities_demands[j])
    model += lpSum(allocation[i][j] for i in range(n_Plants)) >= Cities_demands[j] , "Demand Constraints " + str(j)
model.solve(PULP_CBC_CMD())

status =  LpStatus[model.status]

print(status)
print("Total Cost:", model.objective.value())

# My information:
# Name: Yazid Salem Ba Sharahil
# ID: 1944950
# Senior of Industrial Engineering student in University of Jeddah
# Date: 02-27-2023
# (+966) 58-054-6339
# likedin:https://www.linkedin.com/in/yazid-ba-sharahil-31a2a9257/

