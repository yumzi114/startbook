from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.dates import ArchiveIndexView,YearArchiveView,MonthArchiveView
from django.views.generic.dates import DayArchiveView,TodayArchiveView
from blog.models import Post
# Create your views here.

class PostLV(ListView):
    model=Post
    template_name='blog/post_all.html'
    context_object_name='posts'#콘텐츠명, 기존 object_list도 사용가능
    paginate_by=2#한페이지 보여지는 객체리스트 해당 정의만으로 장고 페이징사용가능, 페이징활성화해야 에터에이블사용가능

class PostDV(DetailView):
    model=Post
    #모델에서  개체조회를 slug로 사용중

class PostAV(ArchiveIndexView):
    model=Post
    date_field='modify_dt'

class PostYAV(YearArchiveView):
    model=Post
    date_field='modify_dt'
    make_object_list=True #object list를 새로생성
    #month_format='%b' 디폴트값
class PostMAV(MonthArchiveView):
    model=Post
    date_field='modify_dt'
class PostDAV(DayArchiveView):
    model=Post
    date_field='modify_dt'
class PostTAV(TodayArchiveView):
    model=Post
    date_field='modify_dt'
