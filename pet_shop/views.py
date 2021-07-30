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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data

        group_request_data = validated_data.pop('group')
        group_create_data = Group.objects.get_or_create(**group_request_data)[0]

        characteristics = validated_data.pop('characteristics_related')
        charac_list = []

        for charac in characteristics:
            charac_prepared = Characteristic.objects.get_or_create(name=charac['name'])[
                0
            ]
            charac_list.append(charac_prepared)

        animal_create_data = Animal.objects.get_or_create(
            **validated_data, group=group_create_data
        )[0]
        animal_create_data.characteristics_related.set(charac_list)

        serializer = AnimalCharacteristicSerializer(animal_create_data)

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
