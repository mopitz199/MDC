from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=False, null=True, upload_to='tradePics')
    photoThumbnail = ImageSpecField(source='photo',
                                      processors=[ResizeToFill(100, 100)],
                                      format='JPEG',
                                      options={'quality': 60})

    enter = models.DecimalField(max_digits=8, decimal_places=2)
    profit = models.DecimalField(max_digits=8, decimal_places=2)
    stop = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(null=True)
    result = models.CharField(null=True, max_length=20)
    tradeType = models.CharField(null=True, max_length=20)
    time = models.TimeField(null=True)

    ts = models.DateTimeField(auto_now_add=True)
