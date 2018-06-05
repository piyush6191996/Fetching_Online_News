from . import views
from django.urls import path

app_name = 'news_api_urls'

urlpatterns = [
    path('test', views.test, name='test'),
]