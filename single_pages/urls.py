from django.urls import path
from . import views 

urlpatterns = [
    path('about_me/', views.about_me), # 내가 함수 두 개 만들겠다라는 의미
    path('', views.landing),
    
]