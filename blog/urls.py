from django.urls import path
from . import views # 현재 디렉토리 안에서 import

urlpatterns = [
    path('<int:pk>/', views.single_post_page), 
    # url주소/pk(작성된 문서의 순서)/들어오면 view의 single_post_page로 가겠다.
    path('', views.index), #views 에서 내가 필요한 것을 띄우
]