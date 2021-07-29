from rest_framework.response import Response
from rest_framework.views import APIView

from pet_shop.models import Group
from pet_shop.serializers import GroupSerializer


class KenziePetView(APIView):
    def get(self, request):
        group = Group.objects.all()

        serialized = GroupSerializer(group, many=True)

        return Response(serialized.data)
