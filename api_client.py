import requests

#todo error afvangen in sys.stderr

# -------------------- QUOTE -----------------------
def get_quote():
    """Fetch zen-quote from API. Returns None on failure."""
    url = "https://zenquotes.io/api/random"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f'Something went wrong. Status code: {response.status_code}')
            return None

    except requests.exceptions.RequestException as e:
        print(f'Error {e}')
        return None #todo klopt dat? idem get_advice()


def fall_back_quote():
    fall_back = ("I learned that courage was not the absence of fear, but the triumph over it. "
                 "The brave man is not he who does not feel afraid, but he who conquers that fear.\n"
                 "- Nelson Mandela")

    print(f'Printing fallback quote.\n'
          f'-------------------------\n'
          f'Your quote for today is: \n"{fall_back}"')


def display_quote(data):
    """ Display quote with null check."""

    if data is None:
        print(f'Unable to fetch new quote at this time.')
        fall_back_quote()
        return

    try:
        quote = data[0]["q"]
        author = data[0]["a"]
        print(f'------------------------'
              f'You quote for today is:\n'
              f'"{quote}"\n'
              f'- {author}')

    except (KeyError, TypeError) as e:
        print(f'Unexpected response format. Error: {e}')
        fall_back_quote()


#--------------------- ADVICE ----------------------
def get_advice():
    """Fetch advice from API. Returns None on failure."""
    url = 'https://api.adviceslip.com/advice'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            print(f'Something went wrong. Status code: {response.status_code}')
            return None

    except requests.exceptions.RequestException as e:
        print(f'Error {e}')
        return None


def display_advice(data):
    """ Display advice with null check."""

    if data is None:
        print(f'Unable to fetch new advice at this time.')
        fall_back_advice()
        return

    try:
        new_advice = data['slip']['advice']
        print(f'------------------------'
              f'You advice for today is:\n"{new_advice}"')

    except (KeyError, TypeError) as e:
        print(f'Unexpected response format. Error: {e}')
        fall_back_advice()


def fall_back_advice():
    fall_back = "Every journey begins with a single step."
    print(f'Printing fallback advice.\n'
          f'-------------------------\n'
          f'Your advice for today is: \n"{fall_back}"')


#main
#print(get_quote())
#advice = get_advice()
#display_advice(advice)
#fall_back_advice()
#test = get_advice()
#print(test['slip']['advice'])
#print(get_advice())



