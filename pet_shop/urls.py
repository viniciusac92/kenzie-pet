from django.urls import path

from .views import CharacteristicView, GroupView

urlpatterns = [
    path('group', GroupView.as_view()),
    path('characteristic', CharacteristicView.as_view()),
]
