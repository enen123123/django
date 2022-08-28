from django.apps import AppConfig


class StuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stu'
#更改app应用名   加入__init__.py
    verbose_name=u'学生应用'
