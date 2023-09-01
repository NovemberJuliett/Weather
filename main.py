import requests


def main():
    cities_list = [
        "SVO",
        "London",
        "Череповец"
    ]

    for i in cities_list:
        url_template = "https://wttr.in/{}"
        response = requests.get(url_template.format(i))
        response.raise_for_status()
        print(response.text)

    cherepovets_param = \
        {"?lang=": "ru", "?M": "", "?m": "", "?n": "", "?q": "", "T": ""}
    response_new_cherepovets = \
        requests.get("https://wttr.in/Череповец", params=cherepovets_param)
    response_new_cherepovets.raise_for_status()
    print(response_new_cherepovets.url)


if __name__ == '__main__':
    main()
