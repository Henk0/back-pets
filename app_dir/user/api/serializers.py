from rest_framework import serializers
from django.contrib.auth import get_user_model
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'is_staff',
            'phone',
            'photo'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        is_staff = validated_data['is_staff']
        phone = validated_data['phone']
        user_obj = User(
            username=username,
            email=email,
            is_staff=is_staff,
            phone=phone
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.photo = validated_data.get('photo', instance.email)
        instance.phone = validated_data.get('phone', instance.email)
        instance.save()

        return instance