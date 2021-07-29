from django.urls import path

from .views import AnimalView, CharacteristicView, GroupView

urlpatterns = [
    path('group', GroupView.as_view()),
    path('characteristic', CharacteristicView.as_view()),
    path('animal', AnimalView.as_view()),
]
