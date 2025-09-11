from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = (
            'name',
            'email',
            'password',
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user