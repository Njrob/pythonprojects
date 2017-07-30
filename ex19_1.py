def money_for_a_house(savings, income):
    print "So you want to buy a new house. Great!"
    print "You currently have %d in your savings." % savings
    print "And you make %d a year, according to our records." % income
    loan = int(raw_input("How large of a loan would you like? "))
    monthly_payment = loan / 12
    interest_rate = .6 / 12
    amortization = monthly_payment * .6 * 30
    print "You will be paying %d dollars a month at an interest rate of %r, and you will have to pay off %d." % (
    monthly_payment, interest_rate, amortization)

money_for_a_house(150000, 40000)

savings_amount = 100000
income_amount = 35000

money_for_a_house(savings_amount, income_amount)
