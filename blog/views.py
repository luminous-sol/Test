from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk' #순서대로 작성
    
    
#    template_name = 'blog/index.html'

class PostDetail(DetailView):
    model = Post
    


# from django.shortcuts import render
# from .models import Post
# # 현재 디렉토리에 있는 modesl에서 Post 불러옴

# def index(request): #함수방식
    
#     posts = Post.objects.all().order_by('-pk') 
#     # order_by('-pk') 최근 작성한 문서가 제일 위에 오도록
#     # DB Query 명령어 => DB에 있는 것 모두 가지고 오게 하는 명령어
    
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts':posts,
#         }
#     )
# #class Post() #클래스 방식 models.py

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk) # object 값 따라 가는 것 1번이면 1번 따라가고 2번이면 2번따라 가고...
    
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
#     )

# # Create your views here.
