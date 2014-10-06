__author__ = 'hemuhan'
from django.conf.urls import patterns, include, url
import views
urlpatterns = patterns(
    '',
    url('^getStyle$',views.getStyle),
    url('^getFlavor$',views.getFlavor),
    url('^prolist$',views.getProduct),
)