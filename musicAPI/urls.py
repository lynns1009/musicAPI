"""musicAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from music import views


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^songs/',views.songs_list,name='songs_list'),
    url(r'^songs/(\d+)/', views.song_detail,name='song_detail'),
    url(r'albums/<int:pk>',views.album_detail,name='album_detail'),

]
