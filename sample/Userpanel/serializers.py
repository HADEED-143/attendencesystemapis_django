from rest_framework import serializers

from . models import Userrecord, UserMark, ViewMark


class UserRecSerializer(serializers.Serializer):
    class Meta:
        model = Userrecord
        fields = '__all__'

class UserMarksSerializer(serializers.Serializer):
    class Meta:
        model = UserMark
        fields = '__all__'

class marksviewSerializer(serializers.Serializer):
    class Meta:
        model = ViewMark
        fields = '__all__'

