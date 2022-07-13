from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView,CreateView,UpdateView,DeleteView
from django.views.generic.dates import ArchiveIndexView,YearArchiveView,MonthArchiveView
from django.views.generic.dates import DayArchiveView,TodayArchiveView
from blog.models import Post
from mysite import settings
#폼관련 import
from django.views.generic import FormView
from .forms import PostSearchForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

# Create your views here.

class PostLV(ListView):
    model=Post
    template_name='blog/post_all.html'
    context_object_name='posts'#콘텐츠명, 기존 object_list도 사용가능
    paginate_by=2#한페이지 보여지는 객체리스트 해당 정의만으로 장고 페이징사용가능, 페이징활성화해야 에터에이블사용가능

class PostDV(DetailView):
    model=Post
    #모델에서  개체조회를 slug로 사용중
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['disqus_short']=f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id']=f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url']=f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title']=f"{self.object.slug}"
        return context

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
###taggit 뷰class
##렌더링만하는 뷰, 클라우드처리기능이 html에 있음{%get_tagcloud%}
class TagCloudTV(TemplateView):
    template_name='taggit/taggit_cloud.html'

##컨텍스트 변수를 추가함
##URL패턴에서 self.kwargs['tag']로 추출
##tag/<str:tag>/,views.TaggerObjectLV.as_view(),name='tagged_objec_list'
class TaggedObjectLV(ListView):
    template_name='taggit/taggit_post_list.html'
    model=Post
    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['tagname']=self.kwargs['tag']
        return context

#####FORM VIEW########
class SearchFormView(FormView):
    #form으로 사용될 클래스 지정
    form_class=PostSearchForm
    template_name='blog/post_search.html'
    #유효성검사후 form_valid 실행됨
    def form_valid(self,form):
        #form.py에 필드명 검사된 데이터를 받음
        searchWord=form.cleaned_data['search_word']
        #검색기능 Q클래스,distinct 중복제거
        post_list=Post.objects.filter(Q(title__icontains=searchWord)|Q(description__icontains=searchWord)|Q(content__icontains=searchWord)).distinct()
        context={}
        context['form']=form
        context['search_term']=searchWord
        context['object_list']=post_list
        #form객체,검색단어,검색결과 오브젝트
        return render(self.request,self.template_name,context)

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','slug','description','content','tags']
    initial={'slug':'auto-filling-do-not-input'}
    #fields=['title','description','content','tags']
    success_url=reverse_lazy('blog:index')
    def form_valid(self,form):
        form.instance.owner=self.request.user
        return super().form_valid(form)

class PostChangeLV(LoginRequiredMixin,ListView):
    template_name='blog/post_change_list.html'
    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model=Post
    fields=['title','slug','description','content','tags']
    success_url=reverse_lazy('blog:index')
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('blog:index')