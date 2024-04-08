#!/usr/bin/env python3
from pulp import *
import argparse

# arugments
parser = argparse.ArgumentParser(description='Calculate cheapest viable meal')
parser.add_argument('--min', type=int, default=0, help='Minimum serving for each meal')
parser.add_argument('--o', type=str, default='solution.txt', help='File output location')
args = parser.parse_args()

# initialize model
model = LpProblem("DietProblem", LpMinimize)

chickenrice = LpVariable("chicken rice", args.min, None, LpContinuous)
egg = LpVariable("eggs", args.min, None, LpContinuous)
potpie = LpVariable("chicken pot pie", args.min, None, LpContinuous)
waffles = LpVariable("waffles", args.min, None, LpContinuous)
snickers = LpVariable("snickers", args.min, None, LpContinuous)

# define objective function (cost)
model += (chickenrice * 2.838) + (egg * .292) + (potpie * 2.046) + (waffles * .386) + (snickers * .15)

# define constraints
model += (chickenrice * 225) + (egg * 70) + (potpie * 950) + (snickers * 40) + (waffles * 410) <= 5000, "sodium(mg)"
model += (chickenrice * 810) + (egg * 70) + (potpie * 610) + (snickers * 80) + (waffles * 195) >= 2000, "calories"
model += (chickenrice * 72) + (egg * 6) + (potpie *  17) + (snickers * 1) + (waffles * 4.6)  >= 50, "protien(g)"
model += (chickenrice * 0.3) + (egg * 4)  >= 20, "vitamin d(mcg)"
model += (chickenrice * 39) + (egg * 30) + (potpie * 30) + (waffles * 260) >= 1300, "calcium(mg)"
model += (chickenrice * 1.2) + (egg * 0.9) + (potpie * 4.8) + (waffles * 3.6)  >= 18, "iron(mg)"
model += (chickenrice * 1335) + (egg * 70) + (potpie * 270) + (waffles * 50) >= 4700, "potassium(mg)"

# solve
model.solve()

# write to file
with open(args.o, 'w') as file:
    for v in model.variables():
        file.write(f"{v.name} = {v.varValue}\n")
    file.write(f"\ndaily cost = {pulp.value(model.objective)}\n")
    file.write(f"weekly cost = {pulp.value(model.objective) * 7}\n")
