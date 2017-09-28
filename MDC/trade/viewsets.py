from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.decorators import list_route
from .models import *
from trade.serializers import *

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=['get'])
    def getCurrentUser(self, request):
        user = request.user
        serializer_context = {'request': Request(request),}
        serializer = UserSerializer(user, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    @list_route(methods=['get'])
    def getOtherUsers(self, request):
        user = request.user
        otherUsers = User.objects.all().exclude(id=user.id)
        serializer_context = {'request': Request(request),}
        serializer = UserSerializer(otherUsers, many=True, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all().order_by('-ts')
    serializer_class = TradeSerializer
    filter_fields = ('user',)

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        data['user'] = user.pk
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @list_route(methods=['get'])
    def getStatistics(self, request):

        user = request.user

        fromDate = request.GET.get('from', None)
        toDate = request.GET.get('to', None)

        if not fromDate and not toDate:
            return Response({
                'error': 'Debe entregar una fecha desde y hasta'
                }, status=status.HTTP_400_BAD_REQUEST)

        resp = {'won': 0,'lost': 0}

        trades = Trade.objects.filter(user=user, date__lte=toDate, date__gte=fromDate)

        for trade in trades:
            resultAmmount = trade.getResultAmmount()
            if resultAmmount>0:
                resp['won']+=resultAmmount
            else:
                resp['lost']+=resultAmmount

        return Response(resp)
