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
from django.core.cache import cache
import random
from .utils import *
from rest_framework import permissions
from rest_framework.views import APIView


class GenerateRecoveryCode(APIView):

    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    """
    Function to generate a code to use it to recover your password
    """
    def post(self, request):
        email = request.data['email'] if 'email' in request.data else None
        print(email)
        code = ''.join(random.choice('0123456789ABCDEF') for i in range(6))
        res = cache.set(code, email, timeout=60*60*24) # 1 day
        print(res)
        if res and User.objects.filter(email=email).exists():
            msg = 'El codigo para recuperar su clave es: {}'.format(code)
            result = sendEmail(toEmail=email, sub='Codigo de recuperacion', msg=msg)
            if result[0]:
                return Response({'status': 'ok'}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'error': result[1]}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'error': u'No se pudo generar el codigo de recuperación'
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'ok'}, status=status.HTTP_202_ACCEPTED)


class ValidateRecoveryCode(APIView):

    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    """
    Function to validate your code and allow you to change your password
    """
    def post(self, request):
        code = request.data['code'] if 'code' in request.data else None
        val = cache.get(code)
        if val:
            resp = {
                'status': 'ok',
                'email': val
            }
            return Response(resp, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({
                'error': u'El codigo es invalido'
                }, status=status.HTTP_400_BAD_REQUEST)


class ChangePassword(APIView):

    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        code = request.data['code'] if 'code' in request.data else None
        email = request.data['email'] if 'email' in request.data else None
        password = request.data['password'] if 'password' in request.data else None
        repeatPassword = request.data['repeatPassword'] if 'repeatPassword' in request.data else None

        val = cache.get(code)
        if val and val==email and password and password==repeatPassword:
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            cache.delete_pattern(val)
            return Response({'status': 'ok'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response({
                'error': u'No se pudo cambiar la clave'
                }, status=status.HTTP_400_BAD_REQUEST)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    """
    Function to get the current user from an specific token
    """
    @list_route(methods=['get'])
    def getCurrentUser(self, request):
        user = request.user
        serializer_context = {'request': Request(request),}
        serializer = UserSerializer(user, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    """
    Function get all the other users in the system
    """
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
