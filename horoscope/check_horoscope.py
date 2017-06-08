#!user/bin/python3
import requests

def check_horoscope(sign=""):
    horoscopes = ['virgo', 'aries', 'leo', 'taurus', 'sagittarius', 'gemini',
                  'cancer', 'pisces', 'capricorn', 'libra', 'scorpio',
                  'aquarius']
    if type(sign) != str or not sign or sign.lower() not in horoscopes:
        return False
    url = 'http://sandipbgt.com/theastrologer/api/horoscope/{}/today'
    req = requests.get(url.format(sign.lower()))
    horoscope = req.json()['horoscope']
    print(horoscope)
