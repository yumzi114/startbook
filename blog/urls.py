"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path,re_path
from blog import views
app_name='blog'
urlpatterns = [
    path('',views.PostLV.as_view(),name='index'),
    path('post',views.PostLV.as_view(),name='post_list'),
    re_path(r'^post/(?P<slug>[-\w]+)/$',views.PostDV.as_view(),name='post_detail'),
    path('archive',views.PostAV.as_view(),name='post_archive'),
    path('archive/<int:year>/',views.PostYAV.as_view(),name='post_year_archive'),
    path('archive/<int:year>/<str:month>',views.PostMAV.as_view(),name='post_month_archive'),
    path('archive/<int:year>/<str:month>/<int:day>/',views.PostDAV.as_view(),name='post_day_archive'),
    path('archive/today',views.PostTAV.as_view(),name='post_today_archive'),
    path('tag/',views.TagCloudTV.as_view(),name='tag_cloud'),
    path('tag/<str:tag>/',views.TaggedObjectLV.as_view(),name='tagged_object_list'),
    path('search/',views.SearchFormView.as_view(),name='search'),
]
