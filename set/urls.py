
from django.urls import path

from .views import HomePageView,weatherPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
     path('weather/', weatherPageView.as_view(), name='weather')
]