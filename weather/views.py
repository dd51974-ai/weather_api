import requests
import os
from django.shortcuts import render
from dotenv import load_dotenv
load_dotenv()

# Create your views here.
def home(request):
    context = {}

    if request.method == 'POST': # When user submits the form
        city = request.POST.get('city')

        if not city:
            context["error"] = "Please type a city name"
        else:
            api_key = os.environ.get("OPENWEATHER_API_KEY")
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

            try:
                response = requests.get(url)
                data = response.json()

                print("STATUS:", response.status_code) # Debug
                print("TEXT", response.text)

                if response.status_code == 200:
                    context = {
                        "city": data.get("name"),
                        "country": data.get("sys", {}).get("country"), # For example "JP", "US"
                        "temp": data.get("main", {}).get("temp"),
                        "humidity": data.get("main", {}).get("humidity"),
                        "desc": data.get("weather", [{}])[0].get("description"),
                        "icon": data.get("weather",[{}])[0].get("icon"), # Weather icon
                    }
                else:
                    context["error"] = "City not found"
            except requests.exceptions.RequestException:
                context["error"] = "API request failed"

    return render(request, "weather/home.html", context)


