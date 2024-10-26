import functions as func

def main():

    properties = func.init_properties()

    user_input = None

    while user_input != "6":

        func.print_menu()

        user_input = input()

        match user_input:
            case "1" : 
                func.current_weather(properties)
            case "2" : pass
            case "3" : pass
            case "4" : pass
            case "5" : pass
            case "6" : break
            case _:
                print("\t\t\t=================================")
                print(f"\t\t\t==-----Invalid Input: <{user_input}>------==")
                print("\t\t\t=================================\n")
                
    
    print("\t\t\t=================================")
    print("\t\t\t==-----------Goodbye!----------==")
    print("\t\t\t=================================")


if __name__ == "__main__":
    main()