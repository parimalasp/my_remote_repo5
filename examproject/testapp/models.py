from django.db import models


class Employee(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=30)
    sal=models.FloatField()
    addr=models.CharField(max_length=30)
