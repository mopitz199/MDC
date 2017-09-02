from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
from django.contrib.auth.models import User
from .models import *
from trade.serializers import *

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        data['user'] = user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
