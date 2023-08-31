import requests
import logging

cities_list = [
    "SVO",
    "London",
    "Череповец"
]


def request_weather():
    for i in cities_list:
        url_template = "https://wttr.in/{}"
        response = requests.get(url_template.format(i))
        response.raise_for_status()
        return response.text


def request_otherweather():
    for i in cities_list:
        url_template = "http://wttr.dvmn.org//{}"
        response = requests.get(url_template.format(i))
        response.raise_for_status()
        return response.text


try:
    forecast = request_weather()
except requests.exceptions.ConnectionError:
    forecast = request_otherweather()


cherepovets_param = {"?lang=": "ru", "?M": "", "?m": "", "?n": "", "?q": "", "T": ""}
response_new_cherepovets = requests.get("https://wttr.in/Череповец", params=cherepovets_param)
response_new_cherepovets.raise_for_status()
print(response_new_cherepovets.url)





