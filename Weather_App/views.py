from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests
import datetime

load_dotenv()

def Get_Weather(request):
    city=""
    json={}
    problem="none"
    try:
        city=str(request.GET.get('city'))
        if city=='None':
            city='India'
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'
        key=os.getenv('API_KEY')
        result=requests.get(url.format(city,key))
        if result:
            json=result.json()
            problem="found"
        else:
            problem="not_found"
    except:
        problem="invalid"
    data=[]
    if len(json)!=0:
        date=datetime.date.today()
        data={
            'city':city,
            'lon':json['coord']['lon'],
            'lat':json['coord']['lat'],
            'main':json['weather'][0]['main'],
            'descripton':json['weather'][0]['description'],
            'icon':json['weather'][0]['icon'],
            'temp':json['main']['temp'],
            'feels_like':json['main']['feels_like'],
            'temp_min':json['main']['temp_min'],
            'temp_max':json['main']['temp_max'],
            'pressure':json['main']['pressure'],
            'humidity':json['main']['humidity'],
            'visibility':json['visibility'],
            'wind_speed':json['wind']['speed'],
            'wind_deg':json['wind']['deg'],
            'clouds':json['clouds']['all'],
            'country':json['sys']['country'],
            'sunrise':json['sys']['sunrise'],
            'sunset':json['sys']['sunset'],
            'date':date,
            'problem':problem,
        }
    else:
        data={
            'problem':problem,
        }
    return render(request, 'weather_app.html', data)
