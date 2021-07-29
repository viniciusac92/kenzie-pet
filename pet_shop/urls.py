from django.urls import path

from .views import AnimalRetrieveView, AnimalView, CharacteristicView, GroupView

urlpatterns = [
    path('group', GroupView.as_view()),
    path('characteristic', CharacteristicView.as_view()),
    path('animals', AnimalView.as_view()),
    path('animals/<int:animal_id>/', AnimalRetrieveView.as_view()),
]
