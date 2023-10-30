import helpperikirjasto

def main():
    while True:
        print("Choose what you want to do:")
        print("1) Generate voluteer work list.")
        print("2) Exit program.")

        choice = input("\nYour choice: ")
        
        print("Your choice was {0}, executing".format(choice))
        if choice == "1":
            data = []
            data = helpperikirjasto.generate_volunteer_list()
            helpperikirjasto.print_all_volunteers(data)
        elif choice == "2":
            break
        
    return 0

main()

