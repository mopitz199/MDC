from django.db import models

class Trade(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='tradePics')
