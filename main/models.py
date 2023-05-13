from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=64,
                                verbose_name="이름")
    usercode = models.CharField(max_length=128,
                                  verbose_name="학번")
    userclass = models.CharField(max_length=128,
                                  verbose_name="과목")
    usergrade = models.CharField(max_length=64,
                                verbose_name="학점")
    registered_dttm = models.DateField(auto_now_add=True,
                                       verbose_name="등록시간")

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"
        verbose_name = "대학생활"
        verbose_name_plural = "대학생활"