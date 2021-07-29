from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    scientific_name = serializers.CharField()


class CharacteristicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    # animal_list = serializers.
