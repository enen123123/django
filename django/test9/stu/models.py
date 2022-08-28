from django.db import models

# Create your models here.



class Clazz(models.Model):
    cno=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=30)

    class Meta:
        db_table='t_clazz'

    def __unicode__(self):
        return u'Clazz:%s'%self.cname

class Course(models.Model):
    courseno=models.AutoField(primary_key=True)
    coursename=models.CharField(max_length=30)

    class Meta:
        db_table='t_course'

    def __unicode__(self):
        return u'Course:%s'%self.coursename

class Student(models.Model):
    sno=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=30)
    cls=models.ForeignKey(Clazz,on_delete=models.CASCADE)
    course=models.ManyToManyField(Course)

    class Meta:
        db_table='t_student'

    def __unicode__(self):
        return u'Student:%s'%self.sname

def insertstu(sname,cname,coursenames):
    # 注册
    try:
        # 插入班级数据
        try:
            cls = Clazz.objects.get(cname=cname)
        except Clazz.DoesNotExist:
            cls = Clazz.objects.create(cname=cname)
        # 插入学生数据
        try:
            stu = Student.objects.get(sname=sname)
        except Student.DoesNotExist:
            stu = Student.objects.create(sname=sname,cls=cls)
        # 插入课程数据
        courselist=[]
        for cn in coursenames:
            try:
                course = Course.objects.get(coursename=cn)
            except Course.DoesNotExist:
                course = Course.objects.create(coursename=cn)
            courselist.append(course)
        # 插入学生课程中间表
        stu.course.add(*courselist)
        return True
    except:
        return False



