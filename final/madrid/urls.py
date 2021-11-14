from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('json', views.FootballView)
app_name = "madrid"
urlpatterns = [
    #path('', views.madrid_list, name='home'),
    path('<slug:slug>/squad', views.madrid_detail, name='detail'),
    path('', include(router.urls))

]