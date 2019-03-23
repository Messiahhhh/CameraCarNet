"""testss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from  myapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),        #admin后台路由
    url(r'^hello$', views.hello),            #你定义的路由，第一个参数为引号中的正则表达式，第二个参数业务逻辑函数（当前为views中的hello函数）
    url(r'^index/$',views.index),
    url(r'^gen/$',views.gen),
    url(r'^video_feed/$',views.video_feed),
    ]
