from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password','first_name','last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangeProfileSerializer(serializers.Serializer):
    new_username = serializers.CharField(required=False,allow_blank=True)
    new_email = serializers.CharField(required=False,allow_blank=True)
    new_first_name = serializers.CharField(required=False,allow_blank=True)
    new_last_name = serializers.CharField(required=False,allow_blank=True)

    def update(self, instance, validated_data):
        if 'new_username' in validated_data:
            instance.username = validated_data['new_username']
        if 'new_email' in validated_data:
            instance.email = validated_data['new_email']
        if 'new_first_name' in validated_data:
            instance.first_name = validated_data['new_first_name']
        if 'new_last_name' in validated_data:
            instance.last_name = validated_data['new_last_name']
        
        instance.save()
        return instance
    
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
