from django.db import models

# Create your models here.

# Admin后台站点
class Clazz(models.Model):
    con=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=30,unique=True)

    def __unicode__(self):
        return self.cname

    class Meta:
        db_table='t_cls'

class Student(models.Model):
    son=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30,unique=True)

    def __unicode__(self):
        return self.sname

    class Meta:
        db_table='t_student'


