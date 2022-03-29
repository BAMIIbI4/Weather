import requests


weather_in_cities = {
    'London': 'm1nTF',
    'Шереметьево': 'm1nTF&lang=ru',
    'Череповец': 'm1nTF&lang=ru'
}
url_template = 'https://wttr.in/{}?{}'

for city, options in weather_in_cities.items():
    url = url_template.format(city, options)
    response = requests.get(url)
    if not response.ok:
        raise requests.exceptions.HTTPError(response=response)
    print(response.text)
