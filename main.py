import requests

url = 'https://wttr.in/san%20francisco?nTqu&lang=en%20HTTP/1.1'
response = requests.get(url)
response.raise_for_status()
print(response.text)

url_template = "https://wttr.in/{}"
response1 = requests.get(url_template.format("svo"))
response2 = requests.get(url_template.format("cherepovets"))
response3 = requests.get(url_template.format("london"))
print(response1.text, response2.text, response3.text)

url_ru = "https://wttr.in/Череповец?lang=ru&?q&?T&?n&?M&?m"
response4 = requests.get(url_ru)
print(response4.text)
