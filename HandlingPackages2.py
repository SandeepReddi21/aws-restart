    # prompt user to input a list of packages to install or remove, or use default packages
    print("Enter a list of packages to install")
    print("The list should be separated by spaces, for example:")
    print(" package1 package2 package3")
    print("Otherwise, input 'default' to " + iOrR + " the default packages listed in this program")
    packages = input().lower()

    # set packages to default packages if user inputs 'default'
    if packages == "default":
        packages = defaultPackages

    # use apt-get command to install or remove packages based on user input
    if iOrR == "install":
        os.system("sudo apt-get install " + packages)