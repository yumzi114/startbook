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

from django.urls import path,include
from . import views


app_name='photo'
urlpatterns = [
   path('',views.AlbumLV.as_view(),name='index'),
   path('album/',views.AlbumLV.as_view(),name='album_list'),
   path('album/<int:pk>/',views.AlbumDV.as_view(),name='album_detail'),
   path('photo/<int:pk>/',views.PhotoDV.as_view(),name='photo_detail'),
   path('album/add/',views.AlbumPhotoCV.as_view(),name='album_add'),
   path('album/change/',views.AlbumChangeLV.as_view(),name='album_change'),
   path('album/<int:pk>/update/',views.AlbumPhotoUV.as_view(),name='album_update'),
   path('album/<int:pk>/delete/',views.AlbumDelV.as_view(),name='album_delete'),
   path('photo/add/',views.PhotoCV.as_view(),name='photo_add'),
   path('photo/change/',views.PhotoChangeLV.as_view(),name='photo_change'),
   path('photo/<int:pk>/update/',views.PhotoUV.as_view(),name='photo_update'),
   path('photo/<int:pk>/delete/',views.PhotoDelV.as_view(),name='photo_delete'),

]
