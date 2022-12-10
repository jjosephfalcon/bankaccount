''''
PS11 Project 1: Bank Account
Program a Bank Account program, as shown in the graphic below! Write out pseudocode in your code comments to plan out the program flow and data structures you'll need to set up. (Note: Make sure the user can log back into their account after they log out!)

'''


 
# Get username and password
# Greet user and tell them their balance 

# What would you like to do?
# make a deposit
# withdrawl
# change password
# logout 


print("-----------------Welcome to the bank program!------------------")




username = input("what is your username? ")
password = input("what is your password ")

balance = 0

program_running = True

while program_running == True:
  print(f"""
  welcome {username}, your current balance is [ {balance} ].What would you like to do?
  What would you like to do?
      1) Make a deposit
      2) Make a withdrawl
      3) Change password
      4) Logout
  

  """)

  choice = input("Pick 1-4: ")


  if choice == '1':
    amount = int(input("How much would you like to deposit? "))
    if amount > 100000:
      print("Thats too much money to deposit at once!")

    balance += amount

# HOMEWORK:
# for choice 2 , is withdraw a string or integer? Must be int to add or subtract from balance.
  if choice == '2':
    amount = int(input("How much would you like to withdraw? "))
    if amount > 1000000:
      print("Sorry, that amount is over the withdrawl limit!")
      # How to make sure there is enough money in balance to take out?
    elif amount > balance:
      print("you dont have enough money")
    else:
      balance -= amount  

# For choice 3: Remember the password is saved inside of the password variable at the start of program...to change it, ask user for a new password and set the old one equal to the new password. ex: old_pw = new_pw 
 
  if choice == '3':
    # Ask user what their password is before changing it to a new one. 
    old_pass =  input("What is your old password? ")
    # Check if old_pass matches password
    if old_pass == password:
      # Ask user for what the new_pass will be: 
      new_pass = input("What is going to be your new password? ")
      # Change the value of password to equal new_pass 
      password = new_pass
      print("You password has been changed!")
    else:
      print("_____________________NO__________________________")

  
  
  
# Choice 4: if users picks logout use the program_running variale to end loop.
 
  if choice == '4':
    print("you are logged out thank you for leaving you were a terrible customer! ")
    program_running = False









































































































































































































