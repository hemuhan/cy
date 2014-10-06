#-*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
# 会员系统
class Member(models.Model):
    username = models.CharField(u'用户名',max_length=50)
    password = models.CharField(u'密码',max_length=32)
    realname = models.CharField(u'真实姓名',max_length=50)
    mobile = models.CharField(u'手机号码',max_length=15)
    money = models.DecimalField(u'用户金额',max_digits=8,decimal_places=2)
    address = models.CharField(u'地址',max_length=500)
    lastip = models.IPAddressField(u'最后登录IP')
    last_time = models.DateTimeField(u'最后登录时间')

#会员登录记录
class Member_login_log(models.Model):
    member_id = models.ForeignKey(Member,verbose_name=u'所属会员')
    ip = models.IPAddressField(u'登录IP')
    time = models.DateTimeField(u'登录时间')


#会员浏览记录
class log(models.Model):
    member_id = models.ForeignKey(Member,verbose_name=u'所属会员')

