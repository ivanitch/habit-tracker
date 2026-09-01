from rest_framework import serializers

from users.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone', 'city', 'avatar']
        read_only_fields = ('email',)


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'phone', 'city', 'avatar']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
