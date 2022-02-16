from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name="home"),
    path('job/<int:id>', views.detail, name="detail"),
]
