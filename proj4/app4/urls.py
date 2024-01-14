from django.conf.urls import url
from app4 import views
app_name = 'app4'


urlpatterns = [
    url(r'^relative/', views.relative, name="relative"),
    url(r'^other/', views.other, name="other"),
]