#-*- coding: UTF-8 -*-
from django.contrib import admin
from models import Product,Pics,Vote
from models import Style,Cuisine,CookingMethod,Flavor,Occasion
class VoteInline(admin.StackedInline):
    model = Vote
    extra = 1

class PicInline(admin.StackedInline):
    model = Pics
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','style','cuisine','flavorList','price')
    list_filter = ('style',)
    search_fields = ('name',)
    inlines = [PicInline,VoteInline]

admin.site.register(Product,ProductAdmin)
admin.site.register((Style,Cuisine,CookingMethod,Flavor,Occasion))
# Register your models here.
