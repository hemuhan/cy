#-*- coding: UTF-8 -*-
from django.db import models
from member.models import Member
# Create your models here.
# 基本属性
class BaseProperty(models.Model):
    name = models.CharField(u'名称',max_length=20)
    order = models.IntegerField(u'排序',max_length=5,default=0)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name
#菜式
class Style(BaseProperty):
    class Meta:
        verbose_name = u'菜式'
        verbose_name_plural = u'菜式列表'
    pass
# 菜系
class Cuisine(BaseProperty):
    class Meta:
        verbose_name = u'菜系'
        verbose_name_plural = u'菜系管理'
    pass

# 烹饪方法
class CookingMethod(BaseProperty):
    class Meta:
        verbose_name = u'烹饪方法'
        verbose_name_plural = u'烹饪方法管理'
    pass

#口味
class Flavor(BaseProperty):
    class Meta:
        verbose_name = u'口味'
        verbose_name_plural = u'口味管理'
    pass

#场合
class Occasion(BaseProperty):
    class Meta:
        verbose_name = u'场合'
        verbose_name_plural = u'场合管理'
    pass

#菜单
class Product(models.Model):
    name = models.CharField(u'名称',max_length=100)
    style = models.ForeignKey(Style,verbose_name=u'菜式')
    cuisine = models.ForeignKey(Cuisine,verbose_name=u'菜系')
    cooking_method = models.ForeignKey(CookingMethod,verbose_name=u'烹饪方法')
    flavor = models.ManyToManyField(Flavor,verbose_name=u'口味')
    occasion = models.ManyToManyField(Occasion,verbose_name=u'场合')
    price = models.DecimalField(u'价格',max_digits=10,decimal_places=2)
    member_price = models.DecimalField(u'会员价',max_digits=10,decimal_places=2)
    preferential_price = models.DecimalField(u'优惠价',max_digits=10,decimal_places=2)
    thumb = models.ImageField(u'封面图片')
    description = models.TextField(u'描述')

    class Meta:
        verbose_name = u'菜'
        verbose_name_plural = u'菜管理'
        pass

        # app_label = u'菜列表'
    def __unicode__(self):
        return self.name
    def flavorList(self):

        return "," .join([e.name for e in self.flavor.all()])
    flavorList.short_description = u'口味'
#菜单的图片样式
class Pics(BaseProperty):
    pid = models.ForeignKey(Product)
    img = models.ImageField(u'图片')

#对菜的评论
class Vote(BaseProperty):
    pid = models.ForeignKey(Product)
    title = models.CharField(u'标题',max_length=100)
    content = models.TextField(u'内容')
    create_time = models.DateTimeField(u'创建时间',auto_now=True)
    useful_num = models.IntegerField(u'评论对我有用',default=0)
    unuseful_num = models.IntegerField(u'评论对我没有',default=0)
    member = models.ForeignKey(Member,verbose_name=u'评论者')