from django.conf.urls import patterns, include, url
from api.views import Record
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'records', Record)

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       )
