from django.contrib import admin
from .models import Album,Photo

class PhotoInline(admin.StackedInline):
    ##외래키 연결된 모델을 같이보여줌 : StackedInline, Tabularinline
    model=Photo
    extra=2

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines=(PhotoInline,)
    list_display=('id','name','description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display=('id','title','upload_dt')

