from . import views
from django.urls import path
app_name = 'my_app'

urlpatterns = [
    path('',views.home, name="home"),
]