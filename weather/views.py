import requests
from django.shortcuts import render

# Create your views here.
def home(request):
    api_key = "bdfd8d2deca36550b33f7c3dcd280007" # Your api_key
    city = "Tokyo"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    data = response.json() # Get data of json

    context = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "desc": data["weather"][0]["description"],
    }

    return render(request, "weather/home.html", context)