from rest_framework import serializers
from apps.users.models import User


# serializers.Serializer
# serializers.ModelSerializer

class UserModelSerializer(serializers.ModelSerializer):
    # password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        # fields='__all__'  #偷懒的做法
        fields = ['id', 'username', 'email', 'mobile', 'password']
