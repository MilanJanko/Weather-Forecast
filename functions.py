import keys
import requests

api_key = keys.api_key


def get_data(place, days=None, option=None):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    filtered = data['list']
    days_value = days * 8
    filtered = filtered[:days_value]
    dates = [dictionary['dt_txt'] for dictionary in filtered]
    if option == 'Temperature':
        filtered = [dictionary['main']['temp'] for dictionary in filtered]
    elif option == 'Sky Conditions':
        filtered = [dictionary['weather'][0]['main'] for dictionary in filtered]
    return dates, filtered


if __name__ == '__main__':
    print(__name__)
