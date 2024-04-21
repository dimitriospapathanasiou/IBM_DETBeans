from pulp import LpProblem, LpVariable, lpSum

fleet_capacity = 50

# Sample flight schedule and delay data
flight_schedule = {'time_period_1': 10, 'time_period_2': 15, 'time_period_3': 20}
flight_delays = {'time_period_1': 2, 'time_period_2': 3, 'time_period_3': 1}

prob = LpProblem(name="TaxiFleetOptimization")

# Decision variables
X = {t: LpVariable(name=f"X_{t}", lowBound=0, cat="Integer") for t in flight_schedule.keys()}

# Constraints
prob += lpSum([X[t] for t in flight_schedule.keys()]) <= fleet_capacity, "Fleet Capacity Constraint"

for t in flight_schedule.keys():
    prob += X[t] >= flight_schedule[t] + flight_delays[t], f"Demand Constraint for {t}"
    prob += X[t] >= 0, f"Non-Negative Constraint for {t}"

prob.solve()
print("Status:", prob.status)
print("Optimal Fleet Size:")
for t, var in X.items():
    print(f"{t}: {var.varValue}")
