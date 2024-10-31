import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

# Create your views here.


class HomePageView(APIView):
    def get(self, request):
        return Response("<h1>Welcome to the weather forcast website</h1>")
    


class WeatherView(APIView):

    def post(self, request):

        city_name = request.data.get('city_name', 'Lagos') # our parameter passed in the body

        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        querystring = {"q":city_name} # query string
        
        headers = {
            "x-rapidapi-key": "7074e65b8bmsh9bf6f0bc9fe366ap1a0f68jsn20ab025c4abf",
            "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
        } # info to our api client

        try:
            response = requests.get(url, headers=headers, params=querystring) # fetching the data
            
        except requests.exceptions.RequestException as e: # should an error occur
            return Response(
                {"error": "Failed to fetch data from the weather data", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        data = response.json()
        return Response(data, status=status.HTTP_200_OK) # returns the response
    



class WeatherForecastAPIView(APIView):
    def post(self, request):
        city_name = request.data.get("City_name", "Imo")
        #country = request.data.get('country', '')
        day = request.data.get("Day", 3)

        # Combine city and country if both are provided
        #location_query = f"{city_name}, {country}" if country else city_name

        url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
        querystrings = {"q":city_name, "days":day}
        headers = {
        	"x-rapidapi-key": "7074e65b8bmsh9bf6f0bc9fe366ap1a0f68jsn20ab025c4abf",
	        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
}
        

        try:
            response = requests.get(url, headers=headers, params=querystrings)

        except requests.exceptions.RequestException as e:     
            return Response(
                {"error": "Failed to fetch data from the weather forecast", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        data = response.json()
        return Response(data, status=status.HTTP_200_OK)