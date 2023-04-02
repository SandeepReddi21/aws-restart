def update_environment():
    # Update the package list
    os.system("sudo apt-get update")
    # Upgrade all packages to their latest versions
    os.system("sudo apt-get upgrade")
    # Upgrade to the latest available version of Ubuntu
    os.system("sudo apt-get dist-upgrade")
