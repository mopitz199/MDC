from .models import *
from rest_framework import serializers

class PushNotificationTokenCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushNotificationToken
        fields = ('key',)

class PushNotificationTokenListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushNotificationToken
        fields = '__all__'
