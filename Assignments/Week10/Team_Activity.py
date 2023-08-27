'''
01- Create two lists, one for the names of the bank accounts, and one for the balances.
Ask the user for the name of the bank account and then for it's current balance. 
Keep looping until the user types "quit" for the name of an account. For each one, 
add the name and the balance to the appropriate list.
'''
# create variables
account_list = []
account_balance = []
end_loop = ''

while end_loop != 'quit':
    account_name = input(
        'What is the name of the bank account you want to create: \n').capitalize()
    account_list.append(account_name)
    balance = float(input('How much money is in that account? \n'))
    account_balance.append(balance)
    end_loop = input(
        'Press "Enter" to create another account.  Otherwise type "quit": \n').lower()
print()
print('Account Information: ')
for i in range(len(account_list)):
    print(
        f'{account_list[i]} \t${account_balance[i]:,.2f}')
print()

# calculate totals
grand_total = 0.00
for i in range(len(account_balance)):
    grand_total += account_balance[i]

average_balance = grand_total/len(account_balance)

print(
    f'Grand Total: \t${grand_total:,.2f}\nAverage: \t${average_balance:,.2f}')

max_amount = 0.00
# STRETCH CHALLENGE
for balance in account_balance:
    if balance > max_amount:
        max_amount = balance

print(max_amount)

for i in range(len(account_list)):
    print(f'{i}. {account_list[i]} - ${account_balance[i]:,.2f}')

ans = ''
while ans != 'no':
    ans = input('Would you like to update an account (Yes/No): ').lower()
    if ans == 'yes':
        index = int(input('What if the index of the account?'))
        new_account_name = input('What is the new account name? ')
        account_list[index] = new_account_name
        new_account_balance = float(input('What is the updated amount?'))
        account_balance[index] = new_account_balance

for i in range(len(account_list)):
    print(f'{i}. {account_list[i]} - ${account_balance[i]:,.2f}')
