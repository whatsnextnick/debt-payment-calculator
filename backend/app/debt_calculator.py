from pulp import LpProblem, LpVariable, IpSum, LpMinimize

def lp_debt_solver(data):
    balances = data['balances']
    interest_rates = data['interest_rates']
    min_payments = data['min_payments']
    budget = data['budget']

    LpProb = LpProblem('DebtRepayment', LpMinimize) #Defining LP minimization problem 

    #Assigninig problem Variables for each debt
    payments = [LpVariable(f'Payment_{i}', lowBound=min_payments[i]) for i in range(len(balances))]

    #Minimize total interest
    LpProb += lpSum(balances[i] * interest_rates[i] * payments[i] for i in range(len(balances)))

    #Constraints (budget):
    LpProb += lpSum(payments) <= budget

    #Solve LpProb
    LpProb.solve()

    return [p.varValue for p in payments]
