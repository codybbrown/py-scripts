# Mon Jul  3 11:41:09 CDT 2017
# Cody Brown Python Study: Python Practice
# *********************************************************

# To calculate the percentage increase:
# First: work out the difference (increase) between the two numbers you are comparing.
# Increase = New Number - Original Number
# Then:  divide the increase by the original number and multiply the answer by 100.
# perceninc= Increase / Original Number * 100

# ************************ tests ************************
initial_worth = 0.001 # oringinal value
current_worth = .67 # appreciated value
holdings = 10000 # number of items
initial_investment = initial_worth * holdings
current_total = current_worth * holdings
bitcoin = 2800

# print(initial_investment, current_total)
def total_percent_increase(initial_worth, current_worth):
	difference = current_worth - initial_worth
	percent_increase = difference / initial_worth * 100.00
	return percent_increase
print(total_percent_increase(200, 1800))
percent_increase = total_percent_increase(initial_worth, current_worth)


# (percent_increase / 100 + 1) * initial_value
def new_total_value(initial_worth, est_percent_increase, holdings):
	percent_increase = est_percent_increase * 1.0
	profit = initial_worth * percent_increase * holdings * .01
	new_investment = initial_investment + profit
	total_holdings = new_investment * holdings

	print("Initial Price Paid Per Holding: ${:.2f}".format(initial_worth))
	print("Number Held: {}".format(holdings))
	print("Initial Total Investment: ${:.2f}".format(initial_investment))
	print("Percent Increase: %{:.2f}".format(percent_increase))
	print("Profit: ${:.2f}".format(profit * holdings * .001))
	print("Dollar Worth: ${:.2f}".format(new_investment))
	print("Bitcoin Worth: ${:.2f}".format(new_investment*bitcoin))


