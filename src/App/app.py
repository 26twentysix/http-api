import requests

from config import APP_CONFIG


class App:
    __base_url: str
    __api_ver: str
    __key: str
    __lang: str

    def __init__(self):
        self.__base_url = APP_CONFIG['api_url']
        self.__api_ver = APP_CONFIG['ver']
        self.__key = APP_CONFIG['key']
        self.__lang = APP_CONFIG['lang']

    def __request_maker(self, method, params):
        return self.__base_url + self.__api_ver + '/' + method + '?key=' + \
               self.__key + '&' + params + '&lang=' + self.__lang

    def __weather_forecast(self, city, days):
        with requests.get(self.__request_maker('forecast.json', 'q=' + city + '&days=' + days)) as response:
            self.__beautiful_print(response.json())

    def __beautiful_print(self, response):
        print(self.__get_location_formatted(response['location']))
        for day in response['forecast']['forecastday']:
            print('')
            print(self.__get_day_forecast_formatted(day))

    def __get_location_formatted(self, location):
        return 'City: ' + location['name'] + '\nRegion: ' + location['region'] + '\nCountry: ' + \
               location['country'] + '\nLocal time: ' + location['localtime']

    def __get_day_forecast_formatted(self, day):
        return 'Forecast for: ' + day['date'] + \
               '\nSunrise: ' + day['astro']['sunrise'] + \
               '\nSunset: ' + day['astro']['sunset'] + \
               '\nMinimum temperature: ' + str(day['day']['mintemp_c']) + \
               '\nMaximum temperature: ' + str(day['day']['maxtemp_c']) + \
               '\nAverage temperature: ' + str(day['day']['avgtemp_c']) + \
               '\nChance of rain: ' + str(day['day']['daily_chance_of_rain']) + '%' + \
               '\nChance of snow: ' + str(day['day']['daily_chance_of_snow']) + '%' + \
               '\nSummary condition: ' + day['day']['condition']['text']

    def run(self):
        while True:
            print('Enter command:')
            command = input()
            match command:
                case 'help':
                    print('Available commands:\nhelp - get list of all commands\ninfo - get info about app'
                          '\nforecast - get weather forecast for next n days in city\nexit - stop app')
                case 'info':
                    print('This app outputs weather forecast for next N days (in range from 1 to 3) in city')
                case 'forecast':
                    print('Enter number of days of weather forecast:')
                    days = input()
                    while True:
                        if int(days) > 3 or int(days) < 1:
                            print('Days should be higher than 0 and lower than 4\nPlease, enter valid days:')
                            days = input()
                        else:
                            break
                    print('Enter city:')
                    city = input()
                    self.__weather_forecast(city, days)
                    print('')
                case 'exit':
                    print('Exiting app...')
                    exit(0)
                case _:
                    print('Unknown command\nEnter help to get list of available commands')
