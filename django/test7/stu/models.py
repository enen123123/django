from django.db import models

# Create your models here.
class Goods(models.Model):
    goodsid=models.AutoField(primary_key=True)
    gname=models.CharField(max_length=30)
    gdesc=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    count=models.PositiveIntegerField()
    created=models.DateField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    gimg=models.ImageField(upload_to='image/')  #图片文件存储自动在image下



# _创建单表
# . BooleanField真假
# . NullBooleanField Null，真假，
# . lnteger 整数
# . PositivelntegerField 正整数
# . DecimalField max_digits(几位数) decimal_places (小数点后保留几位)
# . lmageField图片依赖于Pillow(处理图片)upload_to='upload'指定文件上传到目录·
# . FileField(ImageField继承FileField)
# . AutoField
# . ForeignKey 1:n
# . ManyToManyField n:n. EmailField邮箱
# .UUIDField 重复的概率非常低基本可以忽略;全世界都不一样的标示，uuid的产生和服务器的环境有关(CPU网关，)唯一性的标示，用户模块，订单号
# ·不同的字段在后台对应不同的html的组件
#    ImageField依赖于Pillow组件(python库)
#   常用属性
# . unique标示这个字段唯一
# . default默认的意思，(如果不写的话就使用默认的值)
# . null=True 允许字段为null，(允许数据库为null)数据库层面的.
# . blank=True表单阶段的，admin后台的
# . auto now针对时间的，自动调整当前，(当修改条目的时候，这个时间会自动更新)，每次修改都会更新（修改，保存的时候才会生效，)
# . auto now add十对时间的、只添加—次.(创建的时间)
#
