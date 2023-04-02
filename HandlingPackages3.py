elif iOrR == "remove":
    while True:
        # prompt user if they want to purge files after removing the packages
        print("Purge files after removing? (Y/N)")
        choice = input().upper()
        if choice == "Y":
            # remove packages and purge files
            os.system("sudo apt-get --purge " + iOrR + " " + packages)
            break
        elif choice == "N":
            # remove packages without purging files
            os.system("sudo apt-get " + iOrR + " " + packages)
            break
    # run autoremove to remove any unused packages
    os.system("sudo apt autoremove")
