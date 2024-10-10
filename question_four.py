#Qn4. WITI Academy is proposing a SACCO to help students save their money.
# Design a platform that will do the following.
# Welcome to, WITI Academy SACCO.
# 1. Deposit money
# 2. Withdraw money
# 3. Check balance
# Ensure if the student selects 1, money is deposited and the minimum deposit should be 1000.
# If the students select 2, money should be withdrawn and a minimum withdrawal is 500.
# If the student select 3, the account balance should be displayed.
balance = 0
print("Welcome to WITI Academy SACCO")
print("\nPlease choose an option")
print("1. Deposit Money ")
print("2. Withdraw Money ")
print("3. Check Balance ")

choice = input("Enter your choice (1/2/3): ")
if choice == '1':
    amount = float(input("Enter amount to deposit: "))
    if amount >= 1000:
        balance += amount
        print(f"Successfully deposited {amount}. New balance is: {balance}.")
    else: 
        print("Minimum balance to deposit is 1000")
elif choice == '2':
    amount = float(input("Enter amount to withdraw: "))
    if amount >= 500:
         balance == amount
         print(f"Successfully withdrew {amount}. New balance is: {balance}.")
    else:
            print(" Minimum withdrawal amount is 500.")
elif choice == '3':
    print(f"Your current balance is: {balance}")
else:
    print("Invalid choice")
