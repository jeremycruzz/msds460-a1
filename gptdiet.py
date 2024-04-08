#!/usr/bin/env python3
import pulp

# Step 1: Define the problem
problem = pulp.LpProblem("Minimize_Cost_of_Food", pulp.LpMinimize)

# Step 2: Define decision variables
x1 = pulp.LpVariable("Chicken_Rice", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("Eggs", lowBound=0, cat='Continuous')
x3 = pulp.LpVariable("Chicken_Pot_Pie", lowBound=0, cat='Continuous')
x4 = pulp.LpVariable("Snickers", lowBound=0, cat='Continuous')
x5 = pulp.LpVariable("Waffles", lowBound=0, cat='Continuous')

# Step 3: Define objective function
problem += 2.838 * x1 + 0.292 * x2 + 2.046 * x3 + 0.150 * x4 + 0.386 * x5, "Total Cost"

# Step 4: Define constraints
# Sodium (max 5000mg)
problem += 225 * x1 + 70 * x2 + 950 * x3 + 40 * x4 + 410 * x5 <= 5000, "MaxSodium"
# Energy (min 2000kcal)
problem += 810 * x1 + 70 * x2 + 610 * x3 + 80 * x4 + 195 * x5 >= 2000, "MinEnergy"
# Protein (min 50g)
problem += 72 * x1 + 6 * x2 + 17 * x3 + 1 * x4 + 4.6 * x5 >= 50, "MinProtein"
# Vitamin D (min 20mcg)
problem += 0.3 * x1 + 4 * x2 + 0 * x3 + 0 * x4 + 0 * x5 >= 20, "MinVitaminD"
# Calcium (min 1300mg)
problem += 39 * x1 + 30 * x2 + 30 * x3 + 0 * x4 + 260 * x5 >= 1300, "MinCalcium"
# Iron (min 18mg)
problem += 1.2 * x1 + 0.9 * x2 + 4.8 * x3 + 0 * x4 + 3.6 * x5 >= 18, "MinIron"
# Potassium (min 4700mg)
problem += 1335 * x1 + 70 * x2 + 270 * x3 + 0 * x4 + 50 * x5 >= 4700, "MinPotassium"

# Step 5: Solve the problem
problem.solve()

# Step 6: Print the results
if pulp.LpStatus[problem.status] == "Optimal":
    print("Optimal solution found!")
    print(f"Quantities to purchase for minimizing cost:")
    for variable in problem.variables():
        print(f"{variable.name}: {variable.varValue}")
    print(f"Minimum cost: ${problem.objective.value()}")
else:
    print("No optimal solution found.")
