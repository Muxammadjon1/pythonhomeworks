password=input("Please enter the password:")

if len(password)<8:
    print("The password is short")
elif password==password.lower():
    print('Password must contain an uppercase letter')
else:
    print("The password is strong")
    
