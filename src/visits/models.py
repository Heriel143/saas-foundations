from django.db import models


# Create your models here.
class PageVisits(models.Model):
    # db table to store page visits
    # id is automatically created
    path = models.TextField(blank=True, null=True)  # path of the visited page
    timestamp = models.DateTimeField(auto_now_add=True)  # time of the visit
