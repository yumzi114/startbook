from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from bookmark.models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

# Create your views here.

class BookmarkLV(ListView):
    model=Bookmark

class BookmarkDV(DetailView):
    model=Bookmark

class BookmarkCreateView(LoginRequiredMixin,CreateView):
    model=Bookmark
    fields=['title','url']
    success_url=reverse_lazy('bookmark:index')
    def form_valid(self, form):
        form.instance.owner=self.request.user
        return super().form_valid(form)

class BookmarkChangeLV(LoginRequiredMixin,ListView):
    template_name='bookmark/bookmark_change_list.html'
    #화면에 출력할 레코드리스트반환
    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)
class BookmarkUpdateView(OwnerOnlyMixin,UpdateView):
    #지정된 속성에 대한 내용만 보여줌
    model=Bookmark
    fields=['title','url']
    success_url=reverse_lazy('bookmark:index')
class BookmarkDeleteView(OwnerOnlyMixin,DeleteView):
    model=Bookmark
    success_url=reverse_lazy('bookmark:index')
