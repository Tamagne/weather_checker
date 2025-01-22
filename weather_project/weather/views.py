import requests
from django.shortcuts import render

def weather_home(request):
    weather_data = {}
    city = request.GET.get('city')  # Get the city from the user's input
    if city:
        api_key = 'your_openweathermap_api_key'
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(base_url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data = {"error": "City not found"}
    
    context = {
        'weather_data': weather_data,
        'city': city,
    }
    return render(request, 'weather/weather_home.html', context)
