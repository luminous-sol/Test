from django.db import models
import os

# 함수를 사용하는 방법과 class 를 사용하는 방법

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    
    class Meta :
        verbose_name_plural = 'Categories'
        
class Tag(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=200, unique=True, allow_unicode= True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}'


class Post(models.Model): # 클래스 방식
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)
    # 이미지를 저장하지 않고 
    file_upload = models.FileField(upload_to='blog/filess/%Y/%m/%d', blank=True)
    # 파일 업로드하기
    
    create_at = models.DateTimeField(auto_now_add=True)
    # 시간이 자동으로 들어감
    updated_at = models.DateTimeField(auto_now=True)
    # 시간이 자동으로 업데이트 됨
    
    
    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'    
        
    def get_file_name(self):
        return os.path.basename(self.file_upload.name) 
    # 경로 불러오는 것 
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
    # 경로 제외한 파일명 나타내는 것
    
    # 오브젝트로 나오던 것을 오브젝트가 아닌 입력한 제목으로 나오게 변경
    
    # 현재 가입된 것 하나밖에 없으니까 
    # author : 추후 작성 예저
    
    # models 작업 후에는 꼭 필수적으로 migrate를 해야한다. 
    
