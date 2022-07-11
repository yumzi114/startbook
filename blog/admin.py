from django.contrib import admin
from blog.models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','modify_dt')
    list_filter=('modify_dt',)#필터사이드바
    search_fields=('title','content')#타이틀과 콘텐츠 검색하는 필드
    prepopulated_fields={'slug':('title',)}#slug는 title을 통해 생성