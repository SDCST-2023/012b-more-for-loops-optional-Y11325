#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = "systemadmin"
expectedPassword = "master"
guesses = 0
for i in range(3):
    guesses += 1
    x = input("\n\nEnter your username: ")
    y = input("Enter your password: ")
    if x == expectedUsername and y == expectedPassword:
        print("\nAccess Granted!\n\n")
        break
    elif x != expectedUsername or y != expectedPassword:
        print("\nWrong username or password!")
        if guesses == 3:
            print("\nAccess Denied\nYOUR ACCOUNT IS LOCKED\n\n")