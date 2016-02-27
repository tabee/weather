#!/usr/bin/python

import requests
import helper
import json

WEATHER_SERVICE_API = "http://api.openweathermap.org/data/2.5/"
MODE = 'metric'  # metric (Grad) for europe or imperial for Fahrenheit.


def __get_city_weather_JSON__(city, county):
    '''
    JSON weather data of a city.
    '''

    city_code = city + "," + county
    url_api_query = WEATHER_SERVICE_API + "weather?q=" + city_code + "&units=" + MODE + "&appid=" + weather_service_api_key
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


def test(city, country):
    temperature = get_metric_temperature(city, country)
    description = get_description(city, country)

    print('Weather information for ' + city + ':')
    print('temperature: ' + str(temperature) + " C")
    print('description: ' + str(description) + ".")


if __name__ == '__main__':
    # read config.json file
    json_data = open("config.json").read()
    data = json.loads(json_data)
    # set config vars
    weather_service_api_key = data[1]['api_key']
    city = data[3]['city']
    country = data[3]['country_code']
    filename = data[5]['log_file']
    # get data from openweather
    description = get_description(city, country)
    temperatur = get_metric_temperature(city, country)
    # print console ...
    print(description + ' in ' + city + ' (' + str(temperatur) + ' C)')
    #save stuff
    persist_string = description + ", " + str(temperatur)
    helper.writeData(filename, persist_string, city)
