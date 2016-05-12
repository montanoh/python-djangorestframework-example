from django.db import models

class Record(models.Model):

    id = models.AutoField(primary_key=True)

    date = models.DateTimeField(auto_now=True, auto_now_add=True)

    gid = models.CharField(max_length=100)

    tag = models.CharField(max_length=100)

    note = models.CharField(max_length=100)

    money = models.FloatField()
