#defines a Python function add_user_to_group that allows a user to add an existing user to one or more groups on the system.
def add_user_to_group():
    # Takes the name of the user that you want to work with
    username = input("Enter the name of the user that you want to add to a group: ")

    #Takes the name of the user that you want to work with
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0]

    #Takes the name of the user that you want to work with
    print("Enter a list of groups to add the user to")
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3")
    print("The available groups are:\r\n " + output)
    # Ask the user to enter a list of groups to add the user to
    chosenGroups = str(input("Groups: "))
