'''
First, ask for a rating from 1–10 on the following:
How large is the loan?
How good is your credit history?
How high is your income?
How large is your down payment?
'''

# create the variables for the loan decision
loan_size = int(input('What is your loan size 1 - 10: '))
credit_history = int(input('How good is your credit history 1 - 10: '))
income = int(input('How large is your income 1 - 10: '))
down_payment = int(input('How large is your down payment 1 - 10: '))
loan_decision = False
# decision matrix for loan calculator
'''
First, check if the loan size is at least 5. If it is, use the following rules:
--If the credit history and income are both at least 7, then the decision is "yes"
--If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no"
--Otherwise (if neither the credit history nor income is at least 7), the decision is "no"
--Otherwise (if the loan is not 5 or greater), use these rules:
--If the credit is less than 4, then the decision is "no"
Otherwise, check the following:
--If either the income or the down payment is at least 7, the decision is "yes"
If both the income and the down payment are at least 4, then the answer is "yes"
Otherwise, the decision is "no"
'''

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        loan_decision = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            loan_decision = True
        else:
            loan_decision = False
    else:
        loan_decision = False
elif loan_size < 5:
    if credit_history < 4:
        loan_decision = False
    elif income >= 7 or down_payment >= 7:
        loan_decision = True
    elif income >= 4 and down_payment >= 4:
        loan_decision = True
else:
    loan_decision = False

if loan_decision:
    print("Loan approved!")
else:
    print("Loan denied!")
