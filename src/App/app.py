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
        pass

    def run(self):
        while True:
            print('Enter command:')
            command = input()
            match command:
                case 'help':
                    print('Available commands:\nhelp - get list of all commands\ninfo - get info about app'
                          '\nforecast - get weather forecast for next n days in city\nexit - stop app')
                case 'info':
                    print('This app outputs weather forecast for next N days (in range from 1 to 10) in city')
                case 'forecast':
                    print('Enter number of days of weather forecast:')
                    days = input()
                    while True:
                        if int(days) > 10 or int(days) < 1:
                            print('Days should be higher than 0 and lower than 11\n Please, enter valid days:')
                            days = input()
                        else:
                            break
                    print('Enter city:')
                    city = input()
                    self.__weather_forecast(city, days)
                case 'exit':
                    print('Exiting app...')
                    exit(0)
                case _:
                    print('Unknown command\nEnter help to get list of available commands')