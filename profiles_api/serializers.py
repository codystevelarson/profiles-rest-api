from rest_framework import serializers
from .models import UserProfile, ProfileFeedItem


class HelloSerializer(serializers.Serializer):
    ''' Serializes a name field for testing the APIView '''
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    ''' Serializes a user profile object '''
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        # Set password to write only
        # Set password input as type password
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        ''' Create and return a new user '''
        # Override the create function
        user = UserProfile.objects.create_user(
            email=validated_data['email'], name=validated_data['name'], password=validated_data['password']
        )

        return user

    # Override update to hash password on update to not save plain text passwords
    def update(self, instance, validated_data):
        ''' Handle Updating user account '''
        # Check if password in request
        # Hash password if not none
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    ''' Serializes profile feed items '''
    class Meta:
        model = ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
