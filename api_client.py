import requests

# -------------------- QUOTE -----------------------
def get_quote():
    """
    Fetch zen-quote from API. Returns None on failure.
    """
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


def display_quote(data):
    """ Display quote with null check.
    If data is None - fallback quote will be printend.
    If data has quote, the text is printed. If the data format gives an error - again fallback quote will be printen.
    """

    if data is None:
        print(f'Unable to fetch new quote at this time.')
        fall_back("quote")
        return

    try:
        quote = data[0]["q"]
        author = data[0]["a"]
        print(f'------------------------\n'
              f'You quote for today is:\n'
              f'"{quote}"\n'
              f'- {author}')

    except (KeyError, TypeError) as e:
        print(f'Unexpected response format. Error: {e}')
        fall_back("quote")


#--------------------- JOKE ----------------------
def get_joke():
    url = 'https://jokefather.com/api/jokes/random'

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


def display_joke(data):
    """ Display joke with null check.
    If data is None - fallback joke will be printend.
    If data has a joke, the text is printed. If the data format gives an error - again fallback joke will be printed.
    """

    if data is None:
        print(f'Unable to fetch new quote at this time.')
        fall_back("joke")
        return

    try:
        setup = data["setup"]
        punchline = data["punchline"]
        print(f'------------------------\n'
              f'You joke for today is:\n'
              f'{setup}\n'
              f'\n'
              f'{punchline}')

    except (KeyError, TypeError) as e:
        print(f'Unexpected response format. Error: {e}')
        fall_back("joke")



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
    """ Display advice with null check.
    If data is None - fallback advice will be printend.
    If data has advice, the text is printed. If the data format gives an error - again fallback advice will be printen.
    """

    if data is None:
        print(f'Unable to fetch new advice at this time.')
        fall_back("advice")
        return

    try:
        new_advice = data['slip']['advice']
        print(f'------------------------\n'
              f'You advice for today is:\n"{new_advice}"')

    except (KeyError, TypeError) as e:
        print(f'Unexpected response format. Error: {e}')
        fall_back("advice")


#--------------------- FALLBACK ----------------------
def fall_back(categorie):
    """
    Function for fallback advice, quote and joke in case None is returned in API functions.

    :param categorie: quote, advice, or joke. str
    :return: fallback message
    """
    fall_back_advice = '"Every journey begins with a single step."'
    fall_back_quote = ('"I learned that courage was not the absence of fear, but the triumph over it. '
                       'The brave man is not he who does not feel afraid, but he who conquers that fear."\n'
                       '- Nelson Mandela')
    fall_back_joke = ("What's a computer's favorite snack?\n"
                      "\n"
                      "Microchips")

    if categorie == 'advice':
        text = fall_back_advice
    if categorie == 'quote':
        text = fall_back_quote
    if categorie == 'joke':
        text = fall_back_joke

    print(f'Printing fallback {categorie}.\n'
          f'-------------------------\n'
          f'Your {categorie} for today is:\n'
          f'{text}')


