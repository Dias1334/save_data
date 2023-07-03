from django.shortcuts import render
import requests

# Create your views here.
def current_wind(request):
    json_weather = requests.get('https://feelweather.click/api/astana').json()
    wind = json_weather['current']['wind_kph']

    return render(request, 'wind.html', {'wind': wind})



def qwerty(request):
    return render(request, '123.html')
