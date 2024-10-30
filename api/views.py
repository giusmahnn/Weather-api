import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

# Create your views here.


class HomePageView(APIView):
    def get(self, request):
        return Response("<h1>Welcome to the weather forcast website</h1>")



# class WeatherForecastView(APIView):

#     def get(self, request, city_name):
#         api_key =  settings.WEATHER_API_KEY
#         base_url = "https://weatherapi-com.p.rapidapi.com/current.json?"
#         complete_url = f"{base_url}appid={api_key}&q={city_name}"
#         response = requests.get(complete_url)
#         if response.status_code == 200:
#             data = response.json()
#             main = data['main']
#             temperature = main['temp'] - 273.15  # Convert Kelvin to Celsius
#             humidity = main['humidity']
#             weather_desc = data['weather'][0]['description']
#             return Response(f"Temperature: {temperature:.2f}°C, Humidity: {humidity}%, Weather: {weather_desc}")



class WeatherForecastView(APIView):

    def get (self, request, city_name):

        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q":city_name}
        headers = {
            "x-rapidapi-key": "7074e65b8bmsh9bf6f0bc9fe366ap1a0f68jsn20ab025c4abf",
            "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
        }


        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
            data = response.json()
            print(data)

            return Response(data, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return Response(
                {"error": "Failed to fetch data from the weather service", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        