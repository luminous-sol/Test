from django.db import models

# 함수를 사용하는 방법과 class 를 사용하는 방법

class Post(models.Model): # 클래스 방식
    title = models.CharField(max_length=30)
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
        
    
    # 오브젝트로 나오던 것을 오브젝트가 아닌 입력한 제목으로 나오게 변경
    
    
    # 현재 가입된 것 하나밖에 없으니까 
    # author : 추후 작성 예저
    
    # models 작업 후에는 꼭 필수적으로 migrate를 해야한다. 
    
