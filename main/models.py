from django.db import models

class Network(models.Model):
    STATUS_CHOICES = [
        ('cracked', 'Cracked'),
        ('not_cracked', 'Not Cracked'),
        ('pending', 'Pending'),
    ]

    essid = models.CharField(max_length=25)
    bssid = models.CharField(max_length=25)
    password = models.CharField(max_length=50, null=True, blank=True, default="")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="not_cracked")
    file = models.FileField(null=True)
