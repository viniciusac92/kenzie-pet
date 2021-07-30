from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pet_shop.models import Animal, Characteristic, Group
from pet_shop.serializers import (
    AnimalCharacteristicSerializer,
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
        animals = Animal.objects.all()

        serialized = AnimalCharacteristicSerializer(animals, many=True)

        return Response(serialized.data)

    def post(self, request):
        serializer = AnimalCharacteristicSerializer(data=request.data)

        if not serializer.is_valid():
            import ipdb

            ipdb.set_trace()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data

        group = validated_data.pop('group')

        characteristics = validated_data.pop('characteristics')

        import ipdb

        ipdb.set_trace()

        animal = Animal.objects.get_or_create(**serializer.validated_data)[0]

        serializer = AnimalCharacteristicSerializer(animal)

        return Response(serializer.data)


class AnimalRetrieveView(APIView):
    def get(self, _, animal_id=''):
        if animal_id:
            try:
                animal = Animal.objects.get(id=animal_id)
                serialized = AnimalCharacteristicSerializer(animal)
                return Response(serialized.data)

            except ObjectDoesNotExist:
                return Response({'message': 'Id not found'})
