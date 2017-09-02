from django.db import models
from django.contrib.auth.models import User

class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=False, null=True, upload_to='tradePics')
    enter = models.DecimalField(max_digits=8, decimal_places=2)
    profit = models.DecimalField(max_digits=8, decimal_places=2)
    stop = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(null=True)
    result = models.TextField(null=True)
    tradeType = models.TextField(null=True)
    time = models.TimeField(null=True)
