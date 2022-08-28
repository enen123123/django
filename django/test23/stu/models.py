from django.db import models

# Create your models here.

# inspectdb menu    可以直接获得已知表的代码

class Menu(models.Model):
    areaid = models.IntegerField(primary_key=True)
    areaname = models.CharField(max_length=255, blank=True, null=True)
    parentid = models.IntegerField(blank=True, null=True)
    arealevel = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        # 该表不需要替换
        managed = False
        db_table = 'menu'

