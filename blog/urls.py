from django.urls import path
from . import views # 현재 디렉토리 안에서 import

urlpatterns = [
    path('create_post',views.PostCreate.as_view()),
    path('tag/<str:slug>/',views.tag_page),
    path('<int:pk>/',views.PostDetail.as_view()),
    path('',views.PostList.as_view()),
    # url주소/pk(작성된 문서의 순서)/들어오면 view의 single_post_page로 가겠다.
    # path('', views.index), #views 에서 내가 필요한 것을 띄우게 할 수 있다.
    # path('<int:pk>/', views.single_post_page),
    path('category/<str:slug>/',views.category_page),
    path('',views.PostList.as_view()),
]