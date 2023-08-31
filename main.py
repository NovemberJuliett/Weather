import requests

url_template = "https://wttr.in/{}"
response_svo = requests.get(url_template.format("svo"))
response_london = requests.get(url_template.format("london"))
print(response_svo.text, response_london.text)


url_ru = "https://wttr.in/Череповец?lang=ru&?q&?T&?n&?M&?m"
response_new_cherepovets = requests.get(url_ru)
print(response_new_cherepovets.text)
