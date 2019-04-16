"""vrptn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from partners import views

urlpatterns = [
    path('admin/', admin.site.urls),  # admin后台路由
    path('hello/', views.hello),     # 自定义的路由，第一个参数为引号中的正则表达式，第二个参数业务逻辑函数（当前为views中的hello函数）
    path('index/', views.index),
    path('', views.index),
]
