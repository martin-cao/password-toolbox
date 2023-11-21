def main():
    print(" *********************************\n", "* Welcome to Password Generator *\n",
          "*********************************\n")
    mode = input("Which mode would you like to use?: \n 1. password strength checher \n 2. password generator\n").lower()

    match mode:
        case "1":
            print("Please wait for the module loading...")
            from checker import checker
            checker()
            doContinue = input("Do you want to continue(y/n)?: ").lower()
            match doContinue:
                case "y":
                    main()

        case "2":
            from generator import generate
            generate()
            print("\n")
            doContinue = input("Do you want to check the strength of the password  you just generated (1) or continue(2)?: ").lower()
            match doContinue:
                case "1":
                    from checker import checker
                    checker()
                case "2" :
                    main()

        case _:
            print("Invalid input. Please try again.")
            main()

if __name__ == "__main__":
    main()
