from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('weather-forecast/', WeatherView.as_view(), name='weather-forecast'),
    path('api/weather-forecast/', WeatherForecastAPIView.as_view(), name='weather-forecast-api')
]