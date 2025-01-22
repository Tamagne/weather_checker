import requests
from django.shortcuts import render

def weather_home(request):
    city = request.GET.get('city', '')
    weather_data = {}

    if city:
        api_key = 'Yb9d45f04544c7c68e2cc82050454e952'  # Replace with your OpenWeatherMap API Key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data['error'] = "City not found. Please try again."

    context = {
        'city': city,
        'weather_data': weather_data,
    }
    return render(request, 'weather/weather_home.html', context)
