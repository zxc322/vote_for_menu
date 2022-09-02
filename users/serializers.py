from rest_framework import serializers

from .models import ExtendedUser


class CreateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtendedUser
        fields = [
            'username',
            'password',
            'email',
        ]

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
