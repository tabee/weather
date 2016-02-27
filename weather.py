#!/usr/bin/python

import requests
import json
import logging
import sys


class Weather():
    json_config_file = "config.json"
    api_url_openweathermap = "http://api.openweathermap.org/data/2.5/"
    format = False
    weather_service_api_key = False
    city = False
    country = False
    temperature = False
    temperature_description = False
    filename = False

    def __init__(self, city, country):
        # read json_config_file file
        json_data = open(self.json_config_file).read()
        setting_data = json.loads(json_data)
        # set config vars
        self.weather_service_api_key = setting_data[1]['api_key']
        self.format = setting_data[3]['format']
        self.filename = setting_data[5]['log_file']
        # set config from constructor, fallback to config.json
        if city == False:
            self.city = setting_data[3]['city']
        else:
            self.city = city
        if country == False:
            self.country = setting_data[3]['country_code']
        else:
            self.country = country
        # set weather_data
        self.temperature = self.set_temperature(self.city, self.country)
        self.temperature_description = self.set_temperature_description(self.city, self.country)


    def __str__(self):
        return self.city + ', ' + str(self.temperature) + ', ' + self.temperature_description

    def __set_city_weather_JSON__(self, city=city, county=country):
        '''
        JSON weather data of a city.
        '''

        city_code = city + "," + county
        url_api_query = self.api_url_openweathermap + "weather?q=" + city_code + "&units=" + self.format + "&appid=" + self.weather_service_api_key
        try:
            data = requests.get(url_api_query).json()
        except:
            print('Fehler! Verbindung nicht möglich. Programm wird beendet.')
            return sys.exit()
        return data

    def set_temperature(self, city=city, country=country):
        """
        Asks openweather for the temperature of a city in a specific country.
        """
        data = self.__set_city_weather_JSON__(city, country)
        weather_data = data['main']
        return weather_data['temp']

    def set_temperature_description(self, city=city, country=country):
        """
        sets for this object the description of the weather.

        :arg:
            city und country
        :returns:
            clear sky, few clouds, scattered clouds, broken clouds, shower rain, rain, thunderstorm, snow or mist
        :raise

        """
        data = self.__set_city_weather_JSON__(city, country)
        weather_data = data['weather'][0]
        # print(weather_data)
        return weather_data['description']


if __name__ == '__main__':
    pass