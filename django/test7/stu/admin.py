from django.contrib import admin

# Register your models here.
from stu.models import Goods

admin.site.register(Goods)


# python manage.py migrate  牵引所有
#python manage.py createsuperuser   创建超级用户
# Username (leave blank to use '86187'): admin
# Email address: hello@163.com
# Password:
# Password (again):

