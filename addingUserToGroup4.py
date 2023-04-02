# Update the string to add a space instead of a comma
groupString = groupString[:-1] + " "

# Loop until user enters Y or N
confirm = “”
while confirm != "Y" and confirm != "N" :
    print("Add user '" + username + "' to these groups? (Y/N)")
    confirm = input().upper()

# If user enters N, do not add the user to any groups
if confirm == "N":
    print("User '" + username + "' not added")

# If user enters Y, add the user to the chosen groups using os.system command
elif confirm == "Y":
    os.system("sudo usermod -aG " + groupString + username)
    print(“User ‘” + username + ‘” added)

