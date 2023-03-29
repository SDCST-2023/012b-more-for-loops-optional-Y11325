#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]
guesses = 0

for i in range(3):
    guesses += 1
    names = input("Enter your username: ")
    pw = input("Enter your password: ")
    if names not in users or pw not in passwords:
        print("\nThe username or password you have entered does not exist!")
        continue
    elif names in users and pw in passwords:
        int(users.index(names))
        int(passwords.index(pw))
        if names == pw:
            print("\nAccess Granted!\n\n")
            break
        elif names != pw:
            print("\nWrong username or password!")
            if guesses == 3:
                print("\nAccess Denied\nYOUR ACCOUNT IS LOCKED\n\n")
                break
