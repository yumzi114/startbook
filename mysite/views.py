from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin

# Create your views here.
class HomeView(TemplateView):
    template_name='home.html'
#usercreateview
class UserCreateView(CreateView):
    template_name='registration/register.html'
    form_class=UserCreationForm
    success_url=reverse_lazy('register_done')
class UserCreateDoneTV(TemplateView):
    template_name='registration/register_done.html'
###owner확인클레스##
class OwnerOnlyMixin(AccessMixin):
    raise_exception=True
    permission_denied_message="Owner only can Update/delete the object"
    def dispatch(self,request,*args,**kwargs):
        obj=self.get_object()
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request,*args,**kwargs)