from django.urls import path

from .views import AnimalRetrieveView, AnimalView

urlpatterns = [
    path('animals/', AnimalView.as_view()),
    path('animals/<int:animal_id>/', AnimalRetrieveView.as_view()),
]
