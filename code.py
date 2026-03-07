#variables and constant
Bank_name=('digi bank')
Account_type=('current')
Min_req=(5000)
#user input
Name= str(input('Enter your full name: '))
Age= int(input('Enter your age: '))
Acc_num= int(input('Enter your 13 digit account number: '))
Balance= float(input('Enter your initial deposit amount: '))

#printing types of user input
print('\n')
print(type(Name))
print(type(Age))
print(type(Acc_num))
print(type(Balance))

# string methods
print('\n')
print('Name in uppercase:',Name.upper())
print('Num of char in name:' ,len(Name))

 # type casting
print('\n')
Acc_num_str= str(Acc_num)
print(type(Acc_num_str))
print('length of account number: ',len(Acc_num_str))
print('age after type casting',float(Age))
print(type(Age))

#list
print('\n')
print('Enter your last three transactions use (-) for withdrawls')
t1 = float(input('Enter first transaction amount: '))
t2 = float(input('Enter second transaction amount: '))
t3 = float(input('Enter third transaction amount: '))
Transactions = [t1, t2, t3]
print(Transactions)
Balance = Balance + t1 + t2 + t3
#tuple
Acc_types= ("Savings", "Current", "Fixed")

# dictionary
print('\n')
print('---Customer info---')
customer={'name': Name, 'age': Age, 'Acc_num':Acc_num, 'Balance': Balance}
print(customer)

#methematical operation
print('\n')
print('--- Transaction Summary ---')

print('Transactions:', Transactions)
interest = customer["Balance"] * 0.05
print('Interest amount:',interest)
#even odd
print('\n')
if int(Balance) % 2 == 0:
    print('Your balance is an Even number.')
else:
    print("Your balance is an Odd number.")

#conditional structures
print('\n')
if Balance >= 100000:
  print('Premium Account Holder')

elif Balance >= 50000:
  print('Gold Account Holder')

elif Balance >= 20000:
  print('Silver Account Holder')

else:
  print('Basic Account Holder')
  #LOOP
print('\n')
Password=input('Create a passoword :')
user_pass = input('Enter Password to Login: ')
while user_pass != Password:
    user_pass = input('Incorrect password try again: ')
print('Login Successfull')

print('\n')
print('--- Transaction Counter ---')
i = 1
while i <= 10:
    print('Transaction number:', i)
    i += 1
