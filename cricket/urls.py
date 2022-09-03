from django import views
from django.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'cricket', views.CricketViewSet, basename='cricket')
router.register(r'terrarium', views.TerrariumViewset, basename='terrarium')

urlpatterns = []
urlpatterns += router.urls
