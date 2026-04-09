from search_advice import search_advice, parse_api_advice_response, display_number_results, browse_slips
from api_client import get_advice, get_joke, get_quote, display_joke, display_advice, display_quote
from menu_options import print_inspiration_menu, print_main_menu, print_intro, print_overview

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

        if not ask_repeat("search advice slips using a keyword"):
            return



def ask_repeat(prompt = ""):
    """
    Ask if user wants to repeat the action
    :param prompt:
    :return:
    """
    #todo prompt en false/true
    while True:
        again = input(f"\nDo you want to repeat the action: \033[4m{prompt}\033[0m? (y/n): ")
        if again in ['y', 'yes']:
            return True
        elif again in ['n', 'no']:
            return False
        else:
            print("\nInvalid input. Please enter 'y' or 'n'.")



def inspiration_loop():
    while True:
        print_inspiration_menu()

        try:
            choose_inspiration = int(input("Please choose an option: "))

            match choose_inspiration:
                case 1:
                    display_joke(get_joke())

                case 2:
                    display_quote(get_quote())

                case 3:
                    display_advice(get_advice())

                case 4:
                    advice_search_loop()

                case _:
                    print(f'\033[31mInvalid choice.\033[0m Please choose between options 1 - 4. ')

            if not ask_repeat("choose words of inspiration"): # end menu cycle - ask if want to repeat
                return

        except ValueError as e:
            print(f"\033[31mInvalid input\033[0m - error: {e} \nPlease enter a digit.\n")



def main():
    print_intro()

    while True:
        print_main_menu()

        try:
            choose_main = int(input("Please choose an option: "))
            if choose_main == 1:
                print(f'\nGreat!\n')
                inspiration_loop()

            elif choose_main == 3:
                print_overview()

            elif choose_main == 4:
                print(f'Quiting program')
                break

            else:
                print(f'\033[31mInvalid choice.\033[0m Please choose between options 1 - 4. \n')

        except ValueError as e:
            print(f"\033[31mInvalid input\033[0m - error: {e} \nPlease enter a digit.\n")


if __name__ == "__main__":
    main()
