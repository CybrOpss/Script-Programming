#Problem 1.7: Computing things

months = int(input("Enter the number of months the servers will run: "))

servers_costs = [3200, 5000, 1790, 8900, 2300]
monthly_cost_to_run = 100
total_cost = 0

for i in servers_costs:
    monthly_cost = i + monthly_cost_to_run * months
    print("The server costing "+str(i)+" costs on average "+ str(monthly_cost // months) + " each month.")
    total_cost += monthly_cost
print("Total cost: " + str(total_cost))
