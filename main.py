import requests


def main():
    cities = [
        "SVO",
        "London",
        "Череповец"
    ]

    for city in cities:
        url_template = "https://wttr.in/{}"
        param = {"lang": "ru", "M": "", "m": "", "n": "", "q": "", "T": ""}
        response = requests.get(url_template.format(city), params=param)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
