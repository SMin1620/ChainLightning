from django.db import models
from django.shortcuts import resolve_url
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    first_name = None
    last_name = None
    date_joined = None

    name = models.CharField('이름', max_length=50)
    charge_cost = models.PositiveIntegerField('충전된 금액', default=0)
    reg_date = models.DateTimeField('생성 날짜', auto_now_add=True)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return f'{self.id}, {self.username}, {self.name}, {self.charge_cost}'