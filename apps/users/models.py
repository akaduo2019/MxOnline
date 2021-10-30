# users/models.py

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

'''系统自定义生成的user表中字段如下:
  id: 主键, 
  password 密码, 
  last_login Django自动记录用户最后登录时间,
  is_superuser 表明用户是否是超级用户(后台管理会用到),
  username 用户名字段不要随便改动, 
  email 邮箱,
  is_staff 表示是否是员工(后台管理会用到),
  is_active 用户是否是激活状态, 
  date_joined 注册时间。
对于网站用户信息来说是不够的，因此需要通过AbstractUser来拓展user表'''


class UserProfile(AbstractUser):

    gender_choices = (
        ('male', '男'),
        ('female', '女')
    )

    nick_name = models.CharField('昵称', max_length=50, default='')
    birthday = models.DateField('生日', null=True, blank=True)
    gender = models.CharField('性别', max_length=10, choices=gender_choices, default='female')
    adress = models.CharField('地址', max_length=100, default='', null=True, blank=True)
    mobile = models.CharField('手机号', max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y%m', default='image/default.png', max_length=100)

    class Meta:
        # 定义在后台管理显示的名称
        verbose_name = '用户信息'
        # 定义复数时的名称(去除默认情况下带的复数s)
        verbose_name_plural = verbose_name

    # 调用时返回自身的属性，不然都是显示xx object
    def __str__(self):
        return self.username


# 邮箱验证码
class EmailVerifyRecord(models.Model):
    send_choices = (
        ('register', '注册'),
        ('forget', '找回密码'),
        ('update_email', '修改邮箱')
    )

    code = models.CharField('验证码', max_length=20)
    email = models.EmailField('邮箱', max_length=50)
    send_type = models.CharField(choices=send_choices, max_length=30)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    title = models.CharField('标题', max_length=100)
    # image表示上传到哪里
    image = models.ImageField('轮播图', upload_to='banner/%Y%m', max_length=100)
    # url表示图片的路径
    url = models.URLField('访问地址', max_length=200)
    # index控制轮播图的播放顺序
    index = models.IntegerField('顺序', default=100)
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

