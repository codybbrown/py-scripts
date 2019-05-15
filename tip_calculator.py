# Fri Jun 30 18:13:58 CDT 2017
# Cody Brown Python Study: Python Practice
# *********************************************************
# tip calculator written quick after reading
# on qora that i should write one ...
# *********************************************************

# refactor w/ case
def tip_cal(total, service_qual, tip_percentage):
	if tip_percentage == float:
		tip_percentage = tip_percentage
		if service_qual == 'poor':
			tip = total * .1
			total_w_tip = total + tip
			print("Tip: {:.2f}".format(tip))
			print("Total + tip: {:.2f}".format(total_w_tip))
		elif service_qual == "great":
			tip = float(total * .25)
			total_w_tip = total + tip
			print("Tip: {}".format(tip))
			print("Total + tip: {:.2f}".format(total_w_tip))
		else:
			tip = total * tip_percentage
			total_w_tip = total + tip
			print("Tip: {:.2f}".format(tip))
			print("Total + tip: {:.2f}".format(total_w_tip))
	else:
		tip_percentage = tip_percentage * .01
		if service_qual == 'poor':
			tip = total * .1
			total_w_tip = total + tip
			print("Tip: {:.2f}".format(tip))
			print("Total + tip: {:.2f}".format(total_w_tip))
		elif service_qual == "great":
			tip = float(total * .25)
			total_w_tip = total + tip
			print("Tip: {}".format(tip))
			print("Total + tip: {:.2f}".format(total_w_tip))
		else:
			tip = total * tip_percentage
			total_w_tip = total + tip
			print("Tip: {:.2f}".format(tip))
			print("Total + tip: {:.2f}".format(total_w_tip))

tip_cal(90.01496, "fine", .025)
