from rest_framework import serializers

from . models import adminLogin, viewstudent, userreport, leaveapproval, attendencecount, gradingsys


class loginadminSerializer(serializers.Serializer):
    class Meta:
        model = adminLogin
        fields = '__all__'

class viewstuSerializer(serializers.Serializer):
    class Meta:
        model = viewstudent
        fields = '__all__'

class reportSerializer(serializers.Serializer):
    class Meta:
        model = userreport
        fields = '__all__'

class leaveSerializer(serializers.Serializer):
    class Meta:
        model = leaveapproval
        fields = '__all__'

class attendenceSerializer(serializers.Serializer):
    class Meta:
        model = attendencecount
        fields = '__all__'

class gradingSerializer(serializers.Serializer):
    class Meta:
        model = gradingsys
        fields = '__all__'
