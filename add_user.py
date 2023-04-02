import os
def user_name() :
    confirm ='N'
    while confirm !='Y':
        username = input("Enter the name of the user: ")
        print("use the username '" + username + "'?(Y/N)")
        confirm = input().upper()
    os.system("sudo adduser "+ username)
user_name()