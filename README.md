# Weather

This code helps to check the weather right from the terminal.

## How to install

Python3 should already be installed. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```pip install requests```

## How to use

Code sample of the weather report for London, UK:

```url_template = "https://wttr.in/{}"``` <br/>
```response_london = requests.get(url_template.format("london"))```<br/>
```print(response_london.text)```