# Wed Jun 21 19:51:21 2017
# Cody Brown
# loan ammortization
# ------------------------

# This can REALLY use a refactor

total_owed = 8070.72 + 2758.22
other_total = 11000.00
MONTHS_PER_YEAR = 12
def ammortize(loan_amount, years, apr):
    total_payments = years * MONTHS_PER_YEAR

    def payment(loan_amount, apr):
        a = float(loan_amount)
        n = total_payments
        mon_int_rate = (apr * .01) / MONTHS_PER_YEAR
        d = ((1 + mon_int_rate) ** n - 1) / (mon_int_rate * (1 + mon_int_rate)** n)
        mo_pay = a / d
        return mo_pay

    def interest(loan_amount, apr, monthly_payment):
        mon_int_rate = (apr * .01) / MONTHS_PER_YEAR
        monthly_interest = mon_int_rate * float(loan_amount)
        return monthly_interest
    print("Total Loan Amount Needed: \t{}".format(loan_amount))
    current_monthly = 473.00 + 324.65
    print("Current Monthly Payment: \t{}".format(current_monthly))
    monthly_payment = payment(loan_amount, apr)
    monthly_savings = current_monthly - monthly_payment
    print("New Monthly Payment: \t{}".format(round(monthly_payment, 2)))
    print("Monthly Savings: \t{:.2f}".format(monthly_savings))
    print("Interest Rate: \t{} %\n".format(float(apr)))

    interest_adder = 0.0
    print("Balance\tPayments Remaining\tInterest\tTotal Interest")

    while loan_amount - monthly_payment > 0.0:
        def print_all(loan_amount, total_payments, total_interest, cum_interest):

            if loan_amount - monthly_payment < 0:
                print("{:.2f}".format(loan_amount), "\t{}".format(total_payments), "\t${:.2f}".format(total_interest), "\t${:.2f}".format(round(interest_adder,2)))
                # print("Balance: ${}".format(loan_amount), "\tPayments Remaining: {}".format(total_payments), "\tInterest: ${}".format(total_interest), "\tTotal Interest: ${}".format(interest_adder))
                final_payment = loan_amount - loan_amount
                print("${:.2f}".format(final_payment), "\t".format(total_payments - 1), "\t${:.2f}".format(total_interest), "\t${:.2f}".format(round(interest_adder,2)))
                # print("Balance: ${}".format(final_payment), "\tPayments Remaining: {}".format(total_payments - 1), "\tInterest: ${}".format(total_interest), "\tTotal Interest: ${}".format(interest_adder))
            else:
                print("${:.2f}".format(loan_amount), "\t{}".format(total_payments), "\t${:.2f}".format(round(total_interest,1)), "\t${:.2f}".format(round(interest_adder,2)))
                # print("Balance: ${}".format(loan_amount), "\tPayments Remaining: {}".format(total_payments), "\tInterest: ${}".format(total_interest), "\tTotal Interest: ${}".format(interest_adder))

        total_payments = total_payments - 1

        def loan_balance(loan_amount, apr, monthly_payment):
            mon_int_rate = (apr * .01) / MONTHS_PER_YEAR
            monthly_interest = mon_int_rate * float(loan_amount)
            to_principal = monthly_payment - monthly_interest
            loan_balance = loan_amount - to_principal
            return loan_balance

        total_interest = interest(loan_amount, apr, monthly_payment)
        interest_adder = round(interest_adder,2) + round(total_interest,2)
        loan_amount = loan_balance(loan_amount, apr, monthly_payment)

        print_all(round(loan_amount, 2), total_payments, round(total_interest, 2), round(interest_adder, 2))

ammortize(other_total, 5, 8.0)
