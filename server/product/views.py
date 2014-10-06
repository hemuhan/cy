#-*- coding: UTF-8 -*-

from django.shortcuts import render
from models import Style,Vote,Flavor,Pics,Cuisine,Occasion,Product,CookingMethod
# Create your views here.
from django.core import serializers
from django.http import HttpResponse
#获取所有菜式
def getStyle(request):
    data = Style.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type="application/json")

#获取所有烹饪方法
def getCookingMethod(request):
    data = CookingMethod.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type="application/json")

#获取所有菜系
def getCuisine(request):
    data = Cuisine.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type="application/json")

#获取所有口味
def getFlavor(request):
    data = Flavor.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type="application/json")

#获取所有场合
def getOccasion(request):
    data = Occasion.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type="application/json")


def getProduct(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type="application/json")
