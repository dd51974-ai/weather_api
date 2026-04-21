import requests
from django.shortcuts import render

# Create your views here.
def home(request):
    city = None
    context = {}

    if request.method == "POST":  # When formed to type city somewher.
        city = request.POST['city']  # Enter to type city
        api_key = ""
        url = f"http:api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)


        data = response.json() # Get data of json

        if response.status_code == 200: # Result after being post
            context = {
                "country": data["sys"]["country"],
                "city": data["name"],
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"],
            }
    else: # spelling mistake
        context = {
            "error": "City not found"
        }

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    return render(request, "weather/home.html", context) # Return to "home.html" as a result