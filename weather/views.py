import requests
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}

    if request.method == 'POST': # When user submits the form
        city = request.POST.get('city')

        if not city:
            context["error"] = "Please type a city name"
        else:
            api_key = ""
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

            try:
                response = requests.get(url)
                data = response.json()

                print("STATUS:", response.status_code) # Debug
                print("TEXT", response.text)

                if response.status_code == 200:
                    context = {
                        "city": data.get("name"),
                        "temp": data.get("main", {}).get("temp"),
                        "desc": data.get("weather", [{}])[0].get("description"),
                    }
                else:
                    context["error"] = "City not found"
            except requests.exceptions.RequestException:
                context["error"] = "API request failed"

    return render(request, "weather/home.html", context)

