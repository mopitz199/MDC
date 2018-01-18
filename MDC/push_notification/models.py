from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PushNotificationToken(models.Model):
    key = models.CharField(blank=False, max_length=300, primary_key=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
