import requests

WEATHER_SERVICE_API_URL = "http://api.openweathermap.org/data/2.5/"
WEATHER_SERVICE_API_KEY = "a06a5c8632cd9cacf412aa7a14658c28"
MODE = 'metric'  # metric (Grad) for europe or imperial for Fahrenheit.


def __get_city_weather_JSON__(city, county):
    '''
    JSON weather data of a city.
    '''

    city_code = city + "," + county
    url_api_query = WEATHER_SERVICE_API_URL + "weather?q=" + city_code + "&units=" + MODE + "&appid=" + WEATHER_SERVICE_API_KEY
    data = requests.get(url_api_query).json()
    return data


def get_metric_temperature(city, country):
    """
    Asks the openweather API for the metric temperature of a city in a specific country.
    """
    data = __get_city_weather_JSON__(city, country)
    weather_data = data['main']
    return weather_data['temp']


def get_description(city, country):
    """
    Brings you the description of the weather.
    Uses the get_metric_temperature() function.

    :arg:
        city und country
    :returns:
        clear sky, few clouds, scattered clouds, broken clouds, shower rain, rain, thunderstorm, snow or mist
    :raise

    """
    data = __get_city_weather_JSON__(city, country)
    weather_data = data['weather'][0]
    # print(weather_data)
    return weather_data['description']


def main(city, country):
    temperature = get_metric_temperature(city, country)
    description = get_description(city, country)

    print('Weather information for ' + city + ':')
    print('temperature: ' + str(temperature) + " C")
    print('description: ' + str(description) + ".")


if __name__ == '__main__':
    main('Bern', 'CH')
