from django.urls import path

from .views import KenziePetView

urlpatterns = [path('pet_shop', KenziePetView.as_view())]
