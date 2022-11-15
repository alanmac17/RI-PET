from . import views
from django.urls import path

urlpatterns = [
    path("", views.DeathNoticeList.as_view(), name="home"),
]