from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pet_shop.models import Animal, Characteristic, Group
from pet_shop.serializers import AnimalCharacteristicSerializer


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

        animal_create_data = Animal(
            name=validated_data['name'],
            age=validated_data['age'],
            weight=validated_data['weight'],
            sex=validated_data['sex'],
            group=group_create_data,
        )
        animal_create_data.save()

        animal_create_data.characteristics_related.set(charac_list)

        serializer = AnimalCharacteristicSerializer(animal_create_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AnimalRetrieveView(APIView):
    def get(self, _, animal_id):
        if animal_id:
            try:
                animal = Animal.objects.get(id=animal_id)
                serialized = AnimalCharacteristicSerializer(animal)
                return Response(serialized.data)

            except ObjectDoesNotExist:
                return Response(
                    {'message': 'Id not found'}, status=status.HTTP_404_NOT_FOUND
                )

    def delete(self, _, animal_id):
        if animal_id:
            try:
                animal = get_object_or_404(Animal, id=animal_id)
                animal.delete()

                return Response(status=status.HTTP_204_NO_CONTENT)

            except ObjectDoesNotExist:
                return Response(
                    {'message': 'Id not found'}, status=status.HTTP_404_NOT_FOUND
                )
