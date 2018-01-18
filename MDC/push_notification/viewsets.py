from .models import *
from .serializers import *
from rest_framework import viewsets

class PushNotificationTokenViewSet(viewsets.ModelViewSet):

    queryset = PushNotificationToken.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return PushNotificationTokenListSerializer
        if self.action == 'create':
            return PushNotificationTokenCreateSerializer
        if self.action == 'retrieve':
            return PushNotificationTokenListSerializer
        if self.action == 'update':
            return PushNotificationTokenListSerializer
        if self.action == 'partial_update':
            return PushNotificationTokenListSerializer
        if self.action == 'destroy':
            return PushNotificationTokenListSerializer
        return PushNotificationTokenListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
