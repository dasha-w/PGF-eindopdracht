#--------------------- SEARCH ADVICE ----------------------
# keyword = 'happiness'
# url = f'https://api.adviceslip.com/advice/search/{keyword}'
# response = requests.get(url)
# print(response.json())


#main
#print(get_quote())
#advice = get_advice()
#display_advice(advice)
#fall_back_advice()
#test = get_advice()
#print(test['slip']['advice'])
#print(get_advice())
#fall_back("joke")
#print(get_joke())
#display_joke(get_joke())

def fall_back_quote():
    fall_back = ("I learned that courage was not the absence of fear, but the triumph over it. "
                 "The brave man is not he who does not feel afraid, but he who conquers that fear.\n"
                 "- Nelson Mandela")

    print(f'Printing fallback quote.\n'
          f'-------------------------\n'
          f'Your quote for today is: \n"{fall_back}"')

def fall_back_advice():
    fall_back = "Every journey begins with a single step."
    print(f'Printing fallback advice.\n'
          f'-------------------------\n'
          f'Your advice for today is: \n"{fall_back}"')
fall_back_advice()

def check_advice_found(api_data):
    """
    Function to check if the search for advice with a keyword has returned a message that NO advice with that keyword
    was found.
    :param api_data:
    :return: False if NO advice was found and the api_data contains the dictionary item 'message'
        True if the api_data does NOT contain 'message' and has therefore given advice slips with the keyword.
    """
    try:
        api_data['message'] # checks if message is in the api_data
        return False
    except KeyError as e:
        return True

def slips_dictionary(slips_list):
    slips_dict = {}

    for slip in slips_list:
        index = index(slip)
        slips_dict['index'] = slip

    return slips_dict

    def ask_user_to_continue():
        """
        Ask user if they want to see another slip.
        :return: True on yes, False if no
        """
        while True:
            again = input("\nWould you like to see another slip? (y/n): ").lower().strip()
            if again in ['y', 'yes']:
                return True
            elif again in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'.")

    # for i, advice in enumerate(advice_list,1):
    #     print(i)
    #     print(advice['advice'])

    # Display & interact with found api_data
    # display_number_results(len(parsed['slips']))
    # chosen = choose_advice(len(parsed['slips']))
    # display_advice(parsed['slips'][chosen])
# display_advice(data: parsed['slips'], index

# save slips


#print(check_advice_found(data))


# if 'message' in data:
#      #result = data.get('message')
#      result = data['message']['text']
#      print(result)

#print(data['message'])

#{'message': {'type': 'notice', 'text': 'No advice slips found matching that search term.'}}

# keyword = 'life'
# url = f'https://api.adviceslip.com/advice/search/{keyword}'
# response = requests.get(url)
# data = response.json()
#
# total_results = data['total_results']
# keyword = data['query']
# print(total_results)
# print(keyword)
#
# advice_list = data['slips']
# print(advice_list)
#
# def display_query_advice(data):
#
#
# for i, advice in enumerate(advice_list,1):
#     print(i)
#     print(advice['advice'])
# keyword = input("You are about to search for advice based on a keyword.\n"
#                 "What keyword do you want to search for?: ").lower()
#
# # get api data
# api_data = search_advice(keyword)
#
# # parse api data
# parsed = parse_api_advice_response(api_data)
# slips = parsed['slips']
# display_chosen_advice(slips, 0)
#print(slips[0])
#print(slips_dictionary(parsed['slips']))

#{'found': True, 'slips': [{'id': 215, 'advice': "Once you find a really good friend don't do anything that could mess up your friendship.", 'date': '2016-03-01'}], 'error': None}
#print(slips_dictionary(parsed))

    # for i, advice in enumerate(advice_list,1):
    #     print(i)
    #     print(advice['advice'])

    # display_number_results(len(parsed['slips']))
# for i, advice in enumerate(advice_list,1):
#     print(i)
#     print(advice['advice'])

#========================= weather=====================4
#print(parse_weather_api(get_weather_in_city())['weather'])
# def main():
#
#     try:
#         run_weather_city()
#
#         print(parsed['weather']['current'])
#
#     except KeyError as e:
#         print(f'Unexpected data structure: {e}')
#     except Exception as e:
#         print(f'Unexpected error occurred: {e}')

#main()