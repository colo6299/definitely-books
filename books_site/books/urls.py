from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.Home.as_view(), name='home'),
    path('book/<int:pk>', views.Detail.as_view(), name='detail')

]