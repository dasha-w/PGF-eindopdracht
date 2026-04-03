from search_advice import search_advice, parse_api_advice_response, display_number_results, browse_slips

def run_advice_search():
    """
    Handles 1 search for advice slips
    - asking for keyword
    - fetching data from api
    - parses data
    - browses results (one or more)

    :return:
    """
    print("\n ----- Search for Advice -----\n")
    keyword = input("You are about to search for advice based on a keyword.\n"
                    "What keyword do you want to search for?: ").lower()

    if not keyword:
        print("Keyword cannot be empty.")
        return

    # get api data
    api_data = search_advice(keyword)

    # parse api data
    parsed = parse_api_advice_response(api_data)

    # If no advice found with keyword
    if not parsed['found']:     # if not False = True | If not True = False
        print(f'No advice found: {parsed['error']}')
        #fall_back("advice") #todo yay or nay?
        return

    # if there is advice found for the keyword
    slips = parsed['slips']

    #display number of slips found
    display_number_results(len(slips))

    # Show slips
    browse_slips(slips)

def advice_search_loop():
    """
    Handles loop for multiple searches of advice slips
    :return:
    """
    while True:
        run_advice_search()

        while True:
            again = input("\nDo you want to search again for advice slips using a keyword? (y/n): ")
            if again in ['y', 'yes']:
                break
            elif again in ['n', 'no']:
                return
            else:
                print("\nInvalid input. Please enter 'y' or 'n'.")

def print_intro():
    print(f'----------------------------------------------------------\n'
          f'Good morning! \nWelkom to the start-day application!\n'
          f'\nThis application is here to help you get a good start to your day.\n'
          f'How are you feeling this morning?\n')

def print_main_menu():
    print(f'What would you like to do?\n'
          f'---------------------------------------\n'
          f'1. Get some words to start your day\n'
          f'2. Get the weather forcast\n')


def print_words_menu():
    print(f"\nGreat!\n"
          f"These are your options: \n"
          f"---------------------------\n"
          f"1. Hear a (good) joke\n"
          f"2. Get a famous quote\n"
          f"3. Get some advice\n"
          f"4. Search advice by a keyword\n")

def main():
    print_intro()
    print_main_menu()

    choose_main = int(input("Please choose an option: "))
    if choose_main == 1:
        print_words_menu()

        choose_words = int(input("Please choose an options: "))
        match choose_words:
            case 4:
                advice_search_loop()
            #todo case 1,2,3,_


if __name__ == "__main__":
    main()