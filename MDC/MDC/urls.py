"""MDC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.models import User
from trade.models import *

from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views

from django.conf import settings
from django.conf.urls.static import static

from trade.viewsets import *
from push_notification.viewsets import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'trades', TradeViewSet)
router.register(r'push_notification', PushNotificationTokenViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/generateRecoveryCode/$', GenerateRecoveryCode.as_view()),
    url(r'^api/validateRecoveryCode/$', ValidateRecoveryCode.as_view()),
    url(r'^api/changePassword/$', ChangePassword.as_view()),

    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
