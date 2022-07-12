from django.contrib import admin
from blog.models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','modify_dt','tag_list')
    list_filter=('modify_dt',)#필터사이드바
    search_fields=('title','content')#타이틀과 콘텐츠 검색하는 필드
    prepopulated_fields={'slug':('title',)}#slug는 title을 통해 생성

    def get_queryset(self,request):
        return super().get_queryset(request).prefetch_related('tags')#prefetch_related -- NN관계에서 쿼리 횟숙성능을 높임
    
    def tag_list(self,obj):
        return ','.join(o.name for o in obj.tags.all())