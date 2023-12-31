from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
    thumbnail_image = serializers.ImageField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "middle_name",
            "email",
            "image",
            'thumbnail_image',
            "type_user",
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        instance.set_password(password)
        instance.save()
        return super().update(instance, validated_data)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = get_user_model().objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
