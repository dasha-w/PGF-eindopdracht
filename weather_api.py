import requests

# ============ GET WEATHER DATA FROM API ============
def get_weather_in_city(city):
    """
    Get data from weather api. Returns weather data or None on failure
    :param city: city name string
    :return: json response OR None
    """

    API_KEY = "78ac60675ed0447482e100012260804"

    url = "http://api.weatherapi.com/v1/forecast.json?"
    params = {"key": API_KEY, "aqi": "no", "q":city}

    try:
        response = requests.get(url, params = params)
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f'Error {e}')
        return None
    except ValueError:
        print(f'Invalid JSON response from API')
        return None


#=============== PARSE WEATHER OUTPUT ===================
def parse_weather_api(weather_data):
    """
    Normalize API response into standard format
    :param weather_data: json from weather api
    :return: {'found': bool, 'weather': dict, 'error': None or str
    """
    result = {'found': False, 'weather': {}, 'error': None}

    if weather_data is None:
        result['error'] = 'No data received from API'

    elif 'error' in weather_data:
        result['error'] = weather_data.get('error',{}).get('message', 'Unknown API error')

    elif 'location' in weather_data and 'forecast' in weather_data:
        result['found'] = True
        result['weather'] = weather_data

    else:
        print(f'Unexpected API response structure: {weather_data}')
        result['error'] = 'Unexpected API response structure'

    return result


#============== GET INPUT CITY =================
def get_city():
    """
    Asks user for city name. Input cannot be empty
    :return: string
    """
    while True:
        city = input("Enter a city name to check the weather: ").strip()

        if not city:
            print("City name cannot be empty. Please enter a city name: ")
            continue

        return city


#=============== CONFIRM CITY INPUT =============
def check_city(weather_data):
    """
    From API data the location is shown.
    User is asked if the location is indeed the city the user wants the weather information for
    :param weather_data: parsed weather_data in dict
    :return: bool - True if confirmed, False if not
    """
    try:
        location = weather_data['location']
        print(f'Found {location['name']} in region: {location['region']} and country: {location['country']}\n')

        while True:
            correct_city = input(f'Is this the city you want to see the weather forecast for? (y/n): ')
            if correct_city in ['yes', 'y']:
                return True
            elif correct_city in ['n', 'nee']:
                return False
            else:
                print("\nInvalid input. Please enter 'y' or 'n'.")

    except KeyError as e:
        print(f'Missing expected data: {e}')
        return False


def run_weather_city():# todo naar main_app
    """
    runs 1 search for weather data

    :return: None if no data or not correct city
    """
    city = get_city() #ask user for city
    data = get_weather_in_city(city) #get data from api
    parsed = parse_weather_api(data) #parse data, None if api error, error city not found, or found en data

    if not parsed['found']:  # if not False = True | If not True = False
        print(f'No data found: {parsed['error']}')
        return

    elif not check_city(parsed['weather']): #found data & city - check if city is the one you want to see
        print(f'Asking for city again... \n')
        return


    #todo display


def weather_city_loop():
    while True:
        run_weather_city()

        # todo if not #repeat




city = get_city() #ask user for city
data = get_weather_in_city(city) #get data from api
parsed = parse_weather_api(data)
weather = parsed['weather']
print(weather)
print(check_city(data))
#

#print(weather['forecast']['forecastday'][0])

#----- extract current weather data =====
key_filters_current_weather = ['temp_c', 'condition', 'wind_kph', 'precip_mm', 'feelslike_c',"uv", "wind_dir",
                               'last_updated']

current_weather = {key: weather['current'][key] for key in key_filters_current_weather}
current_weather['condition'] = current_weather['condition']['text']

wind_dir_map = {
    'N': 'northern',
    'S': 'southern',
    'E': 'eastern',
    'W': 'western',
    'NE': 'northeastern',
    'NW': 'northwestern',
    'SE': 'southeastern',
    'SW': 'southwestern',
}
current_weather['wind_dir'] = wind_dir_map.get(current_weather['wind_dir'], current_weather['wind_dir']) #fallback

#----- extract forecast weather data ===
key_filters_forecast_weather = ['maxtemp_c', 'avgtemp_c', 'mintemp_c', 'totalprecip_mm', 'daily_will_it_rain',
                                'daily_chance_of_rain','condition', 'uv']
forecast_daily = weather['forecast']['forecastday'][0]['day']
forecast_weather = {key: forecast_daily[key] for key in key_filters_forecast_weather}
forecast_weather['condition'] = forecast_weather['condition']['text']

forecast_midday = weather['forecast']['forecastday'][0]['hour'][]

"""
temperature range day
for hour_dict in range(8,21):
    for key in key_filters:
        {key: forecast
"""
#todo terug implementeren

#----- display current ====
location = weather['location']

print(f'\n----------------------\n'
      f'The current weather in {location['name']}, {location['country']} at {current_weather['last_updated'][11:]} is:\n'
      f'Temperature: {current_weather['temp_c']}{chr(176)}C \n'
      f'Perceived temperature: {current_weather['feelslike_c']}{chr(176)}C \n'
      f'Precipitation: {current_weather['precip_mm']} mm\n'
      f'Wind: {current_weather['wind_kph']} kph in {current_weather['wind_dir']} direction\n'
      f'Condition: {current_weather['condition']}\n'
      f'')

#----- display forecast ====
print(f'\n--------------------------\n'
      f'The temperature today should be between {forecast_weather['mintemp_c']}{chr(176)}C '
      f'and {forecast_weather['maxtemp_c']}{chr(176)}C \n'
      f'The \u001b[1maverage\u001b[0m temperature today will be: {forecast_weather['avgtemp_c']}{chr(176)}C\n')

# print for temperature
if forecast_weather['avgtemp_c'] <= 10 and forecast_weather['maxtemp_c'] <= 10:
    print(f"It's going to feel cold today. Bundle up!")
elif forecast_weather['avgtemp_c'] <= 10 and forecast_weather['maxtemp_c'] > 10:
    print(f"")
elif 10 < forecast_weather['avgtemp_c'] < 15 :
    print(f"It'll occasionally be chilly today")

# print for different rain conditions
if forecast_weather['daily_will_it_rain'] == 0:
    if forecast_weather['daily_chance_of_rain'] > 0:
        print(f'It should not rain today. Although there is '
              f'a {forecast_weather['daily_chance_of_rain']} chance of rain.\n')
    elif forecast_weather['daily_chance_of_rain'] <= 0:
        print(f'It is not going to rain today.')
elif forecast_weather['daily_will_it_rain'] == 1:
    print("Consider carrying an umbrella as it's going to rain today.\n"
          f"The chance of rain is {forecast_weather['daily_chance_of_rain']} "
          f"with a total of {forecast_weather['totalprecip_mm']}mm rain.\n")


#print(forecast_weather)
#print(current_weather)
#uv = forecast['day']['uv']
#print(uv)
# regen - forecast mm, probability
# temp - max, average, current
#print(current_weather['last_updated'][11:])