print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 4000









def option():
    balance = 4000
    options = input('What would you like to do? (deposit, withdraw, check_balance) \n')
    if options == 'deposit':
        deposit = input('How much would you like to deposit? \n')
        return balance + int(deposit)
    elif options == 'withdraw':
        withdraw = input('How much would you like to withdraw? \n')
        return balance - int(withdraw)
    elif options == 'check_balance':
        return balance

print(f"Your current balance is  ${option()}")

done = input('Are you done? \n')

if done == 'yes':
    print('Thank you!')
elif done == 'no':
    option()




