from rest_framework.response import Response
from rest_framework.views import APIView

from pet_shop.models import Characteristic, Group
from pet_shop.serializers import CharacteristicSerializer, GroupSerializer


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
