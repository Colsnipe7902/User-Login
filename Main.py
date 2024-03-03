welcome_banner = """
                Welcome to User Login app!
"""

welcome = ("Welcome to MyFace")
username_input = input("Enter your username:")
password_input = input("Enter your password:")

if username_input == "codewizard42" :
    if password_input == "programmer_4ever" :
        print("Welcome back codewizard42!")
else :
    print("Your username or password was incorrect, please refresh and try again!")

if username_input == " " :
    print("Please type you username.") 
if password_input == " " :
    print("Please type you password.")
