def install_or_remove_packages():
    iOrR = ""
    while iOrR != "I" and iOrR != "R":
        print("Would you like to install or remove packages? (I/R)")
        iOrR = input().upper()
    if iOrR == "I":
        iOrR = "install" #Checks whether the user wants to install or remove packages
    elif iOrR == "R":
        iOrR = "remove"
