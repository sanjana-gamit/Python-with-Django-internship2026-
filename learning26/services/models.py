from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    discount = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name