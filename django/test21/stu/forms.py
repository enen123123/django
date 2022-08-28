# 正则表达式
import re

from django import forms

# 查询时表单只需要继承forms.Form
from stu.models import Clazz, Student


class Loginform1(forms.Form):
    # label = ''    更改姓名标签
    username=forms.CharField(max_length=10,label='姓名')
    # widget=forms.PasswordInput    密码框显示方式
    password=forms.CharField(max_length=10,label='密码',widget=forms.PasswordInput)

# 增删改变时表单类需要继承forms.ModelForm
class Clazzform(forms.ModelForm):
    class Meta:
        model=Clazz
        fields=['cname']

class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields=['sname']

    # 自定义表单校验，clean_开头
    def clean_sname(self):
        sname=self.cleaned_data.get('sname','')
        # 正则表达式判断，需要模块re
        p=re.compile('^[A-Za-z]+$')
        if p.match(sname):
            return sname
        else:
            raise forms.ValidationError('格式错误，非英语字符',code='sname_invlid')



