from rest_framework.response import Response
from rest_framework.views import APIView

from pet_shop.models import Animal, Characteristic, Group
from pet_shop.serializers import (
    AnimalSerializer,
    CharacteristicSerializer,
    GroupSerializer,
)


class GroupView(APIView):
    def get(self, _):
        group = Group.objects.all()

        serialized = GroupSerializer(group, many=True)

        return Response(serialized.data)


class CharacteristicView(APIView):
    def get(self, _):
        characteristic = Characteristic.objects.all()

        serialized = CharacteristicSerializer(characteristic, many=True)

        return Response(serialized.data)


class AnimalView(APIView):
    def get(self, _):
        animal = Animal.objects.all()

        serialized = AnimalSerializer(animal, many=True)

        return Response(serialized.data)
